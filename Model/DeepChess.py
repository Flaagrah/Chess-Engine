import tensorflow as tf

# Helper libraries
import numpy as np
import tensorflow.keras as keras
import random
import Utils.ModelGenerator as mg
def getBoardInit():
    return np.zeros((2, 6, 8, 8))


def convertBoolToNum(flag):
    if flag == True:
        return 1
    return 0

def convertBoardToMatrix(npBoard):
    #Initialize an empty board
    newBoard = getBoardInit()
    #Replicate the board position in matrix format
    for i in range(0,8):
        for j in range(0,8):
            b = npBoard[i][j]
            if b=='.':
                continue
            if b.isupper():
                color = 0
            else:
                color = 1
            piece = 0
            lower = b.lower()
            if lower == 'p':
                piece = 0
            elif lower == 'r':
                piece = 1
            elif lower == 'n':
                piece = 2
            elif lower == 'b':
                piece = 3
            elif lower == 'q':
                piece = 4
            elif lower == 'k':
                piece = 5
            newBoard[color][piece][i][j] = 1
    return np.reshape(newBoard, (768)).tolist()

# Data generator to create blackWin-whiteWin pairings
class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, whiteWins, blackWins, batch_size=50):
        self.whiteWins = whiteWins
        self.blackWins = blackWins
        self.batch_size = batch_size
        self.on_epoch_end()

    def __len__(self):
        # Assumes equal number of white wins and black wins
        return int(len(self.whiteWins) / self.batch_size)

    def __getitem__(self, index):
        perSide = int(self.batch_size / 2)
        wWins = self.whiteWins[index * self.batch_size:(index + 1) * self.batch_size]
        bWins = self.blackWins[index * self.batch_size:(index + 1) * self.batch_size]

        wWinsParsed = []
        bWinsParsed = []
        for i in range(0, self.batch_size):
            ww = convertBoardToMatrix(wWins[i][0])
            bw = convertBoardToMatrix(bWins[i][0])
            for h in range(0, 5):
                ww.append(wWins[i][1][h])
                bw.append(bWins[i][1][h])
            wWinsParsed.append(ww)
            bWinsParsed.append(bw)
        # ensure half of the white wins are on the left and the other half are on the right so the network does not become biased.
        leftSide = np.concatenate((wWinsParsed[0:perSide], bWinsParsed[0:perSide]))
        rightSide = np.concatenate((bWinsParsed[perSide:perSide * 2], wWinsParsed[perSide:perSide * 2]))
        total = [np.asarray(leftSide), np.asarray(rightSide)]
        result = np.asarray([[1, 0]])
        for i in range(1, perSide):
            result = np.append(result, [[1, 0]], axis=0)
        for i in range(perSide, perSide * 2):
            result = np.append(result, [[0, 1]], axis=0)

        return total, result

    def on_epoch_end(self):
        print("shuffle")
        random.shuffle(self.whiteWins)
        random.shuffle(self.blackWins)


if __name__ == '__main__':
    white = np.load("Model/sortedDataStr/whiteWins.npz")["states"]
    whiteBoolStates = np.load("Model/sortedDataStr/boolWhiteWins.npz")["bools"]
    print(len(white))
    black = np.load("Model/sortedDataStr/blackWins.npz")["states"]
    blackBoolStates = np.load("Model/sortedDataStr/boolBlackWins.npz")["bools"]
    print(len(black))

    whiteTest = np.load("Model/sortedDataStr/whiteWinsTest.npz")["states"]
    whiteBoolStatesTest = np.load("Model/sortedDataStr/boolWhiteWinsTest.npz")["bools"]
    print(len(whiteTest))
    blackTest = np.load("Model/sortedDataStr/blackWinsTest.npz")["states"]
    blackBoolStatesTest = np.load("Model/sortedDataStr/boolBlackWinsTest.npz")["bools"]
    print(len(blackTest))

    whiteWinData = []
    blackWinData = []
    for i in range(0,1000):
        whiteWinData.append([white[i], whiteBoolStates[i]])
        blackWinData.append([black[i], blackBoolStates[i]])
    trainGen = DataGenerator(whiteWinData, blackWinData, 50)
    # example = trainGen.__getitem__(0)
    # for i in range(0,50):
    #     print(example[1][i])
    whiteTestData = []
    blackTestData = []
    for i in range(0, 1000):
        whiteTestData.append([whiteTest[i], whiteBoolStatesTest[i]])
        blackTestData.append([blackTest[i], blackBoolStatesTest[i]])
    validGen = DataGenerator(whiteTestData, blackTestData, 50)

    totalModel = mg.genModel()

    #Determine how many results are wrong (out of a batch size of 50)
    def modelVal(y_true, y_pred):
        y_pred_round = tf.math.round(y_pred)
        y_true_round = tf.math.round(y_true)
        y_abs_diff = tf.abs(tf.subtract(y_pred_round, y_true_round))
        return tf.divide(tf.reduce_sum(y_abs_diff), tf.constant(2.0))

    lr = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.001, decay_steps=22000, decay_rate=0.9)
    opt = keras.optimizers.SGD(learning_rate=lr)
    totalModel.compile(optimizer=opt, loss=keras.losses.CategoricalCrossentropy(), metrics=[modelVal], loss_weights=None)

    validGen = DataGenerator(whiteTestData, blackTestData, 100)
    partTest = validGen.__getitem__(0)
    valInputs = partTest[0]
    valLabels = partTest[1]

    #totalModel.load_weights('totalModel50SGD')
    totalModel.fit(x=trainGen, epochs=100, validation_data=(valInputs, valLabels))

    inputs = valInputs
    labels = valLabels
    preds = totalModel.predict(inputs)


    npPreds = np.asarray(preds)
    npPreds = np.round(npPreds)

    numWrong = 0
    for i in range(0, len(preds)):
        if npPreds[i][0] > npPreds[i][1] and labels[i][0] < labels[i][1]:
            numWrong = numWrong + 1
        elif npPreds[i][0] < npPreds[i][1] and labels[i][0] > labels[i][1]:
            numWrong = numWrong + 1
        elif npPreds[i][0] == npPreds[i][1] or labels[i][0] == labels[i][1]:
            print(npPreds[i])
            numWrong = numWrong + 1

    print(numWrong)
    print(numWrong / len(preds))
    # The model has a ~84% success rate (it gets 15644 wrong out of 100,000). This is higher than the monkey score of 50%.

    #totalModel.save_weights('totalModel50SGD')