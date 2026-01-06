# Cybersecurity Threat Detection and Analysis Platform

A machine learning-based platform for detecting and analyzing cybersecurity threats.

## Project Structure

- **data/** - Downloaded CSV datasets
- **notebooks/** - Jupyter notebooks for exploration and analysis
- **src/** - Python scripts for data processing and model training
- **models/** - Saved trained models
- **api/** - Flask application for serving predictions
- **requirements.txt** - Project dependencies

## Getting Started

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. Download and place your CSV data files in the `data/` directory

3. Start exploring with Jupyter notebooks in the `notebooks/` directory

## License

Your license here

## Dataset download instructions

The repository does not include raw datasets (they are large and excluded by `.gitignore`). Place the dataset CSVs and parquet files into the local `data/` folder before running the notebooks or `main.py`.

Options to host and download the datasets:

- Upload files to cloud storage (recommended): S3, Azure Blob, Google Drive, Dropbox. Then download to the project root and extract into `data/`.

- Example: download with `curl` or `wget` (Linux/macOS or WSL):

```bash
mkdir -p data
cd data
curl -O https://example.com/path/to/Benign-Monday-no-metadata.csv
curl -O https://example.com/path/to/Botnet-Friday-no-metadata.csv
cd ..
```

- Example: download from Google Drive using `gdown` (install with `pip install gdown`):

```bash
pip install gdown
mkdir -p data
gdown --folder https://drive.google.com/drive/folders/<FOLDER_ID> -O data/
```

- Example: download from S3 using AWS CLI:

```bash
aws s3 cp s3://my-bucket/dataset/ data/ --recursive
```

After downloading, verify files are present:

```powershell
ls data\*.csv
```

Then run the data preparation step or notebook:

```powershell
python main.py
# OR open notebooks/01_data_exploration.ipynb and run the cells
```

Notes:
- The repo `/.gitignore` excludes `data/` and large model files. Do not commit raw datasets to this repository.
- If you need dataset versioning, configure Git LFS and track the `data/` files, or store datasets in a dedicated data bucket and reference their URLs here.

