# Laptop Price Prediction Project

This project predicts laptop prices using Machine Learning regression algorithms. The dataset is cleaned, preprocessed, analyzed, and trained using multiple regression models including Linear Regression, Ridge Regression, KNN, Decision Tree, SVR, Random Forest, AdaBoost, Gradient Boosting, and XGBoost.

The best-performing model (Gradient Boosting Regressor) is exported using Pickle and can be used in a Streamlit web application.

## Project Workflow

1. Load Dataset  
2. Data Cleaning  
3. Remove Unnecessary Columns  
4. Feature Engineering  
5. Exploratory Data Analysis  
6. Data Preprocessing  
7. Model Training  
8. Model Evaluation  
9. Model Export  

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Pickle

## Feature Engineering

- Extracted Touchscreen and IPS Panel features
- Calculated PPI (Pixels Per Inch)
- Processed CPU, GPU, RAM, Storage, and Operating System features
- Converted target column using log transformation

## Models Used

- Linear Regression
- Ridge Regression
- K-Nearest Neighbors
- Decision Tree Regressor
- Support Vector Regressor
- Random Forest Regressor
- AdaBoost Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

## Best Model

Gradient Boosting Regressor achieved the best performance and was selected for deployment.

## Model Export

```python
pickle.dump(df, open('df.pkl', 'wb'))
pickle.dump(pipe_gb, open('gb.pkl', 'wb'))


