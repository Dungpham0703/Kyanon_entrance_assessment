import pandas as pd

def extract_data(path):
    df = pd.read_csv(path)
    print(df)
    print(f'Extracting successfully {len(df)} rows from csv file from {path}')
    return df