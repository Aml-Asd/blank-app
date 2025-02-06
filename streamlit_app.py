import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = sns.load_dataset("tips")


df = pd.get_dummies(df, drop_first=True)

X = df.drop("tip", axis=1)
y = df["tip"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)


mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

st.title("Tip Prediction")



st.write("### Model Performance Evaluation")
st.write(f"- MAE: {mae:.2f}")
st.write(f"- MSE: {mse:.2f}")
st.write(f"- R² Score: {r2:.2f}")

st.write("### Predict Tip for a New Example")
input_features = {}
for col in X.columns:
    input_features[col] = st.number_input(f"{col}", value=float(X_train[col].mean()))
input_df = pd.DataFrame([input_features])
if st.button("Predict Tip"):
    result = model.predict(input_df)[0]
    st.success(f"Predicted Tip: {result:.2f}")
