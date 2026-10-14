# Project Report: Data Classification Using AI

**Organization:** DecodeLabs  
**Project:** Artificial Intelligence — Project 2  
**Project title:** Data Classification Using AI  
**Algorithm:** K-Nearest Neighbors (KNN)  
**Dataset:** Iris dataset

## 1. Introduction
Classification is a supervised machine-learning task in which a model learns from labelled examples and predicts the class of new examples. This project implements a basic classification pipeline using the Iris dataset. The work covers data loading, inspection, splitting, model training, and evaluation.

## 2. Objective
The objective is to build and evaluate a simple AI classification model on a small dataset, following the requirements in the provided project brief.

## 3. Dataset Description
The Iris dataset contains 150 samples and four numeric features: sepal length, sepal width, petal length, and petal width. Each sample belongs to one of three flower species: setosa, versicolor, or virginica. The dataset is included in scikit-learn, so no separate download is required. The program exports the dataset to a CSV file for inspection.

## 4. Methodology
1. Load the Iris dataset and inspect its dimensions, features, class names, and class distribution.
2. Split the data into 80% training and 20% testing subsets. Stratification keeps the class proportions similar in both subsets.
3. Standardize the numeric features. This is important for KNN because it compares distances between samples.
4. Compare values of `k` from 1 to 15 using five-fold cross-validation on the training data. The test set is not used for selecting `k`.
5. Train the final KNN model with the selected `k`.
6. Predict the labels of the held-out test samples.
7. Evaluate the predictions using accuracy, weighted precision, weighted recall, weighted F1-score, and a confusion matrix.

## 5. Algorithm
K-Nearest Neighbors classifies a sample by finding its `k` closest training samples and assigning the most common class among those neighbors. A very small `k` can be sensitive to noise, while a very large `k` can blur boundaries between classes. Cross-validation is used to select a suitable value based on training data.

## 6. Implementation
The implementation is in `main.py`. It uses pandas for tabular data handling and scikit-learn for dataset access, train/test splitting, scaling, KNN, cross-validation, and metrics. Matplotlib and Seaborn create the evaluation charts. A Pipeline ensures scaling is fitted separately inside each cross-validation fold and on the training set for final evaluation.

## 7. Results
Run `python main.py` to produce the actual metrics for the selected environment and fixed split. The terminal output and `outputs/metrics.json` contain the selected `k`, accuracy, weighted precision, weighted recall, weighted F1-score, per-class classification report, and confusion matrix. The project also generates `outputs/confusion_matrix.png`, `outputs/k_selection.png`, and `outputs/test_predictions.csv`.

**Important:** Do not enter guessed performance numbers into a submission. Use the values printed by your own run and, if required, insert them here:
- Selected k: ______
- Test accuracy: ______
- Weighted precision: ______
- Weighted recall: ______
- Weighted F1-score: ______

## 8. Conclusion
This project demonstrates the fundamental supervised-learning workflow: load labelled data, separate training and testing samples, fit a classifier, and evaluate predictions. KNN provides an understandable baseline for a small multi-class dataset. Using multiple evaluation metrics and a confusion matrix gives a more complete picture than accuracy alone.

## 9. Possible Improvements
- Compare KNN with Decision Tree, Logistic Regression, or Support Vector Machine.
- Test repeated stratified cross-validation.
- Add a small user interface that accepts flower measurements and returns a predicted species.
- Test on a different dataset to check how well the workflow generalizes.
