from src.extract import extract_data
from src.transform import transform_data
from src.load import load_csv_file

path = 'data/orders.csv'

def run_pipe_line():
    df = extract_data(path)
    df = transform_data(df)
    load_csv_file(df)
    print('Pipeline data run succeessfully')

if __name__ == '__main__':
    run_pipe_line()