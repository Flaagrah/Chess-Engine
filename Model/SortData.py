import numpy as np
#Sorting data based one which side won the game

def sortData(whiteWins, boolWhiteWins, blackWins, boolBlackWins, start, end, inc):
    for i in range(start, end, inc):
        states = np.load("Data/boardStr/boardStates"+str(i)+".npz")["states"]
        results = np.load("Data/resultStr/results"+str(i)+".npz")["results"]
        boolStates = np.load("Data/boardStateBools/boardStatesBools"+str(i)+".npz")["states"]

        for j in range(0, len(states)):
            if results[j] == 1:
                whiteWins.append(states[j].tolist())
                boolWhiteWins.append(boolStates[j].tolist())
            elif results[j] == 0:
                blackWins.append(states[j].tolist())
                boolBlackWins.append(boolStates[j].tolist())


whiteWinStatesTest = []
blackWinStatesTest = []
boolWhiteWinStatesTest = []
boolBlackWinStatesTest = []

whiteWinStates = []
blackWinStates = []
boolWhiteWinStates = []
boolBlackWinStates = []

sortData(whiteWinStates, boolWhiteWinStates, blackWinStates, boolBlackWinStates, 1000, 280000, 1000)
sortData(whiteWinStatesTest, boolWhiteWinStatesTest, blackWinStatesTest, boolBlackWinStatesTest, 280000, 330000, 1000)
np.savez("sortedDataStr/whiteWins.npz", states=np.asarray(whiteWinStates))
np.savez("sortedDataStr/boolWhiteWins.npz", bools=np.asarray(boolWhiteWinStates))
np.savez("sortedDataStr/blackWins.npz", states=np.asarray(blackWinStates))
np.savez("sortedDataStr/boolBlackWins.npz", bools=np.asarray(boolBlackWinStates))
np.savez("sortedDataStr/whiteWinsTest.npz", states=np.asarray(whiteWinStatesTest))
np.savez("sortedDataStr/boolWhiteWinsTest.npz", bools=np.asarray(boolWhiteWinStatesTest))
np.savez("sortedDataStr/blackWinsTest.npz", states=np.asarray(blackWinStatesTest))
np.savez("sortedDataStr/boolBlackWinsTest.npz", bools=np.asarray(boolBlackWinStatesTest))