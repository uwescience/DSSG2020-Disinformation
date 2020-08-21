---
layout: page
title: Methods
---

**Data**

The data for this project were collected by our partner organization, Global Disinformation Index  (GDI), and consists of genuine news articles and content identified to contain disinformation. The data were scraped from the internet using the software Veracity and provided to us in two separate .csv files:

    (1) articles labeled as containing disinformation

    (2) articles labeled as legitimate news articles 

All samples are related to coronavirus and were published between May and June 2020. Before any cleaning processes, the disinformation article dataset consisted of 20,172 samples and the legitimate article dataset included 14,278. 

The Global Disinformation Index also provided a separate corpus that was used to train word embeddings. This corpus (1.3 GiB) contained over 574,000 unlabeled articles about coronavirus. We chose to train word embeddings on this separate corpus in order to ensure that our model would learn from a set of articles it has never seen thereby minimizing overfitting.

**Tools (aka “component specification”)**

In order to prepare the data for modelling, we did the following:

    1. Removed all duplicates in the article text column (i.e. any articles that had exactly the same text).

    2. Removed any observations which were missing the article text.

    3. Removed all non-English articles. 

    4. Identified all embedded hyperlinks and replaced them with ‘HTMLEMBD’. 

    5. Tokenized article text. 

The following packages were used in data processing, feature engineering and modelling stages of the project:  NLTK, Pandas, SciPy, SpaCy,  Keras, TensorFlow, numpy, matplotlib and sklearn. We also used other libraries to train our word embeddings in Glove and Word2Vec. These libraries are Fasttext and Gensim libraries respectively. The outcomes from these approaches were saved in text files which were referenced in our word embedding model.

**Processes**

We conducted some exploratory analyses on the data using Jupyter Notebooks. These analyses included descriptive and summary statistics as well as data visualizations. 

In order to prepare the data for natural language processing analysis, we performed a series of data cleaning steps. First, we combined the two datasets into one. Next, we removed all duplicates in the article text column (i.e. any articles that had exactly the same text) as well as any observations which were missing the article text. We then used the Language-Detection library in Python to identify and remove any non-English articles. 

After basic data cleaning described above, we conducted a series of preprocessing steps to further wrangle the text data, in turn getting it ready for machine learning. The steps for prepping are evolving as we are gaining more understanding of the models that we want to use. However, some of the steps that we have tried so far are:

* Tokenizing (breaking sentences/phrases into individual words)
* Removing stop words (words that don't add much meaning to a sentence, such as 'the', 'that', 'a')
* Word embeddings (creating mathematical vector representations of words)

In the upcoming weeks, we will need to extract features from the text data through further data processing.  Currently, we plan on extracting both linguistic features (i.e. average sentence length, average use of nouns) as well as text representation features (where each word is transformed into mathematical vector).  A different process is required to extract each type, with NLP used for the latter and some form of word embeddings (Word2Vec, Bag of Words, used for the latter). 

The following diagram captures the overall workflow of this project, starting with data cleaning and processing and culminating in selection of the final model. Once the data is prepped it is divided into test and train data. While training the model the train data is also used to cross-validate the model to make sure that the chosen model has the highest performance. Finally, the performance of a model is evaluated by how well it is able to predict the test data categories.

![Image of disinformation narratives](assets/img/Pipeline.png)

**Analyses**

*Model 1: Baseline Model*

This model acts as a baseline model for the next 2 models. Model 1 is a Recurrent Neural Network LSTM (Long Short Term Memory) model which takes the article texts as input and predicts whether the article is disinformation or legitimate. The model embeds the article text as vectors which are then fed into a bidirectional LSTM layer.

![Baseline model](assets/img/model.1.png)

This model has validation AUC (Area under the Curve) ranging from 97.6-98.6% across 7 epochs and training AUC ranging from 95.1-99.7%.

    1. The why?
    
Methods such as Tfidf, word count frequencies are very commonly used as predictors of different categories. Our idea was to not only look at what is the        frequency of the words appearing in an article but also the context in which they appear.

![Context](assets/img/context.png)

For example, in the following sentence:

The <b><ins>pandemic</ins></b> has been <b><ins>tough</ins></b> on our people. While there have been some signs of recovery, <b><ins>coronavirus</ins></b> has put us in a <b><ins>challenging</ins></b> position.

We wanted to find a way to find an association between words pandemic, tough and also coronavirus and challenging because they appear in a similar context. These associations can be a very strong way to tell apart disinformation articles from legitimate articles. We decided to use the Long Short Term Memory Model to train our data.

    2. Architecture

Layers of the model:

![Context](assets/img/layers1.png)

1. Embedding layer: 
This layer takes in the article text as input and generates word embeddings.
2. Bidirectional LSTM layer
This layer helps build the context of the word embedding inputs.
3. Dense layer
4. Dropout layer
We added a dropout layer as a method to help model avoid overfitting. The dropout rate is a number between 0 and 1. 
5. Output layer
Binary output in the form of 0 and 1. 0 if the news article is predicted as legitimate and 1 if the news article is predicted as disinformation.

    3. Features

This model takes as input the news article text. The news article text is passed into the model after preprocessing like removing noisy characters, removing duplicates etc. You can read more about the preprocessing steps <a href="https://uwescience.github.io/DSSG2020-Disinformation/methods/">here<a>
    
The first layer of the model converts the text data into word embeddings. Word embedding is a way of converting a text corpus into an array of numbers by representing those numbers across multi-dimensional features.



**Limitations**

One big limitation of our work has to do with the raw data itself. The articles that form our genuine samples were scraped from professionally written and credible sources, whereas the disinformation samples come from a more varied set of sources, including personal blogs and  web-pages, which are inherently noisier and probably differ in writing style/tone in comparison to genuine subset. This might have a detrimental effect on the reliability of our final model - we want it to predict disinformation content as opposed to amateurly written content. But, since the genuine content is exclusively professionally written, we need to take extra precaution to train our model to make a distinction between articles in a way that doesn't automatically label personal blogs as containing disinformation. 
