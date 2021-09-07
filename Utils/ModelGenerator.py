import tensorflow.keras as keras
import tensorflow as tf
def genModel():
    def encoderEvaluation(y_true, y_enc):
        y_enc_round = tf.math.round(y_enc)
        y_true_round = tf.math.round(y_true)
        return tf.divide(tf.reduce_sum(tf.abs(tf.subtract(y_true, y_enc_round))), tf.cast(tf.size(y_true), tf.float32))
        #return tf.reduce_sum(tf.abs(tf.subtract(y_true_round, y_enc_round)))

    def popLayer(model):
        for layer in model.layers:
            layer.trainable = True
        output = model.layers[-2].output
        newModel = keras.Model(model.input, output)
        return newModel

    def complexEncoderName(complexEncoder, s):
        complexEncoder.layers[0]._name = "input1"+s
        complexEncoder.layers[1]._name = "coded1"+s
        complexEncoder.layers[2]._name = "coded2"+s
        complexEncoder.layers[3]._name = "coded3"+s
        complexEncoder.layers[4]._name = "coded4"+s
        #Train every layer except the input layer. The autoencoder should be trained to extract information relevant to determining winning/losing positions
        for layer in complexEncoder.layers:
            layer.trainable = True
        return complexEncoder


    complexEncoder1 = complexEncoderName(keras.models.load_model('../Model/Pretraining/autoencoder4', custom_objects={"encoderEvaluation": encoderEvaluation}), 's')

    input1 = keras.layers.Input((773,))
    input2 = keras.layers.Input((773,))
    tower1 = complexEncoder1(input1)
    tower2 = complexEncoder1(input2)
    for l in complexEncoder1.layers:
        print(l.trainable)

    combined = tf.keras.layers.Concatenate(axis=1)([tower1,tower2])
    print(combined.shape)
    layer1 = keras.layers.Dense(400, activation="relu", name="input_analyze1")(combined)
    layer2 = keras.layers.Dense(200, activation="relu", name="input_analyze2")(layer1)
    layer3 = keras.layers.Dense(100, activation="relu", name="input_analyze3")(layer2)
    output = keras.layers.Dense(2, activation="softmax", name="final_output")(layer3)
    totalModel = keras.Model(inputs=[input1, input2], outputs=output)
    totalModel.summary()
    return totalModel