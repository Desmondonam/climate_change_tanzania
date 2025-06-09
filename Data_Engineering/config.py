import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database Configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': 'tanzania_climate_change'
}

# Data Sources Configuration
DATA_SOURCES = {
    'worldbank': {
        'base_url': 'https://api.worldbank.org/v2/country/TZA',
        'indicators': [
            'EN.ATM.CO2E.KT',  # CO2 emissions
            'AG.LND.ARBL.HA',  # Arable land
            'ER.H2O.INTR.PC',  # Freshwater withdrawal
        ]
    },
    'nasa_giovanni': {
        'base_url': 'https://giovanni.gsfc.nasa.gov/giovanni/daac-bin/service',
        'datasets': [
            'precipitation',
            'temperature',
            'drought_index'
        ]
    },
    'climate_data_sources': [
        'https://crudata.uea.ac.uk/cru/data/hrg/',  # CRU Climate Research Unit
        'https://www.ipcca.org/tanzania-climate-data',
        'https://sedac.ciesin.columbia.edu/data/collection/tanzania-climate'
    ]
}

# Logging Configuration
LOGGING_CONFIG = {
    'filename': 'climate_data_pipeline.log',
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}