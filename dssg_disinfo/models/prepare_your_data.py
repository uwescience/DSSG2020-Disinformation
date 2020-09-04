from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from . import params_class
params=params_class.params()

def prepare_your_data(data):
    
    tokenizer = Tokenizer(num_words = params.vocab_size, oov_token='<OOV>')
    tokenizer.fit_on_texts(data['article_text'])
    data_processed = tokenizer.texts_to_sequences(data['article_text'])
    data_processed = pad_sequences(data_processed, padding='post', maxlen=params.maxlen, truncating='post')
    return data_processed