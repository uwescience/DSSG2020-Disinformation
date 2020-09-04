from .model_arch import *
from .baseline_model import *
from .build_model import *
from .param_tune import *
from .get_data import *
from .word_embedding_arch import *

# Importing the default parameters
from . import params_class
params= params_class.params()

def run_model(model_arch='basic', **copacabana):
    """Run a model type specified by the model_arch.
    default parameters stored in the params_class
    will be used if not overwritten by user in **copacabana
    
    input
    -----
    model_arch: string, the type of the model
    **copacabana: parameteres
    
    output
    ------
    file_name: 
    """
    
    # Calling the default parameters
    default_params = {value:items for value, items in params.__dict__.items()}
    # Storing all the parameters into copacabana, parameters passed by user will overwrite default
    copacabana = {k: copacabana.get(k, default_params[k]) for k in default_params.keys()}
    
    if model_arch == 'basic': # basic model- LSTM
        
        file_name=param_tune(model_arch, **copacabana) #returns file name with epoch logs for the best model
        # plot_graphs(file_name) # Plug the correct plot graph here

    elif model_arch == 'multiple': # two input model- linguistic features and text input
        
        #model=build_model(model_arch=model_arch, **copacabana)
        #compiled_model=compile_model(model)
        file_name = fit_and_run_model(create_multiple_model_arch(**copacabana), model_arch= model_arch, 
                                      **copacabana)
    
    elif model_arch == 'word_embedding': # word embedding model, pulls in word_embedding file specified by user.
        file_name=param_tune(model_arch, **copacabana)
        # plot_graphs(file_name) # Plug the plot thing here
    else:
        print("Invalid model type entered entered!")
        file_name= None
    
    print("That's all folks!")
    
    return file_name
