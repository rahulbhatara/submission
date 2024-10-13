import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from scipy.stats import f_oneway

st.set_page_config(page_title="Air Quality from Tiantan Analysis by Rahul Bhatara")
st.title('Air Quality Analysis Dashboard: Tiantan Station')

# Load data
csv_files = [file for file in os.listdir('data/') if file.endswith('.csv')]
dataframes = []
for file in csv_files:
    file_path = os.path.join('data/', file)
    d = pd.read_csv(file_path)
    dataframes.append(d)

df = pd.concat(dataframes, ignore_index=True)

# About me
st.markdown("""
### About Me
- **Name**: Mhd. Rahul Bhatara Guru
- **Email Address**: rahulbhataraguru@gmail.com
- **Dicoding ID**: [rahulbhatara](https://www.dicoding.com/users/rahulbhatara/)

### Project Overview
By analyzing ozone level data recorded at the Tiantan station, this project investigates how temperature fluctuations influence ozone concentrations in the atmosphere. Examining trends, seasonal variations, and the interplay between temperature and ozone formation, this tool aims to provide valuable insights for environmental monitoring, air quality forecasting, and public health initiatives.
""")

# Display data preview
st.subheader("Data Preview")
st.write(df.head())

# Display missing data pattern
st.subheader("Missing Data Pattern")
missing_percentage = df.isnull().mean() * 100
missing_percentage = missing_percentage[missing_percentage > 0]

if not missing_percentage.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    missing_percentage.plot(kind='bar', color='salmon', ax=ax)
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}%', (p.get_x() * 1.005, p.get_height() * 1.005), fontsize=12)
    ax.set_title('Missing Data Pattern')
    ax.set_xlabel('Column')
    ax.set_ylabel('Percentage of Missing Data (%)')
    st.pyplot(fig)
else:
    st.write("No missing data!")

# Data cleaning and handling missing values
df_fixed = df.copy()
columns_numerik_to_fill = df_fixed.select_dtypes(include=['float64']).columns
for col in columns_numerik_to_fill:
    df_fixed[col].fillna(df_fixed[col].mean(), inplace=True)
columns_object = df_fixed.select_dtypes(include=['object']).columns
for col in columns_object:
    df_fixed[col].fillna(df_fixed[col].mode()[0], inplace=True)

# Create time series data
df_fixed['date'] = pd.to_datetime(df_fixed[['year', 'month', 'day', 'hour']])
data_time_series = df_fixed[["date", "PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "DEWP", "RAIN", "WSPM"]].set_index('date').resample('W').mean()

# Display TEMP and O3 trends over time
st.subheader("Weekly Average TEMP and O3 Concentrations")
fig, ax = plt.subplots(figsize=(15, 6))
ax.plot(data_time_series.index, data_time_series['O3'], label='O3', color='green')
ax.plot(data_time_series.index, data_time_series['TEMP'], label='TEMP', color='yellow')
ax.set_title('Weekly Average TEMP and O3 Concentrations')
ax.set_xlabel('Date')
ax.set_ylabel('Concentration')
ax.legend()
st.pyplot(fig)

# Display correlation matrix
st.subheader("Correlation Matrix of Selected Parameters")
correlation_matrix = df_fixed[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].corr()
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
ax.set_title('Correlation Matrix of Selected Parameters', fontsize=16)
st.pyplot(fig)

# Display seasonal trends in temperature
st.subheader("Seasonal Trends: Average Temperature by Month")
seasonal_trends = df_fixed.groupby('month')['TEMP'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
seasonal_trends.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Average Temperature by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Average Temperature (°C)')
ax.set_xticks(range(0, 12))
ax.set_xticklabels([str(m) for m in range(1, 13)], rotation=0)
st.pyplot(fig)

# Display regression plot of TEMP vs O3
st.subheader("Scatter Plot of Weekly Average TEMP and O3 with Regression Line")
fig, ax = plt.subplots(figsize=(15, 6))
sns.regplot(x='TEMP', y='O3', data=data_time_series, scatter_kws={'alpha':0.5}, ax=ax)
ax.set_title('Scatter Plot of Weekly Average TEMP and O3 with Regression Line')
ax.set_xlabel('Temperature')
ax.set_ylabel('O3 Concentration')
st.pyplot(fig)