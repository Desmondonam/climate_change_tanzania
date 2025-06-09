import logging
from config import LOGGING_CONFIG, DATA_SOURCES
from data_extraction import DataExtractor
from data_transformation import DataTransformer
from data_loading import DatabaseLoader

def setup_logging():
    """Set up logging configuration"""
    logging.basicConfig(
        filename=LOGGING_CONFIG['filename'],
        level=LOGGING_CONFIG['level'],
        format=LOGGING_CONFIG['format']
    )
    return logging.getLogger(__name__)

def main():
    # Setup logging
    logger = setup_logging()
    
    try:
        # Initialize components
        extractor = DataExtractor(logger)
        transformer = DataTransformer()
        loader = DatabaseLoader()
        
        # Create database tables
        loader.create_tables()
        
        # Extract World Bank indicators
        worldbank_indicators = []
        for indicator in DATA_SOURCES['worldbank']['indicators']:
            raw_data = extractor.extract_worldbank_data(indicator)
            cleaned_data = transformer.clean_worldbank_data(raw_data)
            worldbank_indicators.append(cleaned_data)
            loader.load_worldbank_data(cleaned_data)
        
        # Extract satellite datasets
        for dataset in DATA_SOURCES['nasa_giovanni']['datasets']:
            raw_satellite_data = extractor.extract_satellite_data(dataset)
            normalized_data = transformer.normalize_satellite_data(raw_satellite_data)
            loader.load_satellite_data(normalized_data)
        
        # Extract and aggregate climate research data
        climate_research_data = extractor.extract_climate_research_data()
        aggregated_data = transformer.aggregate_climate_datasets(climate_research_data)
        
        logger.info("Climate change data pipeline completed successfully")
    
    except Exception as e:
        logger.error(f"Error in climate data pipeline: {e}")

if __name__ == "__main__":
    main()