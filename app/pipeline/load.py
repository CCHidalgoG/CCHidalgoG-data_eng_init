import pandas as pd
import os
import glob
from pipeline.transform import union_df

def load_data(data: pd.DataFrame, output_path: str, file_name: str) -> str:
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    data.to_excel(output_path + file_name, index=False)
    return f"Sucessfully saved the file at {output_path + file_name}"
