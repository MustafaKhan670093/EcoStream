a = tf.truncated_normal([16,128,128,3])
sess = tf.Session()
sess.run(tf.initialize_all_variables())
sess.run(tf.shape(a))



b=tf.reshape(a,[16,49152])
sess.run(tf.shape(b))

classes = ['dogs', 'cats']
num_classes = len(classes)
 
train_path='training_data'
 
# validation split
validation_size = 0.2
 
# batch size
batch_size = 16
 
data = dataset.read_train_sets(train_path, img_size, classes, validation_size=validation_size)


def create_weights(shape):
    return tf.Variable(tf.truncated_normal(shape, stddev=0.05))
 
def create_biases(size):
    return tf.Variable(tf.constant(0.05, shape=[size]))




tf.nn.max_pool(value=layer,
                               ksize=[1, 2, 2, 1],
                               strides=[1, 2, 2, 1],
                               padding='SAME')


def create_convolutional_layer(input,
               num_input_channels, 
               conv_filter_size,        
               num_filters):  
    
    ## We shall define the weights that will be trained using create_weights function.
    weights = create_weights(shape=[conv_filter_size, conv_filter_size, num_input_channels, num_filters])
    ## We create biases using the create_biases function. These are also trained.
    biases = create_biases(num_filters)
 
    ## Creating the convolutional layer
    layer = tf.nn.conv2d(input=input,
                     filter=weights,
                     strides=[1, 1, 1, 1],
                     padding='SAME')
 
    layer += biases
 
    ## We shall be using max-pooling.  
    layer = tf.nn.max_pool(value=layer,
                            ksize=[1, 2, 2, 1],
                            strides=[1, 2, 2, 1],
                            padding='SAME')
    ## Output of pooling is fed to Relu which is the activation function for us.
    layer = tf.nn.relu(layer)
 
    return layer


def create_flatten_layer(layer):
    layer_shape = layer.get_shape()
    num_features = layer_shape[1:4].num_elements()
    layer = tf.reshape(layer, [-1, num_features])
 
    return layer


def create_fc_layer(input,          
             num_inputs,    
             num_outputs,
             use_relu=True):
    
    #Let's define trainable weights and biases.
    weights = create_weights(shape=[num_inputs, num_outputs])
    biases = create_biases(num_outputs)
 
    layer = tf.matmul(input, weights) + biases
    if use_relu:
        layer = tf.nn.relu(layer)
 
    return layer






x = tf.placeholder(tf.float32, shape=[None, img_size,img_size,num_channels], name='x')
 
y_true = tf.placeholder(tf.float32, shape=[None, num_classes], name='y_true')
y_true_cls = tf.argmax(y_true, dimension=1)




layer_conv1 = create_convolutional_layer(input=x,
               num_input_channels=num_channels,
               conv_filter_size=filter_size_conv1,
               num_filters=num_filters_conv1)
 
layer_conv2 = create_convolutional_layer(input=layer_conv1,
               num_input_channels=num_filters_conv1,
               conv_filter_size=filter_size_conv2,
               num_filters=num_filters_conv2)
 
layer_conv3= create_convolutional_layer(input=layer_conv2,
               num_input_channels=num_filters_conv2,
               conv_filter_size=filter_size_conv3,
               num_filters=num_filters_conv3)
          
layer_flat = create_flatten_layer(layer_conv3)
 
layer_fc1 = create_fc_layer(input=layer_flat,
                     num_inputs=layer_flat.get_shape()[1:4].num_elements(),
                     num_outputs=fc_layer_size,
                     use_relu=True)
 
layer_fc2 = create_fc_layer(input=layer_fc1,
                     num_inputs=fc_layer_size,
                     num_outputs=num_classes,
                     use_relu=False)






y_pred = tf.nn.softmax(layer_fc2,name="y_pred")


cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=layer_fc2,
                                                    labels=y_true)
cost = tf.reduce_mean(cross_entropy)



optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)





batch_size = 16
 
x_batch, y_true_batch, _, cls_batch = data.train.next_batch(batch_size)
 
feed_dict_train = {x: x_batch,
                           y_true: y_true_batch}
 
session.run(optimizer, feed_dict=feed_dict_tr)



x_valid_batch, y_valid_batch, _, valid_cls_batch = data.valid.next_batch(train_batch_size)
 
feed_dict_val = {x: x_valid_batch,
                      y_true: y_valid_batch}
 
val_loss = session.run(cost, feed_dict=feed_dict_val)


optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)

 
batch_size = 16
 
x_batch, y_true_batch, _, cls_batch = data.train.next_batch(batch_size)
 
feed_dict_train = {x: x_batch,
                           y_true: y_true_batch}
 
session.run(optimizer, feed_dict=feed_dict_tr)

x_valid_batch, y_valid_batch, _, valid_cls_batch = data.valid.next_batch(train_batch_size)
 
feed_dict_val = {x: x_valid_batch,
                      y_true: y_valid_batch}
 
val_loss = session.run(cost, feed_dict=feed_dict_val)

Python

correct_prediction = tf.equal(y_pred_cls, y_true_cls)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


correct_prediction = tf.equal(y_pred_cls, y_true_cls)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


val_acc = session.run(accuracy,feed_dict=feed_dict_validate)

acc = session.run(accuracy, feed_dict=feed_dict_train)

saver.save(session, 'dogs-cats-model')

