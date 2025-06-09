import pandas as pd
import geopandas as gpd
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_CONFIG

Base = declarative_base()

class DatabaseLoader:
    def __init__(self):
        # Create SQLAlchemy engine
        connection_string = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
        self.engine = sa.create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
    
    def create_tables(self):
        """
        Create database tables for climate data
        """
        # Define SQLAlchemy models for different data types
        class WorldBankIndicator(Base):
            __tablename__ = 'world_bank_indicators'
            
            id = sa.Column(sa.Integer, primary_key=True)
            indicator = sa.Column(sa.String(100))
            year = sa.Column(sa.Integer)
            value = sa.Column(sa.Float)
        
        class SatelliteClimateData(Base):
            __tablename__ = 'satellite_climate_data'
            
            id = sa.Column(sa.Integer, primary_key=True)
            dataset = sa.Column(sa.String(100))
            latitude = sa.Column(sa.Float)
            longitude = sa.Column(sa.Float)
            temperature = sa.Column(sa.Float)
            precipitation = sa.Column(sa.Float)
        
        # Create all tables
        Base.metadata.create_all(self.engine)
    
    def load_worldbank_data(self, df: pd.DataFrame):
        """
        Load World Bank climate indicators to database
        
        Args:
            df (pd.DataFrame): Processed World Bank data
        """
        df.to_sql('world_bank_indicators', self.engine, if_exists='replace', index=False)
    
    def load_satellite_data(self, gdf: gpd.GeoDataFrame):
        """
        Load satellite climate data to database
        
        Args:
            gdf (gpd.GeoDataFrame): Processed satellite geospatial data
        """
        gdf.to_sql('satellite_climate_data', self.engine, if_exists='replace', index=False)