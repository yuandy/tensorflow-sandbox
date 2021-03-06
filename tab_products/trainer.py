import tensorflow as tf

def optimizer(logits, labels, learn_rate, global_step):
  with tf.variable_scope('optimizer') as scope:
    cross_entropy      = tf.nn.sparse_softmax_cross_entropy_with_logits(logits, labels, name='cross_entropy')
    cross_entropy_mean = tf.reduce_mean(cross_entropy, name='cross_entropy_mean')
    tf.add_to_collection('losses', cross_entropy_mean)
    loss               = tf.add_n(tf.get_collection('losses'), name='total_loss')
    train_opt          = tf.train.AdamOptimizer(learn_rate).minimize(loss, global_step=global_step, name='train_opt')
    tf.scalar_summary('cross_entropy', cross_entropy_mean)
    tf.scalar_summary('loss', loss)
  return train_opt

def evaluater(logits, labels):
  with tf.variable_scope('evaluater') as scope:
    prediction = tf.equal(tf.argmax(logits,1), labels, name='prediction')
    accuracy   = tf.reduce_mean(tf.cast(prediction, tf.float32), name='accuracy')
    tf.scalar_summary('accuracy', accuracy)
  return accuracy
