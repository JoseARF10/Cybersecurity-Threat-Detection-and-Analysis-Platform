import pandas as pd
import os
import shutil
from pathlib import Path

        
 
def TransformData():
    # Define input and output file paths
    for filename in os.listdir('data/'):
        if filename.endswith('.parquet'):
            parquet_file = os.path.join('data/', filename)
            csv_output = os.path.join('data/', filename.replace('.parquet', '.csv'))

    # Read the parquet file into a pandas DataFrame
        df = pd.read_parquet(parquet_file)

    # Convert the DataFrame to a CSV file
        df.to_csv(csv_output, index=False)

        print(f"Successfully converted {parquet_file} to {csv_output}")

def sent_to_parquet_folder():
    source_folder = Path('data/')
    destination_folder = Path('data/parquet_files/')
    destination_folder.mkdir(parents=True, exist_ok=True)
    for file in source_folder.glob('*.parquet'):
        shutil.move(str(file), destination_folder / file.name)


def send_output_to_csv_folder():
    source_folder = Path('data/combined_dataset.csv')
    destination_folder = Path('data/csv_files/')
    destination_folder.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source_folder), destination_folder / source_folder.name)
    
send_output_to_csv_folder()