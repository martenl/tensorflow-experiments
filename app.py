import tensorflow as tf

x = tf.placeholder(tf.float32,name="x")

y = tf.placeholder(tf.float32,name="y")

z = tf.add(x,y)

with tf.Session() as sess:
    print(sess.run(z,feed_dict={x:2.0,y:3.0}))