#This work is based on the following research paper:
#https://www.cs.tau.ac.il/~wolf/papers/deepchess.pdf
# The purpose of this notebook is to create an autoencoder that does dimensionality reduction on a vector of size 773 which represents the current position on the board.
import tensorflow as tf

# Helper libraries
import numpy as np
import tensorflow.keras as keras


states = np.load("board/boardStates1000.npz")["states"]
results = np.load("result/results1000.npz")["results"]

for i in range(2, 10):
    numStr = str(i)+"000"
    print(i)
    tstates = np.load("board/boardStates"+numStr+".npz")["states"]
    tresults = np.load("result/results"+numStr+".npz")["results"]
    states = np.concatenate((states, tstates), axis=0)
    results = np.concatenate((results, tresults), axis=0)

states2 = np.load("board/boardStates11000.npz")["states"]
results2 = np.load("result/results11000.npz")["results"]

states3 = np.load("board/boardStates12000.npz")["states"]
results3 = np.load("result/results12000.npz")["results"]

#This is used to evaluate how well the first layer of the encoder is able to replicate the positions
def encoderEvaluation(y_true, y_enc):
    y_enc_round = tf.math.round(y_enc)
    y_true_round = tf.math.round(y_true)
    return tf.divide(tf.reduce_sum(tf.abs(tf.subtract(y_true, y_enc_round))), tf.cast(tf.size(y_true), tf.float32))
    #return tf.reduce_sum(tf.abs(tf.subtract(y_true_round, y_enc_round)))

#autoencoder = keras.models.load_model('autoencoder', custom_objects={"encoderEvaluation": encoderEvaluation})

#Reduce 773 to 600
encoder_input = keras.Input(shape=(773,))
enc_first_layer = keras.layers.Dense(600, activation="relu")(encoder_input)
decoding = keras.layers.Dense(773, activation="sigmoid")(enc_first_layer)

autoencoder = keras.Model(encoder_input, decoding)
lr = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.005, decay_steps=50, decay_rate=0.98)
opt = keras.optimizers.Adam(learning_rate=lr)
autoencoder.compile(optimizer=opt, loss='binary_crossentropy', metrics=[encoderEvaluation])
len(states)

autoencoder.fit(states, states, epochs=5, batch_size=50, shuffle=True, validation_data=(states2, states2))
#autoencoder.save('autoencoder')

#helper method for layerwise training
def readyForNext(autoencoder, nodes, prevNodes):
    #new_model = keras.Model(autoencoder.input, autoencoder.layers[-2].output)
    for layer in autoencoder.layers:
        layer.trainable = False
    newLayer = keras.layers.Dense(nodes, activation="relu", name="newDense"+str(nodes))(autoencoder.layers[-2].output)
    newOutput = keras.layers.Dense(prevNodes, activation="relu", name="newOutput"+str(nodes))(newLayer)
    newModel = keras.Model(autoencoder.input, newOutput)
    oldModel = keras.Model(autoencoder.input, autoencoder.layers[-2].output)
    return newModel, oldModel

#autoencoder2 = keras.models.load_model('autoencoder2')

def trainNextLayer(prevAutoEncoder, nodes, prevNodes, decay_steps, decay_rate):
    autoencoderNext, old = readyForNext(prevAutoEncoder, nodes, prevNodes)
    print(autoencoderNext.summary())
    print(old.summary())
    for layer in autoencoderNext.layers:
        print(layer.trainable)

    predictions = old.predict(states)
    validation_preds = old.predict(states2)

    # Train the second layer of size 400
    lr = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.001, decay_steps=decay_steps, decay_rate=decay_rate)
    opt = keras.optimizers.Adam(learning_rate=lr)
    autoencoderNext.compile(optimizer=opt, loss=tf.keras.losses.MeanSquaredError())
    autoencoderNext.fit(states, predictions, epochs=50, batch_size=1000, verbose=1, shuffle=True, validation_data=(states2, validation_preds))
    return autoencoderNext

autoencoder2 = trainNextLayer(autoencoder, 400, 600, 1200, 0.8)
# autoencoder2, old = readyForNext(autoencoder, 400, 600)
# print(autoencoder2.summary())
# print(old.summary())
# for layer in autoencoder2.layers:
#     print(layer.trainable)
#
# predictions = old.predict(states)
# validation_preds = old.predict(states2)
#
# #Train the second layer of size 400
# lr = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.001, decay_steps=1200, decay_rate=0.8)
# opt = keras.optimizers.Adam(learning_rate=lr)
# autoencoder2.compile(optimizer=opt, loss=tf.keras.losses.MeanSquaredError())
# autoencoder2.fit(states, predictions, epochs = 50, batch_size=1000, verbose=1, shuffle=True, validation_data=(states2, validation_preds))
# autoencoder2.save('autoencoder2')

autoencoder3 = trainNextLayer(autoencoder2, 200, 400, 1200, 0.95)
#autoencoder3 = keras.models.load_model('autoencoder3')
# autoencoder3, old = readyForNext(autoencoder2, 200, 400)
# print(autoencoder3.summary())
# print(old.summary())
# for layer in autoencoder3.layers:
#     print(layer.trainable)
#
# predictions = old.predict(states)
# validation_preds = old.predict(states2)
#
# #Train third layer
#
# lr = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.001, decay_steps=1200, decay_rate=0.95)
# opt = keras.optimizers.Adam(learning_rate=lr)
# autoencoder3.compile(optimizer=opt, loss=tf.keras.losses.MeanSquaredError())
# autoencoder3.fit(states, predictions, epochs = 50, batch_size=1000, verbose=1, shuffle=True, validation_data=(states2, validation_preds))
#autoencoder3.save('autoencoder3')

autoencoder4 = trainNextLayer(autoencoder3, 100, 200, 1200, 0.95)
#Train last layer. Dimensions are reduced to 100
# autoencoder4, old = readyForNext(autoencoder3, 100, 200)
# print(autoencoder4.summary())
# print(old.summary())
# for layer in autoencoder3.layers:
#     print(layer.trainable)
#
# predictions = old.predict(states)
# validation_preds = old.predict(states2)
#
# #Train final layer of autoencoder
# lr = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.001, decay_steps=1200, decay_rate=0.95)
# opt = keras.optimizers.Adam(learning_rate=lr)
# autoencoder4.compile(optimizer=opt, loss=tf.keras.losses.MeanSquaredError())
# autoencoder4.fit(states, predictions, epochs = 50, batch_size=1000, verbose=1, shuffle=True, validation_data=(states2, validation_preds))
#autoencoder4.save('autoencoder4')
