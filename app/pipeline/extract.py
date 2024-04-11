import os # for file operations
import glob # for file operations
import pandas as pd
from typing import List


def extract_data(file_path: str) -> List[pd.DataFrame]:
    """
    Function to read all csv files in the folder and return a single dataframe.
    Parameters: 
        file_path (str): path to the folder containing csv files
    Returns:
        data_frame_list (List[pd.DataFrame]): List of dataframes read from csv files
    """
    # Read all csv files in the folder
    all_files = glob.glob(os.path.join(file_path, "*.xlsx"))
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))
    print(f'Data have been extracted successfully. Dataframes: {len(data_frame_list)}')
    return data_frame_list