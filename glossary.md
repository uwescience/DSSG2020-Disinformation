---
layout: page
title: Glossary
---

These are the terms that we will be using commonly throughout our project:

## 1. Area Under the Curve (AUC)

Area Under Curve is a commonly used metric to evaluate model performance when the training data is imbalanced. It tries to strike a balance between maximizing correct identification of disinformation and reducing mislabeling of legitimate articles. A model whose predictions are 100% wrong has an AUC of 0.0; one whose predictions are 100% correct has an AUC of 1.0.

You can read more about the concept behind AUC [here](https://www.analyticsvidhya.com/blog/2020/06/auc-roc-curve-machine-learning/#:~:text=The%20Area%20Under%20the%20Curve,summary%20of%20the%20ROC%20curve.&text=So%2C%20the%20higher%20the%20AUC,between%20positive%20and%20negative%20classes).

## 2. Confusion Matrix

A confusion matrix is a 2x2 matrix that shows true labels and predicted labels each of the axis. This matrix is useful in determining the performance of supervised  machine learning model. Refer to this [wikipedia](https://en.wikipedia.org/wiki/Confusion_matrix) page for more information.

## 3. Cross Validation

Cross validation is a method used commonly in supervised machine learning to avoid overfitting the model to the training data and to improve the prediction accuracy of the model.

Cross validation is done with the training data. In each iteration, training data is split into n parts. This number n is usually 5 by default. Each of these parts is then treated as a test data set that is held out and the model is trained on the left over n-1, lets say 4 parts.

After each run the test accuracies are recorded and eventually the final trained model is developed with averaged out weights learned during each iteration.

You can learn in detail about this process [here](https://scikit-learn.org/stable/modules/cross_validation.html).

## 4. Loss Curves

Loss curves are commonly used to evaluate and diagnose model optimization only. 

In the context of an optimization algorithm, the function used to evaluate a candidate solution (i.e. a set of weights) is referred to as the objective function.

We may seek to maximize or minimize the objective function, meaning that we are searching for a candidate solution that has the highest or lowest score respectively.

Typically, with neural networks, we seek to minimize the error. As such, the objective function is often referred to as a cost function or a loss function and the value calculated by the loss function is referred to as simply “loss.” This is [article](https://machinelearningmastery.com/loss-and-loss-functions-for-training-deep-learning-neural-networks/) explains it in more detail.

## 5. Vectors

In our project, a numerical array which represents a word is being refered to as a vector. The dimension of the vector in the code was provided by embedding_dim argument.

We have majorly used two dimensions 200 and 300. This means that all the words in the corpus will be represented by a 200 dimensional vector. These vectors will be useful in determining how similar or dissimilar the words are.


## 6. Word Embeddings

We have converted our text articles into vectors. These vectors are called word embeddings.

When we come across two sentences like *cat* is sleeping there and *dog* was running here, our brain is able to infer that the words *cat* and *dog* are more similar to each other because they share common features. Like they are both animals, they are both cute.

Similarly, we get similar vectors for words that have more features in common and vectors that are far apart for words that have less features in common.

In our project, these features were developed from articles which were separate from our training data.

This helps in ensuring that the vectors that we are generating can be used across domains and different times and not dependent completely on the training data.

You can read more about the concept of word embeddings [here](https://machinelearningmastery.com/what-are-word-embeddings/).
