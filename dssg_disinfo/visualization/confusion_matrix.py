from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import pandas as pd 
import matplotlib
from matplotlib import pyplot as plt
import os
import seaborn as sns


def plot_confusion_matrix(predicted_labels, model_arch):
    ''' Plots confusion matrix based on true vs.
    predicted labels and saves the plot as png in the
    Graph folder. 

    Parameters

    -----------
    obj

        predicted_labels  - csv file containing predicted and validation 
        labels. 

    str
        model - model name such as 'word_embedding', 'basic', 'multiple'

    Returns
    -------
    none
            
    '''

    
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'Graphs/')
    
    data = pd.read_csv(predicted_labels)
    cm = confusion_matrix(data['label'], data['predicted_label'], normalize='true')
    sns.set()
    ax = sns.heatmap(cm, annot=True, fmt='.1%', cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["lightcyan","yellow","teal"]))
    ax.set_title("Confusion Matrix - " + model_arch)
    ax.set(xlabel='Predicted Label', ylabel='True Label')
    file_name = 'confusion_matrix'+'_'+ model_arch + '.png'
    plt.savefig(results_dir + file_name)

    return 
