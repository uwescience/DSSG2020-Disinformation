---
layout: page
title: Methods
---

**Data**

The data for this project was collected by our partner organization, Global Disinformation Index, and consists of news articles that have been identified as either genuine or to contain disinformation narratives. It was scraped from the internet using the software Veracity and provided to us in two separate .csv files: (1) articles labeled as disinformation and (2) articles labeled as genuine. Our raw data provides domain name of the scraped website, article headline and the text of the article. We are primary working with Article Text, although have been thinking about how to leverage the other two variables.

Before any cleaning processes, the disinformation article dataset included 14,000 rows and the genuine article dataset included 19,000 rows.

**Tools (aka “component specification”)**

For data cleaning, preprocessing,and data modelling we are mostly relying on the following packages/libraries: NLTK, Pandas, scipy, and sklearn. We anticipate that a few more libraries will be used in the feature engineering process (i.e. word embedding packages such as Word2Vec). We are also working on streamlining some of our main script by developing individual modules in Python targeted as a specific task (i.e. data cleaning, embedded link analysis, etc.). Since all of these tools were designed for Python, they are already interoperable. 

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

Although we are still brainstorming which models are most appropriate for this given task, the following are close contenders and the team has tried their hand at a few of these already in some capacity:

* Logistic Regression Classifier
* Naive Bayes Classifier
* Random Forest
* Neural Networks

This list is a work in progress.

**Analyses**

At this point, we haven't finalized building our models. However, once that part of the pipeline is complete, we are planning to evaluate each model we develop with the following tests:

* Precision score (true positives / (true positives + false positives))
* Accuracy score (true positives + true negatives / total observations)
* Recall score (true positives / (true positives + false negatives)

**Limitations**

One big limitation of our work has to do with the raw data itself. The articles that form our genuine samples were scraped from professionally written and credible sources, whereas the disinformation samples come from a more varied set of sources, including personal blogs and  web-pages, which are inherently noisier and probably differ in writing style/tone in comparison to genuine subset. This might have a detrimental effect on the reliability of our final model - we want it to predict disinformation content as opposed to amateurly written content. But, since the genuine content is exclusively professionally written, we need to take extra precaution to train our model to make a distinction between articles in a way that doesn't automatically label personal blogs as containing disinformation. 
