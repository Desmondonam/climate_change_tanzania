import pandas as pd
import geopandas as gpd
import numpy as np
from typing import Dict, List

class DataTransformer:
    @staticmethod
    def clean_worldbank_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean and preprocess World Bank climate indicator data
        
        Args:
            df (pd.DataFrame): Raw World Bank data
        
        Returns:
            pd.DataFrame: Cleaned and transformed data
        """
        # Drop rows with missing values
        df_cleaned = df.dropna(subset=['value'])
        
        # Convert data types
        df_cleaned['date'] = pd.to_datetime(df_cleaned['date'], format='%Y')
        df_cleaned['value'] = pd.to_numeric(df_cleaned['value'], errors='coerce')
        
        # Add additional derived columns
        df_cleaned['year'] = df_cleaned['date'].dt.year
        
        return df_cleaned
    
    @staticmethod
    def normalize_satellite_data(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Normalize and standardize satellite climate data
        
        Args:
            gdf (gpd.GeoDataFrame): Raw satellite geospatial data
        
        Returns:
            gpd.GeoDataFrame: Normalized geospatial data
        """
        # Clip data to Tanzania boundaries
        tanzania_crs = '+proj=aea +lat_1=-5 +lat_2=-15 +lat_0=-10 +lon_0=35 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs'
        gdf = gdf.to_crs(tanzania_crs)
        
        # Normalize numeric columns
        numeric_columns = gdf.select_dtypes(include=[np.number]).columns
        for col in numeric_columns:
            gdf[f'{col}_normalized'] = (gdf[col] - gdf[col].min()) / (gdf[col].max() - gdf[col].min())
        
        return gdf
    
    @staticmethod
    def aggregate_climate_datasets(datasets: Dict[str, pd.DataFrame]) -> pd.DataFrame:
        """
        Aggregate multiple climate datasets
        
        Args:
            datasets (Dict[str, pd.DataFrame]): Dictionary of climate datasets
        
        Returns:
            pd.DataFrame: Aggregated and merged climate data
        """
        merged_df = pd.DataFrame()
        
        for source, df in datasets.items():
            # Standardize column names
            df = df.rename(columns={
                'Year': 'year',
                'Temperature': 'temperature',
                'Precipitation': 'precipitation'
            })
            
            # Merge datasets
            if merged_df.empty:
                merged_df = df
            else:
                merged_df = pd.merge(merged_df, df, on='year', how='outer')
        
        return merged_df