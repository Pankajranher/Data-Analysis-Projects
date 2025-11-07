import pandas as pd

def loading_and_cleaning_data(file_path):              # the file path take from app.py
    df = pd.read_csv('data\\sales_data.csv', parse_dates=['Date'])
    df.dropna(inplace=True)
    df['Month'] = df['Date'].dt.to_period('M')
    
    return df


# Loadaing and cleaning the data
df = loading_and_cleaning_data(r"data")

print("Data loaded and cleaned successfully!")
print(df.head())



