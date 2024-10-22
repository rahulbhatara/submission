# Air Quality Analysis Project: Tiantan Station

## Live Dashboard
https://rahuldicoding.streamlit.app/

## Project Overview
This project analyzes ozone level data recorded at the Tiantan station to investigate how temperature fluctuations influence ozone concentrations in the atmosphere. By examining trends, seasonal variations, and the interplay between temperature and ozone formation, this tool aims to provide valuable insights for environmental monitoring, air quality forecasting, and public health initiatives.

## Libraries Used
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- NumPy

## How to Run the Dashboard

To run the Air Quality Analysis Dashboard, follow these steps:

### Setup Environment

1. **Install Required Packages**:
   - The following packages are necessary for running the analysis and the dashboard:
     ```
     pip install pandas numpy matplotlib seaborn streamlit
     ```

     or you can do
     ```
     pip install -r requirements.txt
     ```

### Run the Streamlit App

1. **Navigate to the Project Directory** where `dashboard.py` is located.

2. **Run the Streamlit App**:
    ```
    streamlit run dashboard/dashboard.py
    ```

### Data Processing Steps
1. Data Collection: Automatically reads and combines multiple CSV files
2. Missing Data Treatment: 
- Numerical data: Filled with mean values
- Categorical data: Filled with mode values
3. Exploratory Data Analysis:
- Time series pattern analysis
- Correlation analysis
- Statistical summaries

## Visualizations Include
1. Missing Data Pattern Analysis
2. Time Series Analysis of Temperature
3. Monthly Temperature Statistics
4. Temperature-Ozone Correlation Analysis

## Conclusions
- Temperature shows clear seasonal patterns throughout the year
- There is a moderate positive correlation between temperature and ozone levels
- The relationship between temperature and ozone is consistent across different correlation measures

## About Me
- **Name**: Mhd. Rahul Bhatara Guru
- **Email Address**: rahulbhataraguru@gmail.com
- **Dicoding ID**: [rahulbhatara](https://www.dicoding.com/users/rahulbhatara)
