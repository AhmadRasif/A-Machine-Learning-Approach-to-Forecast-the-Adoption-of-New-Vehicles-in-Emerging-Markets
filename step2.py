#Exploratory Data Analysis (EDA)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ১. ক্লিন করা ডেটা লোড করা
df = pd.read_csv('Bangladesh_Vehicle_Data_Merged.csv')

# স্টাইল সেট করা
sns.set(style="whitegrid")

# ২. ট্রেন্ড দেখা (Yearly Registration Trend) 
# বছর এবং ফুয়েল টাইপ অনুযায়ী গ্রুপিং
yearly_trend = df.groupby(['REGISTRATION_YEAR', 'Fuel_Type'])['TOTAL'].sum().unstack().fillna(0)

# গ্রাফ তৈরি
plt.figure(figsize=(12, 6))
yearly_trend['Electric'].plot(kind='line', marker='o', color='green', label='Electric Vehicle (EV)')
plt.title('Bangladesh EV Registration Trend (2022-2025)')
plt.xlabel('Year')
plt.ylabel('Number of Registrations')
plt.xticks(yearly_trend.index)
plt.legend()
plt.show()

# ৩. মার্কেট লিডার (Top EV Manufacturers)
# শুধুমাত্র ইলেকট্রিক গাড়ি ফিল্টার করা
ev_only = df[df['Fuel_Type'] == 'Electric']
top_manufacturers = ev_only.groupby('MANUFACTURER_NAME')['TOTAL'].sum().sort_values(ascending=False).head(10)

# বার চার্ট তৈরি
plt.figure(figsize=(12, 6))
top_manufacturers.plot(kind='bar', color='skyblue')
plt.title('Top 10 EV Manufacturers in Bangladesh')
plt.xlabel('Manufacturer Name')
plt.ylabel('Total EVs Registered')
plt.xticks(rotation=45)
plt.show()

# ৪. গ্রোথ রেট হিসাব করা (EV Growth Rate %)
ev_yearly = yearly_trend['Electric']
# পার্সেন্টেজ চেঞ্জ হিসাব করা
growth_rate = ev_yearly.pct_change() * 100

print("--- EV Yearly Growth Rate (%) ---")
for year, rate in growth_rate.items():
    if pd.notnull(rate):
        print(f"In {year} growth rate : {rate:.2f}%")
    else:
        print(f"In {year} growth rate: N/A (ভিত্তি বছর)")

# ৫. মার্কেট শেয়ার (EV vs Non-EV)
total_market = df.groupby('Fuel_Type')['TOTAL'].sum()
plt.figure(figsize=(8, 8))
plt.pie(total_market, labels=total_market.index, autopct='%1.2f%%', colors=['lightgreen', 'lightcoral'], startangle=140)
plt.title('Overall Market Share: EV vs Non-EV')
plt.show()