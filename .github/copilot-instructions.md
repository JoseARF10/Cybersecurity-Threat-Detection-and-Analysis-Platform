# GitHub Copilot Instructions

## Project Overview

**Cybersecurity Threat Detection and Analysis Platform** - A machine learning system that analyzes network traffic and security event data to detect and classify cybersecurity threats (DDoS, Botnet, Bruteforce, etc.).

## Architecture Overview

The project follows a three-tier architecture:

1. **Data Layer** (`data/` directory)
   - Raw CSV files for each threat type: Benign, Botnet, Bruteforce, DDoS, DoS, Infiltration, Portscan, WebAttacks
   - Combined dataset generated in `data/csv_files/combined_dataset.csv`
   - Parquet files automatically organized to `data/parquet_files/` for optimization

2. **Processing & Analysis Layer** (Planned `src/` and `notebooks/`)
   - `notebooks/01_data_exploration.ipynb` - Initial exploratory data analysis
   - Data loading pattern: Multi-file CSV aggregation using `pathlib` and `pandas.concat()`
   - Combines datasets from multiple threat types into single DataFrame

3. **Model & Serving Layer** (`models/` and `api/`)
   - Trained models stored as pickled objects (joblib format)
   - Flask API (`api/`) for serving threat detection predictions

## Critical Data Processing Workflow

The primary workflow (in `main.py` and notebook):

```python
# 1. Locate all CSV files using pathlib.glob()
data_directory = Path.cwd().parent / "data"
CSV_FILE_PATHS = list(data_directory.glob('*.csv'))

# 2. Load each file with low_memory=False (important for large mixed-type datasets)
df = pd.read_csv(file_path, low_memory=False)

# 3. Concatenate with ignore_index=True to reset row indices
combined_df = pd.concat(data_Frames, ignore_index=True)

# 4. Save to csv_files/ subfolder
combined_df.to_csv(data_directory / "combined_dataset.csv", index=False)
```

**Key Pattern**: Always use `low_memory=False` when reading CSV files to avoid dtype inference issues with heterogeneous data.

## File Organization Conventions

- **Raw data**: `data/*.csv` (individual threat-type datasets)
- **Processed data**: `data/csv_files/combined_dataset.csv` (aggregated training data)
- **Archive**: Parquet files auto-moved to `data/parquet_files/`
- **Notebooks**: Sequential naming (`01_`, `02_`, etc.) for analysis progression
- **Models**: joblib-serialized sklearn models in `models/`

## Development Workflow

1. **Environment Setup**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **Data Preparation**: Run `main.py` to aggregate CSV files into combined dataset

3. **Exploration**: Execute notebooks in sequence (`01_data_exploration.ipynb` → future notebooks)

4. **Model Development**: Build ML pipelines in notebooks, save models with joblib

5. **Serving**: Deploy via Flask API in `api/` folder

## Technology Stack

- **Data Processing**: pandas (>=1.3.0), numpy (>=1.21.0)
- **ML Framework**: scikit-learn (>=0.24.0) - primary ML library
- **Visualization**: matplotlib, seaborn
- **Model Serialization**: joblib
- **Web Framework**: Flask (>=2.0.0) for threat detection API
- **Notebooks**: Jupyter/JupyterLab for interactive development
- **Environment**: python-dotenv for configuration

## Important Implementation Patterns

### Path Handling
- Use `pathlib.Path` for cross-platform compatibility (Windows/Unix)
- Always use `Path.glob()` for file discovery, not `os.listdir()`
- Example: `Path.cwd().parent / "data"` for parent directory access

### Data Loading
- Specify `low_memory=False` parameter when reading mixed-type CSVs
- Use `ignore_index=True` when concatenating multiple dataframes to avoid index conflicts
- Always verify combined shape after concatenation: `print(combined_df.shape)`

### Directory Structure Creation
- Use `Path.mkdir(parents=True, exist_ok=True)` for safe directory creation
- Example from main.py: preparing `data/csv_files/` and `data/parquet_files/`

## Threat Classification Context

Dataset contains 8 threat types (and benign traffic):
- **DDoS/DoS**: Denial-of-Service attacks
- **Botnet**: Compromised machine networks
- **Bruteforce**: Credential attack attempts
- **Infiltration**: Unauthorized network access
- **Portscan**: Network reconnaissance
- **WebAttacks**: HTTP-layer attacks
- **Benign**: Normal traffic baseline

This is a **multi-class classification problem** with imbalanced classes (benign typically dominates).

## Notebook Execution Notes

- `01_data_exploration.ipynb`: Loads combined dataset, displays shape and first rows
- All cells use pandas DataFrames as primary data structure
- No cells have been executed yet (setup phase)
- Future notebooks should build incrementally: EDA → preprocessing → feature engineering → model training

## Common Tasks for AI Agents

1. **Add new analysis notebook**: Follow naming convention (`02_preprocessing.ipynb`, `03_feature_engineering.ipynb`)
2. **Expand model pipeline**: Save trained models as `models/threat_classifier_v1.pkl` with joblib
3. **Build API endpoint**: Add Flask routes in `api/` that load saved models and return predictions
4. **Debug data issues**: Always check combined dataset shape and sample rows first (`print(combined_df.head())`)

## Windows-Specific Considerations

Project runs on Windows (PowerShell activation). Ensure:
- Path separators handled by pathlib (not hardcoded `/` or `\`)
- Virtual environment activation uses `.venv\Scripts\Activate.ps1`
- CSV file handling accounts for Windows line endings (pandas handles automatically with `engine='python'` if needed)
