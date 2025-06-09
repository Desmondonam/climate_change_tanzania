import requests
import pandas as pd
import logging
from typing import Dict, List
import geopandas as gpd
import rasterio
from config import DATA_SOURCES

class DataExtractor:
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)
    
    def extract_worldbank_data(self, indicator: str, start_year: int = 1990, end_year: int = 2023) -> pd.DataFrame:
        """
        Extract World Bank climate indicators for Tanzania
        
        Args:
            indicator (str): World Bank indicator code
            start_year (int): Starting year for data extraction
            end_year (int): Ending year for data extraction
        
        Returns:
            pd.DataFrame: Extracted data
        """
        try:
            url = f"{DATA_SOURCES['worldbank']['base_url']}/indicator/{indicator}"
            params = {
                'date': f'{start_year}:{end_year}',
                'format': 'json'
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()[1]
            df = pd.DataFrame(data)
            df['indicator'] = indicator
            
            self.logger.info(f"Successfully extracted {indicator} data")
            return df
        except Exception as e:
            self.logger.error(f"Error extracting World Bank data: {e}")
            return pd.DataFrame()
    
    def extract_satellite_data(self, dataset: str) -> gpd.GeoDataFrame:
        """
        Extract satellite-based climate datasets for Tanzania
        
        Args:
            dataset (str): Type of satellite dataset
        
        Returns:
            gpd.GeoDataFrame: Geospatial climate data
        """
        # Placeholder for satellite data extraction
        # This would typically involve API calls or file downloads from NASA, ESA, etc.
        try:
            # Example with hypothetical data source
            base_url = f"https://giovanni.gsfc.nasa.gov/giovanni/daac-bin/service/{dataset}"
            
            # Geospatial bounds for Tanzania
            tanzania_bounds = {
                'min_lon': 29.3272,
                'max_lon': 40.4409,
                'min_lat': -11.7459,
                'max_lat': -0.9956
            }
            
            # Simulated download and processing
            gdf = gpd.read_file(base_url, bbox=tanzania_bounds)
            
            self.logger.info(f"Successfully extracted {dataset} satellite data")
            return gdf
        except Exception as e:
            self.logger.error(f"Error extracting satellite data: {e}")
            return gpd.GeoDataFrame()
    
    def extract_climate_research_data(self) -> Dict[str, pd.DataFrame]:
        """
        Extract climate research data from various sources
        
        Returns:
            Dict[str, pd.DataFrame]: Dictionary of climate datasets
        """
        datasets = {}
        
        # Example sources (you'd replace with actual data retrieval)
        sources = [
            'https://crudata.uea.ac.uk/cru/data/temperature/tanzaniadata.csv',
            'https://ipcca.org/tanzania-precipitation-data.csv'
        ]
        
        for source in sources:
            try:
                df = pd.read_csv(source)
                datasets[source] = df
                self.logger.info(f"Successfully extracted data from {source}")
            except Exception as e:
                self.logger.error(f"Error extracting data from {source}: {e}")
        
        return datasets