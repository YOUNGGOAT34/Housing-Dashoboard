# type: ignore
import numpy as np 
import pandas as pd 

import streamlit as st 
from plots import (
    longitude_latitude_distribution,
    generate_correlation_heatmap,
    pairwise_scatter_plots,
    numerical_attribute_histograms
    
)

st.set_page_config(page_title="Demographic Dashboard", page_icon=":bar_chart:", layout="wide")


@st.cache_data
def load_data():
    # Load the data using pandas
    df = pd.read_csv('housing.csv')
    mean_total_bedrooms = df['total_bedrooms'].mean()

    # Fill missing values with the mean
    df['total_bedrooms'].fillna(mean_total_bedrooms, inplace=True)
    return df

df = load_data()

# Sidebar for display options
display_option = st.sidebar.radio(
    "Display Option",
    (
        "Dataframe",
        "Statistics",
        "Correlation Heatmap",
        "Distribution of houses in longitude and latitude",
        "Pairwise Scatter Plots",
        "Numerical Attribute Histograms"
        
        
    )
)


# Display the selected option
if display_option == "Dataframe":
    st.dataframe(df)
elif display_option == "Statistics":
    st.write(df.describe())
elif display_option == "Correlation Heatmap":
    plt = generate_correlation_heatmap(df) 
    st.pyplot(plt)  # Display the correlation heatmap in Streamlit app

elif display_option=="Distribution of houses in longitude and latitude":
    plt=longitude_latitude_distribution(df)
    st.pyplot(plt) 

elif display_option=="Pairwise Scatter Plots":
    plt=pairwise_scatter_plots(df)
    st.pyplot(plt) 

elif display_option=="Numerical Attribute Histograms":
    plt=numerical_attribute_histograms(df)
    st.pyplot(plt) 

