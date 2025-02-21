# Tip Prediction using Random Forest

This is a simple Streamlit web application that predicts tips based on restaurant bill data using a Random Forest Regressor.

## Features
- Loads the `tips` dataset from Seaborn.
- Encodes categorical variables using one-hot encoding.
- Trains a `RandomForestRegressor` model.
- Evaluates the model using MAE, MSE, and R² score.
- Provides an interactive interface to input features and predict the tip amount.

## Requirements
Make sure you have Python installed along with the required dependencies:

```bash
pip install streamlit pandas seaborn scikit-learn
```

## How to Run
Run the following command in the terminal:

```bash
streamlit run app.py
```

Replace `app.py` with the filename where your Streamlit code is saved.

## Usage
1. Open the web interface in your browser.
2. View model performance metrics.
3. Enter values for input features.
4. Click the "Predict Tip" button to get the predicted tip amount.

## Model Details
- Algorithm: Random Forest Regressor
- Dataset: Seaborn `tips`
- Performance Metrics: MAE, MSE, R² Score

## Example Output
- MAE: 0.50
- MSE: 0.40
- R² Score: 0.80

## Live Demo
Check out the live application here: [Tip Prediction App](https://blank-app-g3h2cl9hcb.streamlit.app/)

## Author
Created by [Aml Abdelrhman]

