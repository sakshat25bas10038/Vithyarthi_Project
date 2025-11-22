# Problem Statement
Predicting the occurrence of a destructive tsunami immediately following a major earthquake is crucial for early warning systems. This project addresses the need for a data-driven model that uses the physical characteristics of the seismic event to provide an automated, statistical assessment of the probability of tsunami generation.

# Scope of the Project
The project scope is focused on demonstrating a complete, foundational ML workflow within a single environment: from raw data upload to model training and visualization.
The system will:
#### 1) Use the Global Earthquake-Tsunami Risk Assessment Dataset with the binary tsunami indicator.
#### 2) Implement and train a Logistic Regression model in the notebook.
#### 3) Use key seismic features: magnitude, depth, latitude, and longitude.
#### 4) Demonstrate proper data splitting (80% train / 20% test) and feature scaling techniques.
#### 5) Validate model performance, successfully achieving an Accuracy Score exceeding 82% on the test set.

# Target Users
#### 1) First-Year Engineering Students: 
Used as a portfolio piece demonstrating proficiency in Python, Data Handling, and Machine Learning.
#### 2) Geophysical Analysts: 
Users who require a quick, statistically-validated tool for initial tsunami risk screening.

# High-Level Features (Functional Modules)
### 1) Data Acquisition & Preparation
Handles all data ingestion, cleaning (missing value imputation), train/test split, and Standard Scaling of numerical features to optimize model training.
### 2) Logistic Regression Training
Trains the Logistic Regression model, which outputs key evaluation metrics (Accuracy, Precision, Recall) by testing against the unseen test data.
### 3) Results & Visualization
Uses the trained model to generate final predictions and creates a 2D scatter plot to visually demonstrate the model's classification of tsunami events based on the relationship between earthquake, magnitude and depth.

