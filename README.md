# Global Earthquake-Tsunami Risk Probability Classifier

## Project Overview
This project implements a foundational Machine Learning system designed to assess the potential risk of an earthquake generating a destructive tsunami. It performs Binary Classification using key seismic features to predict the Tsunami Indicator (tsunami: 1 for Tsunami, 0 for No Tsunami). The entire workflow is executed within a single Google Colab environment, with the model trained directly on the uploaded data using Logistic Regression.

## Features
### 1) Data uploads and cleaning :-
#### Manually upload the csv file dataset.csv (opendatasets module) - "https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset"
#### Cleaning of NaN values in data set (Pandas module) - After reading the csv file no NaN values found
#### Splitting of data in 80/20 ratio (scikit-learn module) - By importing train_test_split
### 2) Logistic Regression Model :-
#### Applies Feature Scaling - import StandardScaler
#### Model training - import LogisticRegression
#### Classificatiion - - Accuracy Score 0.8265.
### 3) Prediction & Visualization :-
#### Trained model used for probability predictiction of dataset - Probability output
#### Scatter plot with earthquake magnitude and depth as factors - (matplotlib module)

## Technologies and Tools Used
### 1) Modules Used :-
Numpy, Matplotlib, Scikit-learn, Pandas are used for data handling, modelling and visualization. 
### 2) Machine Learning Model :-
Logistic Regression Model is trained for simple, interpretable linear classifier ideal for demonstrating foundational ML on binary outcomes.
### 3) Execution Environment :-
Google Collab is used as it is organised and freely accessible.

## Steps to Install & Run the Project
### Prequesities :-
You must have Kaggle account and an API Key configured to download the dataset using the opendatasets library. Open the Tsunami_Classifier_Colab.ipynb file in Google Colab.
### Execution :-
#### 1) Install Libraries: Run the initial cell to install dependencies
##### !pip install pandas numpy scikit-learn matplotlib
##### !pip install opendatasets kaggle
#### 2) Data Acquisition: Run the cell to download the dataset. You will be prompted to enter your Kaggle username and Key
##### import opendatasets as od
##### od.download("https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset")
#### 3) Data Loading: Run the cell to load the downloaded CSV file into a DataFrame
##### import pandas as pd
##### data=pd.read_csv("/content/global-earthquake-tsunami-risk-assessment-dataset/earthquake_data_tsunami.csv")
#### 4) Model Training: Run the cell containing the Logistic Regression training block (Data Split, Scaling, Training, and Evaluation). This output includes the final model accuracy (e.g., Accuracy Score: 0.8265)
#### 5) Prediction & Visualization (Section 3): Run the final cells to generate the predicted results and display the Magnitude vs. Depth scatter plot



