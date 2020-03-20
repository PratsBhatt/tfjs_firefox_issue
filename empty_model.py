import tensorflow as tf
import tensorflowjs as tfjs

tfjs_target_dir = './'

BATCH_SIZE = 1

vocab_size = 62

# The embedding dimension
embedding_dim = 64

# Number of RNN units
rnn_units = 512

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform')),
      tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(rnn_units,
                          return_sequences=True,
                          stateful=True,
                          recurrent_initializer='glorot_uniform')),
    tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(vocab_size))
  ])
  return model

model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=BATCH_SIZE)


model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy())

model.summary()

tfjs.converters.save_keras_model(model, tfjs_target_dir)