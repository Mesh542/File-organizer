import os
from pathlib import Path
import pandas as pd
import numpy as np

PATH = r'C:\Users\Mesh\Downloads'
sorted_files = {}

def group_files_by_type(files: list[str]):
    for file in files:
        file_name = 'no_extension' if Path(file).suffix[1: ].lower() == '' else Path(file).suffix[1: ].lower()
        if file_name not in sorted_files.keys():
            sorted_files[file_name] = [file]
        else:
            sorted_files[file_name].append(file)

def main():
    for root, dir, files in os.walk(PATH):
        group_files_by_type(files)

    # Determine the maximum length of the arrays
    max_length = max(len(arr) for arr in sorted_files.values())

    # Pad shorter arrays with NaN
    padded_data = {key: arr + [np.nan] * (max_length - len(arr)) for key, arr in sorted_files.items()}
    df = pd.DataFrame(padded_data)
    df.to_excel(f'{PATH}/downloads_files_data.xlsx')
    print('Exported.')

if __name__=='__main__':
    main()