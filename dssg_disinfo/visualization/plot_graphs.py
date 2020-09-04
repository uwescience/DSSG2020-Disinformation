import numpy as np
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
import os

def plot_graphs(log_file, model_arch):
    ''' Plots model output metrics such as 
    accuracy, etc. for a given model and
    saves a png file with the results. 
    The name of the file will be a string =
    history+metric

    Parameters

    -----------
    obj

        log_file  - csv log containing validation accuracy, 
        loss, etc. collected after an instance of a model has been fit 
    str
        model_arch - model name (i.e. 'word_embedding', 'basic', 'multiple')


    Returns
    -------
    none
            
    
    '''    

    data = pd.read_csv(log_file, sep=';')
    
    # plotting loss 
    ax = plt.figure(figsize=(15,8)).gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.plot(data['epoch'], data.iloc[:,[2,4]])#data[['val_loss','loss']])
    plt.legend(data[['val_loss','loss']])
    plt.title('Loss for Training and Validation' + ' - ' + model_arch)
    plt.xlabel("Epochs")
    plt.ylabel("Loss") 
    file_name_loss= model_arch + '_'+ 'loss_'+datetime.now().strftime('%Y%m%d%H%M%S')+'.png'
    plt.savefig(file_name_loss)

    # plotting accuracy 
    ax = plt.figure(figsize=(15,8)).gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    accuracy= plt.plot(data['epoch'], data.iloc[:,[1,3]])
    plt.legend(['validation data','training data'])
    plt.title('Area Under the Curve for Training and Validation Data' + ' - ' + model_arch)
    plt.xlabel("Epochs")
    plt.ylabel("AUC")   
    file_name_acc= model_arch + '_'+ 'auc_'+datetime.now().strftime('%Y%m%d%H%M%S')+'.png'
    plt.savefig(file_name_acc)
       
    return
