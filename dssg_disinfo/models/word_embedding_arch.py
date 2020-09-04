from .model_arch import *
from .get_data import *

def create_embedding_matrix(filepath, word_index, embedding_dim):
    """ creates embedding matrix from pretrained vectors
    
    input
    -----
    filepath: path to pretrained vectors
    word_index: dictionary, the word index of training corpus
    embedding_dim: integer, dimensions of the pretrained vectors
    
    output
    ------
    embedding_matrix: 2 dimensional array
    """
    vocab_size = len(word_index) + 1  # Adding again 1 because of reserved 0 index
    
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    
    with open(filepath) as f:
        for line in f:
            l = len(line.split())
            word = line.split()[0]
            vector = line.split()[-embedding_dim:]
            if word in word_index:
                idx = word_index[word] 
                embedding_matrix[idx] = np.array(
                    vector, dtype=np.float32)[:embedding_dim]

    return embedding_matrix

def create_word_embd_model_arch(embedding_dim=300, bidir_num_filters=64, dense_1_filters=10, vocab_size=10000, maxlen=681, dropout_rate=0.2, optimizer='adam'):
    """ developing word embedding for the corpus
    
    input
    -----
    embedding_dim: integer, dimensions of the pretrained vectors
    bidir_num_filters: integer, number of filters for LSTM layer
    dense_1_filters: integer, number of filters for Dense layer
    vocab_size: integer, number of words to select from entire corpus
    maxlen: integer, number of words taken per column
    dropout_rate: float, between 0 and 1
    optimizer: string
    
    output
    ------
    model: compiled model withs input weights set with word embeddings
    """
    
    #embedding_path=input("Enter path of word embedding:")
    embedding_path = '/data/dssg-disinfo/glove.trained.preprocessed.merged1.vectors.300d.txt'
    #embedding_path='/data/dssg-disinfo/coronavirus-corpus/chunks/wv.txt' #200 dimension embedding

    (X_train, X_test, y_train, y_test, word_index) = get_data_and_split(vocab_size=10000,
                                                                        maxlen=681,
                                                                        model_arch='word_embedding',
                                                                        multiple=False,
                                                                        scaler=False) 

    embedding_matrix=create_embedding_matrix(filepath=embedding_path,
                                        word_index=word_index, embedding_dim=embedding_dim)
    
    vocab_size = len(word_index) + 1 # Adding again 1 because of reserved 0 index
    
    model = keras.Sequential([
        
        keras.layers.Embedding(vocab_size, embedding_dim,
                                   weights=[embedding_matrix],
                                   input_length=maxlen),
        keras.layers.Bidirectional(keras.layers.LSTM(bidir_num_filters)),
        keras.layers.Dense(dense_1_filters, activation='relu'),
        keras.layers.Dropout(rate=dropout_rate),
        keras.layers.Dense(1, activation='sigmoid')
        ])
        
        
    model.compile(optimizer=optimizer,loss='binary_crossentropy', metrics=[tf.keras.metrics.AUC()])
    
    return model

# Register the basic model (writing into our dictionary of models)
register_model_arch("word_embedding", create_word_embd_model_arch,
                    ["embedding_path", "bidir_num_filters", "dense_1_filters", "vocab_size", "embedding_dim", "maxlen",  "optimizer","dropout_rate", "word_index"])
        
