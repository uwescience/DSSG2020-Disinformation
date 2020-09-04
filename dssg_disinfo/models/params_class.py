class params(object):
    '''
    The params class object tracks the parameters for the entire modeling 
    process and all the corresponding functions.
    
    Inputs:
    none
    
    Returns:
    none
    '''
    
    # define the default parameters live in the init argument list:
    def __init__(self,
                 oov_token='<OOV>',
                 truncating='post',
                 embedding_dim=300,
                 epochs=3,
                 optimizer='adam',
                 bidir_num_filters=64,
                 dense_1_filters=10,
                 embedding_path=None,
                 dropout_rate=0.2,
                 vocab_size = 10000,
                 maxlen=681
                 ):
        self.oov_token = oov_token
        self.truncating = truncating
        self.embedding_dim = embedding_dim
        self.epochs = epochs
        self.optimizer = optimizer
        self.bidir_num_filters=bidir_num_filters
        self.dense_1_filters=dense_1_filters
        self.embedding_path=embedding_path
        self.dropout_rate=dropout_rate
        self.vocab_size = vocab_size
        self.maxlen= maxlen
