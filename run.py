import sys

sys.path.append('..')

from src.components.config import DataIngestionConfig
from src.components.data_ingestion import DataIngestor

def main() -> None:
    """
    Main function to run the data ingestion process.
    """
    config = DataIngestionConfig(
        path="./src/compressed/dataset.rar",      # or .csv
        extract_to="./src/data",
        output_filename="dataset.csv",
        auto_rename=True
    )
    ingestion = DataIngestor(config)
    df = ingestion.load_data()
    print("[INFO] Data loaded. Shape:", df.shape)

if __name__ == "__main__":
    main()
