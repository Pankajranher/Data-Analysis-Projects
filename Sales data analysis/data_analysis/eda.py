def get_kpis(df):
    return {
        'Total Sales': df['Sales'].sum(),               # calculating total saless
        'Total Profit': df['Profit'].sum(),          # calculating total profit
        'Total Quantity': df['Quantity'].sum(),      # calculating total quantity
        'Average Discount': df['Discount'].mean()       # calculating average
    }

def get_sales_by_category(df):
    return df.groupby('Category')["Sales"].sum().reset_index()
    # print(df.groupby('Category')["Sales"].sum().reset_index())