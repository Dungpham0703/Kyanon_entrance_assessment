import pandas as pd

def transform_data(df):
    df_filtered = df[df['status'] == 'completed']

    df_report = df_filtered.groupby('order_date')['amount'].sum().reset_index()

    print(df_filtered)
    print(df_report)
    
    print('Transform successfully')
    return df_report