import tensorflow as tf

a = tf.constant("hello tf")
sess = tf.Session()
print(sess.run(a))
