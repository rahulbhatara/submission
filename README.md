# Air Quality Analysis Project: Tiantan Station

## Live Dashboard
https://rahulbhatara.streamlit.app/

## Project Overview
By analyzing ozone level data recorded at the Tiantan station, this project investigates how temperature fluctuations influence ozone concentrations in the atmosphere. Examining trends, seasonal variations, and the interplay between temperature and ozone formation, this tool aims to provide valuable insights for environmental monitoring, air quality forecasting, and public health initiatives.

## Libraries Used
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- NumPy
- SciPy
- Statsmodels

## How to Run the Dashboard

To run the Air Quality Analysis Dashboard, follow these steps:

### Setup Environment

1. **Create and Activate a Python Environment**:
   - If using Conda (ensure [Conda](https://docs.conda.io/en/latest/) is installed):
     ```
     conda create --name airquality-ds python=3.9
     conda activate airquality-ds
     ```
   - If using venv (standard Python environment tool):
     ```
     python -m venv airquality-ds
     source airquality-ds/bin/activate  # On Windows use `airquality-ds\Scripts\activate`
     ```

2. **Install Required Packages**:
   - The following packages are necessary for running the analysis and the dashboard:
     ```
     pip install pandas numpy scipy matplotlib seaborn streamlit statsmodels
     ```

     or you can do
     ```
     pip install -r requirements.txt
     ```
### Run the Streamlit App

1. **Navigate to the Project Directory** where `dashboard.py` is located.

2. **Run the Streamlit App**:
    ```
    streamlit run dashboard.py
    ```

## About Me
- **Name**: Mhd. Rahul Bhatara Guru
- **Email Address**: rahulbhataraguru@gmail.com
- **Dicoding ID**: [maliki_borneo](https://www.dicoding.com/users/rahul_bhatara/)
