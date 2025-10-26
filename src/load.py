def load_csv_file(df):
    df.to_csv('data/report.csv', index=False)
    print('Create successfully file csv in data folder')