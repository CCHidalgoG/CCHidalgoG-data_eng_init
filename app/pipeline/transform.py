import pandas as pd
from pipeline.extract import extract_data


def union_df(data):
    """
    Function to concatenate all dataframes in the list into a single dataframe.
    Parameters:
        data_list (List[pd.DataFrame]): List of dataframes
    Returns:
        pd.DataFrame: Single dataframe containing all dataframes in the list
    """
    df = pd.concat(data, ignore_index=True)
    print('Data have been concatenated successfully.')
    return df
