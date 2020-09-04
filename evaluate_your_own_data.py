import pandas as pd
from dssg_disinfo.models.prepare_your_data import prepare_your_data
import tensorflow as tf
import sys

#'../../../data/dssg-disinfo/articles_v3_50.csv' ## This was used for testing

'''
This python file reads data passed by the user while calling evaluate_your_own_data.sh file

Example: $ ./evaluate_your_own_data.sh '../../../data/dssg-disinfo/articles_v3_50.csv'

The csv file will be passed into this file as sys.argv[1].
The data is then processed by prepare_your_data function.
Once the data passed by the user is processed it is evaluated against the trained model.
'''

my_data = pd.read_csv(sys.argv[1]) # Replace this path with path to your data
processed_data=prepare_your_data(my_data)

load_model = tf.keras.models.load_model('output/best_model.h5') # calls the trained model saved in the /output folder

# Evaluate the trained model
loss, acc = load_model.evaluate(processed_data,  my_data['label'], verbose=2)
print('Loaded model, loss: {:5.2f}'.format(loss))
print('Loaded model, accuracy: {:5.2f}%'.format(100*acc))