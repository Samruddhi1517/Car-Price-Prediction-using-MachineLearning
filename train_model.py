import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("car data.csv")

# Feature Engineering
df["Car_Age"] = 2025 - df["Year"]
df.drop(["Car_Name", "Year"], axis=1, inplace=True)

df = pd.get_dummies(df, drop_first=True)

X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
pickle.dump(model, open("car_price_model.pkl", "wb"))

print("Model saved successfully!")