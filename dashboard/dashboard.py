import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Konfigurasi halaman
st.set_page_config(page_title="Air Quality from Tiantan Analysis by Rahul Bhatara", layout="wide")
st.title('Air Quality Analysis Dashboard: Tiantan Station')

# About section
st.markdown("""
### About Me
- **Name**: Mhd. Rahul Bhatara Guru
- **Email Address**: rahulbhataraguru@gmail.com
- **Dicoding ID**: [rahulbhatara](https://www.dicoding.com/users/rahulbhatara/)

### Project Overview
By analyzing ozone level data recorded at the Tiantan station, this project investigates how temperature fluctuations influence ozone concentrations in the atmosphere. Examining trends, seasonal variations, and the interplay between temperature and ozone formation, this tool aims to provide valuable insights for environmental monitoring, air quality forecasting, and public health initiatives.
""")

# Load data
@st.cache_data
def load_data():
    csv_files = [file for file in os.listdir('data/') if file.endswith('.csv')]
    dataframes = []
    for file in csv_files:
        file_path = os.path.join('data/', file)
        d = pd.read_csv(file_path)
        dataframes.append(d)    
    df = pd.concat(dataframes, ignore_index=True)
    
    # Cleaning data
    columns_numerik_to_fill = df.select_dtypes(include=['float64']).columns
    for col in columns_numerik_to_fill:
        df[col] = df[col].fillna(df[col].mean())
    columns_object = df.select_dtypes(include=['object']).columns
    for col in columns_object:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

df = load_data()

# Sidebar
st.sidebar.header('Dashboard Navigation')
page = st.sidebar.selectbox('Select Analysis:', ['Temperature Analysis', 'O3 Analysis', 'Correlation Analysis'])

if page == 'Temperature Analysis':
    st.header("Temperature Time Series Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Monthly Temperature Statistics
        st.subheader("Monthly Temperature Statistics")
        monthly_stats = df.groupby('month')['TEMP'].agg(['mean', 'std', 'min', 'max'])
        st.dataframe(monthly_stats)
        
        # Key insights
        st.info(f"""
        Key Insights:
        - Highest temperature month: {monthly_stats['mean'].idxmax()} (July)
        - Lowest temperature month: {monthly_stats['mean'].idxmin()} (January)
        - Month with highest temperature variation: {monthly_stats['std'].idxmax()} (March)
        """)
    
    with col2:
        # Monthly Temperature Box Plot
        st.subheader("Monthly Temperature Distribution")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=df, x='month', y='TEMP')
        plt.title('Temperature Distribution by Month')
        plt.xlabel('Month')
        plt.ylabel('Temperature (°C)')
        st.pyplot(fig)

elif page == 'O3 Analysis':
    st.header("Ozone (O3) Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # O3 Statistics
        st.subheader("O3 Basic Statistics")
        o3_stats = df['O3'].describe()
        st.dataframe(o3_stats)
        
        # Monthly O3 averages
        monthly_o3 = df.groupby('month')['O3'].mean()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=monthly_o3, markers=True)
        plt.title('Monthly O3 Averages')
        plt.xlabel('Month')
        plt.ylabel('O3 Concentration (ppb)')
        st.pyplot(fig)
    
    with col2:
        # O3 Distribution
        st.subheader("O3 Distribution")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=df, x='O3', kde=True)
        plt.title('O3 Concentration Distribution')
        plt.xlabel('O3 Concentration (ppb)')
        plt.ylabel('Frequency')
        st.pyplot(fig)

elif page == 'Correlation Analysis':
    st.header("Correlation Analysis")
    
    # Hanya pilih kolom numerik untuk analisis korelasi
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    numeric_df = df[numeric_columns]
    
    # Correlation matrix
    corr_matrix = numeric_df.corr()
    st.subheader("Correlation Matrix")
    st.dataframe(corr_matrix)
    
    # Heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True, fmt='.2f')
    plt.title('Correlation Heatmap of Numeric Variables')
    st.pyplot(fig)
    
    # Fokus pada korelasi TEMP dan O3
    st.subheader("Temperature and O3 Relationship")
    temp_o3_corr = corr_matrix.loc['TEMP', 'O3']
    st.info(f"""
    Key Insights:
    - Correlation coefficient between Temperature and O3: {temp_o3_corr:.3f}
    - This indicates a {abs(temp_o3_corr):.1%} {'positive' if temp_o3_corr > 0 else 'negative'} correlation
    - Interpretation: {'Strong' if abs(temp_o3_corr) > 0.7 else 'Moderate' if abs(temp_o3_corr) > 0.3 else 'Weak'} relationship
    """)
    
    # Scatter plot TEMP vs O3
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df, x='TEMP', y='O3', alpha=0.5)
    plt.title('Temperature vs O3 Concentration')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('O3 Concentration (ppb)')
    st.pyplot(fig)