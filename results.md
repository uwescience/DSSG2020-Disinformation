---
layout: page
title: Results
---

**Findings**

What were the outcomes of your analyses?

| Model Name      | Layers |      Accuracy| Recall |
| :---        |    :----:   |          ---: |
| Model 1      |        |       |             |
| Model 2   |         |          |           |



True Positives: Disinformation articles that were correctly predicted as disinformation by the model.
True Negatives: Disinformation articles that were incorrectly predicted as genuine by the model.
False Positives: Genuine articles that were incorrectly predicted as disinformation by the model.
False Negatives: Genuine articles that were correctly predicted as genuine by the model.


*ROC curves for each  of the model*
PLACEHOLDER PICTURE HERE? 


*Training Loss and Validation Loss curve*
PLACEHOLDER PICTURE HERE? 

What is your interpretation of those findings?
Our findings demonstrate the predictive efficacy of our model. In addition to the hidden features of our neural network model, the linguistic features that we extracted from the corpus using natural language processing techniques improve (?) our model accuracy by further quantifying the complexity of disinformation text characteristics.

We developed word embeddings from a larger corpus to train our data and this made the model perform ________.

The model is able to predict the disinformation correctly _____ of the times. It is falsely labeling genuine news articles as disinformation _____ of times. Our hypothesis for why this is happening is _______.

These findings suggest that the ………. model is performing better compared to other models we also implemented. Based on these findings, we think that this model will be generalizable to other coronavirus-related disinformation corpora and will likely also achieve high accuracy in predicting whether an article contains disinformation or not in such corpora. We encourage researchers and others using our model and other artifacts to test their efficacy for classifying disinformation in other datasets.

*LIMITATIONS???*


**Deliverables**

What artifacts or outputs did you produce?
We have produced a predictive model which will be able to predict a news article as disinformation or genuine. In the process of developing this model we have also developed the following artifacts:


Trained embeddings (news articles on COVID)
Working with text data requires that it is not only processed in accordance with standard natural language processing principles (standardizing, normalizing) but that it is also converted into a mathematical representation which then allows for more advanced machine learning. As described in the Methods section, word embeddings allow for such a transformation of text. There are many pre-trained word embeddings that are available to researchers (GloVe, Word2Vec). However, based on discussions with GDI and our data science team we chose to train our own GloVe embeddings on a subset of articles provided by GDI. This corpus was not part of our training dataset, and besides training word embeddings was not used for any other purpose. We produced a 300 dimension word embedding from a text corpus of ______ MB/GB. There are ______ unique vocabulary words in these embeddings. These embeddings can be used independently to train other natural language models.


We checked the output of these embeddings against other pre-trained embeddings for comparison purposes. For instance, the word “Trump” was associated with ____ and ___ in our bespoked model, while in the GloVe model it was associated with ____ and ____. 

(PASTE IMAGE BELOW SHOWING MOST SIMILAR WORDS FOR ‘VIRUS’ FOR OUR TRAINED WORD EMBEDDING MODEL AND PRE-TRAINED ONE). 

We ran the same model using GloVe pre-trained and our own embeddings, and the outcome confirmed our hypothesis that custom-trained embeddings on recently collected article texts result in better model performance than pre-trained word embeddings as measured by ______. This result lends support to the advantages  of relying on custom word embeddings over pre-trained embeddings, in spite of the fact that custom embeddings such as ours are trained on much smaller corpus. 


Annotated Bibliography
Throughout this project, our team relied heavily on literature review to inform our methodology. Our focus was on surveying the most recent literature on article classification with machine learning. We’ve read a total of ___ papers and documented key summaries in an annotated bibliography available in the public repository. This document serves as a guidepost for our thinking process, assumptions as well as framework within which this project took place. Our aim was to build on top of most recent wisdom in text classification. 




How will these deliverables be used? 

The deliverables will be used to design a larger model which will be able to provide disinformation indexes for news websites. Such an index can inform advertisers about the “health” of a news website and thereby stopping advertising content on “unhealthy” websites. 

**Outcomes**

How have your stakeholders responded to your deliverables? 

The stakeholders- GDI (Global Disinformation Index) are very ________ about the deliverables. (TBD)


What impact has your project had, or do you anticipate it having? 


Accurate, reliable, and timely health information is critical to combating any large-scale health emergency, such as the current and ongoing coronavirus pandemic. In February of 2020, the Director-General of the World Health Organization, Tedros Adhanom Ghebreyesus, famously said, “We’re not just fighting an epidemic; we’re fighting an infodemic.” (https://www.un.org/en/un-coronavirus-communications-team/un-tackling-‘infodemic’-misinformation-and-cybercrime-covid-19) An infodemic refers to the proliferation of information about a topic so that the realm is flooded by both real and fake information and one may have trouble locating reliable and evidence-based information. While disinformation continues to be a problem that plagues the internet, it has been particularly dangerous in an era when people need access to critical health and prevention guidance. In the United States, the coronavirus pandemic has shown no signs of abating and, instead, has increased in intensity with many states experiencing new records in cases, hospitalizations, and deaths (Need to check/find source). Some of this spread and other adverse outcomes, even some deaths, have resulted from coronavirus disinformation. 

As such, the importance of continuing to disarm and defund disinformation efforts as well as increase public awareness of the corresponding “infodemic” about coronavirus. Our work in this project added to the field by developing a long short term memory (LSTM) recurrent neural network model by which to classify news websites as disinformation versus not. We anticipate that this work will be utilized by our partner organization, Global Disinformation Index, by informing their current model as well as future model development. Additionally, other researchers and organizations studying disinformation may also find our model and documentation useful as res Specifically, our classifier model may be adapted as the pandemic continues or reworked to address disinformation surrounding the upcoming election in November 2020, in the United States.

In terms of educating the wider public, we will present our findings at the end of the Data Science for Social Good Program in a talk that is open to the public and will be attended by key stakeholders. Additionally, we hope to consolidate and summarize our findings into a manuscript for publication in a high impact, peer-reviewed journal and/or one or more conference presentations in the coming months in order to disseminate the model we’ve developed and the knowledge that we’ve accumulated from the extant literature, exploration of our coronavirus corpus, and from key domain experts.

