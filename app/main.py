import os

from pipeline.extract import extract_data
from pipeline.load import load_data
from pipeline.transform import union_df

if __name__ == '__main__':
    abspath = os.path.abspath('data/input/')
    print(abspath)

    data = extract_data(abspath)
    df = union_df(data)
    load_data(df, 'data/output/', 'output.xlsx')
