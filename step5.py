#Supervised Learning (Random forest)

from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# ডেটা তৈরি (আগের বছরের বিক্রয়কে ফিচার হিসেবে ব্যবহার করা)
# Year, Lag_1 (আগের বছর) -> Current_Sales
df_ml = pd.DataFrame({
    'Year': [2023, 2024, 2025],
    'Lag_1': [9, 61, 267],
    'Target': [61, 267, 223]
})

X = df_ml[['Year', 'Lag_1']]
y = df_ml['Target']

# মডেল ট্রেনিং
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# ২০২৬ সালের জন্য প্রেডিকশন
next_year_pred = rf_model.predict([[2026, 223]])
print(f"Random Forest Prediction for 2026: {next_year_pred[0]:.2f}")