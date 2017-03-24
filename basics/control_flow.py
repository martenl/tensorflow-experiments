import tensorflow as tf

#x = tf.placeholder(tf.float32)
#y = tf.placeholder(tf.float32)
#cond = tf.greater(x,y)
#select = tf.cond(cond,lambda: tf.subtract(x,y),lambda: tf.subtract(y,x))

def euclid():
    a = tf.placeholder(tf.int32)
    b = tf.placeholder(tf.int32)

    inside_block = lambda: tf.cond(tf.greater(a,b),lambda: tf.subtract(a,b),lambda: tf.subtract(a,b))
    block =  tf.while_loop(lambda: tf.not_equal(b,0),inside_block,[a,b])

    result = tf.cond(
        lambda: tf.equal(a,0),
        lambda: b,
        lambda: block)

    return a,b,result

a,b,result = euclid()

with tf.Session() as sess:
    print(sess.run(result,feed_dict={a:6,b:3}))