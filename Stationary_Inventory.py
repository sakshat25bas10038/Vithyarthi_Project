!pip install pandas numpy scikit-learn matplotlib
!pip install kaggle

!pip install opendatasets

import opendatasets as od
od.download("https://www.kaggle.com/datasets/ahmeduzaki/global-earthquake-tsunami-risk-assessment-dataset")

data.info()

if 'classifier_model' in locals() and 'x_scaled_all' in locals() and len(x_scaled_all) > 0:
   
    predictions = classifier_model.predict(x_scaled_all)
    data['is_tsunami_predicted'] = predictions
    
    probabilities = classifier_model.predict_proba(x_scaled_all)[:, 1]
    data['tsunami_probability'] = probabilities
    
    print("\n--- Top 5 Earthquake Events with Tsunami Risk Prediction ---")
    print(data[['magnitude', 'depth', 'is_tsunami_predicted', 'tsunami_probability']].head())

else:
    print("Prediction skipped: Model or scaled data not available. Please ensure Section 2 ran without errors.")

import matplotlib.pyplot as plt

if 'is_tsunami_predicted' in data.columns:
    
    plt.figure(figsize=(10, 6))
    
    scatter = plt.scatter(
        data['depth'],
        data['magnitude'],
        c=data['is_tsunami_predicted'], 
        cmap='coolwarm',                
        alpha=0.7,
        edgecolors='k'                  
    )
    
    plt.xlabel('Earthquake Depth (km)')
    plt.ylabel('Earthquake Magnitude')
    plt.title('Predicted Tsunami Risk by Magnitude and Depth (Logistic Regression)')
    
    plt.legend(*scatter.legend_elements(), title="Predicted Tsunami (1/0)")
    
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.gca().invert_xaxis()
    
    plt.show()

else:
    print("Visualization skipped: Predictions were not generated.")
