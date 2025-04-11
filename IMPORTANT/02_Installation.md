# Installation Guide

This document provides detailed instructions for setting up the Heart Health Lifestyle Recommendation Engine on your system.

## System Requirements

- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- 500MB free disk space
- Internet connection (for initial package download)

## Installation Steps

### 1. Clone or Download the Repository

If you're using Git:

```bash
git clone <repository-url>
cd heart-disease-AI-system
```

Alternatively, download and extract the ZIP file from the repository.

### 2. Create a Virtual Environment

Creating a virtual environment is highly recommended to avoid conflicts with other Python packages.

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

All required packages are specified in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

This will install the following key dependencies:
- pandas (2.2.0): For data manipulation
- numpy (1.26.3): For numerical operations
- scikit-learn (1.4.0): For machine learning capabilities
- streamlit (1.31.0): For the web interface
- plotly (5.18.0): For data visualization
- python-dotenv (1.0.0): For environment variable management

### 4. Verify Dataset

Ensure the heart disease dataset file (`heart-disease-risk-dataset-sample.csv`) is located in the root directory of the project. This file should be tab-separated and contain the required columns for the system to function properly.

### 5. Launch the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

This will start the web server and provide a local URL (typically http://localhost:8501) which you can open in your web browser to access the application.

## Troubleshooting

### Common Issues:

1. **Missing Dependencies**: If you encounter errors about missing modules, ensure you've activated the virtual environment and run the pip install command.

2. **Dataset Not Found**: Verify that the CSV file is in the correct location and has the expected format (tab-separated values).

3. **Port Already in Use**: If port 8501 is already in use, Streamlit will attempt to use another port. Check the terminal output for the correct URL.

4. **Version Conflicts**: If you experience issues with package versions, try creating a fresh virtual environment and installing the exact versions specified in requirements.txt.

### Getting Help

If you continue to experience issues with installation, please check:
- The project's issue tracker on GitHub
- Streamlit's documentation at https://docs.streamlit.io/
- Python virtual environment documentation 