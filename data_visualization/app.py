import streamlit as st
import pandas as pd
import plotly.express as px
from data_storage.sql_database import fetch_from_sql

def load_data():
    """
    Loads data from the SQL database.
    """
    return fetch_from_sql("SELECT * FROM climate_data")

def main():
    st.title("Climate Change Dashboard - Tanzania")
    
    # Load data
    data = load_data()
    
    # Visualize temperature trends
    st.subheader("Temperature Trends")
    fig = px.line(data, x="date", y="temperature_c", color="location", title="Temperature Over Time")
    st.plotly_chart(fig)
    
    # Visualize CO2 levels
    st.subheader("CO2 Levels")
    fig = px.bar(data, x="location", y="co2_ppm", title="CO2 Levels by Location")
    st.plotly_chart(fig)
    
    # Visualize rainfall
    st.subheader("Rainfall Analysis")
    fig = px.scatter(data, x="date", y="rainfall_mm", color="location", title="Rainfall Over Time")
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()