# dssg-disinfo
DSSG 2020 Online disinformation classification project

# Using Deep Learning to identify Disinformation news articles online

Websites that disseminate disinformation about coronavirus likely contribute to public harm by sowing confusion and distrust as well as preventing people from taking appropariate prevention measures or engagin gin dangerous fake treatment and cures, which could result in increased virus transmission, morbidity, and mortality worldwide.

Developing a method to identify disinformation sites could mitigate these harmful effects by allowing advertisers to not fund such sites. The purpose of this project is to develop an open-source natural language processing model that can accurately classify news articles according to their risk of containing disinformation about the coronavirus.

See [project web page](https://uwescience.github.io/DSSG2020-Disinformation/).

## Pre-requisites

To run the code following pre-requisite should be met:
1. Data must be present in form of a csv file at /data/dssg-disinfo/ folder. The csv file must have three columns ```article_pk```, ```article_text```, and ```label```.
```label``` is a binary column with value 1 if the ```article_text``` is disinformation and 0 if the ```article_text``` is legitimate.
```article_pk``` is a unique identifier for the ```article_text```.
```article_text``` is a string column which contains the articles scraped from the websites. Each column is an article either disinformation or legitimate.

2. You can also create an environment file in the dssg_disinfo folder (or same location as where the Dockerfile is present) . This environment file should have the following variables defined:

``` 
ENV DATA_PATH "/data"
ENV ALL_FEATURES_DATA articles.csv 
```
Here ```DATA_PATH``` is the location from where the data will be read.
```ALL_FEATURES_DATA``` should be the name of the csv file where the data is stored (present at ```DATA_PATH``` specified above). Read Pre-requisite point 1. for more details on the required format for the data file.
 
3. The output from the code will be saved in a ```/output``` folder in the current working directory. To read about the different types of outputs that are generated please read the Output section.

## Running

1. Build the docker.
```$ docker build --tag dssg-disinfo/testdocker "$PWD"```

2. Run the docker.
The following command will read in the data from /data/dssg-disinfo folder, run the Dockerfile and save the outputs generated from the code inside /output folder.
```$ docker run -it --rm -v /data/dssg-disinfo:/data -v $PWD/output:/output dssg-disinfo/testdocker```


## Output
The following outputs are produced by the code:
1. _log file_- A csv file is created for the best model (after hypertuning across a range of parameters) for all the epochs. The log contains epoch number, loss, validation loss, auc accuracy and auc accuracy for validation. The log file is saved in the ```/output``` folder.

2. _predict file_- A csv file that stores the original label and the predicted label of the validation data. This predict file can be used for developing confusion matrix or for further analysis of the labels assigned by the model. The predict file is saved in the ```/output``` folder.

3. _article_pk file_ - A csv file that stores the article primary keys of the articles that were used in the validation data set. This file can be used in combination with _predict file_ to identify which articles were incorrectly labelled for a further analysis. The article pk file is saved in the ```/output``` folder.

4. _Plots_- Two .png plots are saved in the ```/output``` folder. One plot is showing loss for validation and testing data across the epochs and the other plot shows the auc accuracies for validation and testing data.

5. _Trained model_ - A .h5 file that stores the trained model. This model can be used to evaluate the performance of the model on new data. The model is saved in the ```/output``` folder.


## Model Evaluation
_NOTE_ This step can be done if there is a trained model present in the ```/output``` folder.

_NOTE_ The csv file must have three columns ```article_pk```, ```article_text```, and ```label```.
```label``` is a binary column with value 1 if the ```article_text``` is disinformation and 0 if the ```article_text``` is legitimate.
```article_pk``` is a unique identifier for the ```article_text```.
```article_text``` is a string column which contains the articles scraped from the websites. Each column is an article either disinformation or legitimate.

If you want to evaluate the saved model for your own data you need to perform the following steps:
Run ```$ ./evaluate_your_own_data.sh 'PATH/TO/YOUR/DATA.csv'```
