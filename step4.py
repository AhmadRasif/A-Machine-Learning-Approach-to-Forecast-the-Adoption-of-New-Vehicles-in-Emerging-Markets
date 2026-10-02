#Time-Series Forecasting

import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# ইভি ডেটা সিরিজ
data = [9, 61, 267, 223]
index = pd.date_range(start='2022', periods=4, freq='Y')
ts = pd.Series(data, index=index)

# Holt's Linear Trend Model (কারণ ইভি ট্রেন্ড ঊর্ধ্বমুখী)
model = ExponentialSmoothing(ts, trend='add', seasonal=None).fit()

# পরবর্তী ৫ বছরের পূর্বাভাস
forecast_steps = 5
forecast = model.forecast(forecast_steps)

print("Next 5 Years Forecast:")
print(forecast)