#Bass Diffusion Model 

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# previous ডেটা (ফাইল থেকে পাওয়া)
years = np.array([1, 2, 3, 4]) # ২০২২=১, ২০২৩=২...
sales = np.array([9, 61, 267, 223])
cum_sales = np.cumsum(sales)

# Bass Model Function
def bass_model(t, p, q, M):
    return M * (((p + q)**2 / p) * np.exp(-(p + q) * t)) / (1 + (q / p) * np.exp(-(p + q) * t))**2

# মডেল ফিটিং (প্যারামিটার p, q এবং M খুঁজে বের করা)
# M = সম্ভাব্য মোট মার্কেট সাইজ (ধরি বাংলাদেশে ইভি মার্কেট আপাতত ৫০,০০০)
popt, _ = curve_fit(bass_model, years, sales, p0=[0.01, 0.1, 50000])

p, q, M = popt
print(f"Innovation (p): {p:.4f}, Imitation (q): {q:.4f}, Market Potential (M): {int(M)}")

# ২০৩০ পর্যন্ত পূর্বাভাস
future_t = np.linspace(1, 10, 100)
forecast = bass_model(future_t, p, q, M)

plt.plot(future_t + 2021, forecast, label='Bass Forecast')
plt.scatter(years + 2021, sales, color='red', label='Actual Sales')
plt.title("Bass Diffusion Model: EV Adoption in Bangladesh")
plt.legend()
plt.show()