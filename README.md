# Global Earthquake-Tsunami Risk Probability Classifier

## Project Overview
This project implements a foundational Machine Learning system designed to assess the potential risk of an earthquake generating a destructive tsunami. It performs Binary Classification using key seismic features to predict the Tsunami Indicator (tsunami: 1 for Tsunami, 0 for No Tsunami). The entire workflow is executed within a single Google Colab environment, with the model trained directly on the uploaded data using Logistic Regression.

## Features
### 1) Data uploads and cleaning :-
Manually upload the csv file dataset.csv (opendatasets module) - "https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset"
Cleaning of NaN values in data set (Pandas module) - After reading the csv file no NaN values found
Splitting of data in 80/20 ratio (scikit-learn module) - By importing train_test_split
### 2) Logistic Regression Model :-
Applies Feature Scaling - import StandardScaler
Model training - import LogisticRegression
Classificatiion - - Accuracy Score 0.8265.
### 3) Prediction & Visualization :-
Trained model used for probability predictiction of dataset - Probability output
Scatter plot with earthquake magnitude and depth as factors - (matplotlib module)

## Technologies and Tools Used
1) 
