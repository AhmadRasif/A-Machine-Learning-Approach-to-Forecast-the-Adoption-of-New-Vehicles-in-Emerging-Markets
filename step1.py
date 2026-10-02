# Data preparation and cleaning

import pandas as pd


file_path = 'EV and NON EV _REGISTRATION_nov2025.xls' 

try:
    
    ev_df = pd.read_excel(file_path, sheet_name='Electric', skiprows=1)
    non_ev_df = pd.read_excel(file_path, sheet_name='NON Electric', skiprows=1)

    #ফুয়েল টাইপ কলাম যোগ করা
    ev_df['Fuel_Type'] = 'Electric'
    non_ev_df['Fuel_Type'] = 'Non-Electric'

    # ডাটা merge করা 
    df_master = pd.concat([ev_df, non_ev_df], ignore_index=True)

    # কলামের নাম ও ডাটা ফরম্যাট ঠিক করা
    df_master.columns = df_master.columns.str.strip() # বাড়তি স্পেস বাদ দেওয়া
    df_master['MANUFACTURER_NAME'] = df_master['MANUFACTURER_NAME'].astype(str).str.upper().str.strip()
    
    # সংখ্যা জাতীয় কলামগুলো ঠিক করা
    df_master['REGISTRATION_YEAR'] = pd.to_numeric(df_master['REGISTRATION_YEAR'], errors='coerce').fillna(0).astype(int)
    df_master['TOTAL'] = pd.to_numeric(df_master['TOTAL'], errors='coerce').fillna(0)

    # রেজাল্ট সেভ করা
    df_master.to_csv('Bangladesh_Vehicle_Data_Merged.csv', index=False)

    print("সফলভাবে মাস্টার ফাইল তৈরি হয়েছে: 'Bangladesh_Vehicle_Data_Merged.csv'")
    print(df_master.head())

except Exception as e:
    print(f"Error logic: {e}")