import os, sys
sys.path.append('..')
from dataclasses import dataclass
import pandas as pd
from src.components.config import DataIngestionConfig
from src.utils.extractor import RarExtractor
from pandas import DataFrame

@dataclass
class DataIngestor:
    """
    Handles data extraction and loading into a DataFrame.
    """
    config: DataIngestionConfig

    def _extract_if_needed(self)->str:
        """
        If the file is a .rar archive, extract it and return the CSV path.
        Otherwise, return the configured CSV path.
        """
        if self.config.path.lower().endswith("rar"):
            print("[INFO] RAR archive detected - extracting...")
            extractor = RarExtractor(
                rar_path = self.config.path,
                extract_to = self.config.extract_to,
                output_filename = self.config.output_filename,
                auto_rename = self.config.auto_rename
            )
            return extractor.extract()
        return self.config.path
    def load_data(self) -> DataFrame:
        """
        Loads data into a pandas DataFrame after optional extraction.
        """
        file_path = self._extract_if_needed()
        print(f"[INFO] Loading data from {file_path}")
        df = pd.read_csv(file_path, low_memory=False)
        return df


# # import os
# # import pandas as pd
# # from dataclasses import dataclass

# # @dataclass
# # class DataIngestion:
# #     """
# #     This class handles the data ingestion process, including loading the dataset from a CSV file.
# #     """
# #     path: str
# #     def __init__(self, path: str = "./data/dataset.csv"):
# #         self.path = path




# # def load_data() -> pd.DataFrame:
# #     """
# #     Docstring:
# #     This method loads the dataset from the specified path and returns a pandas DataFrame.
# #     """
# #     df = pd.read_csv('./data/dataset.csv', low_memory=False)
# #     return df


# # if __name__ == "__main__":
# #     # Example usage of the module
# #     load_data()
# #     print("Data ingestion module loaded successfully.")


# # src/components/data_ingestion.py

# import pandas as pd
# from src.components.config import DataIngestionConfig
# from src.utils.extractor import RarExtractor

# class DataIngestion:
#     """
#     Handles data extraction and loading into a DataFrame.
#     """

#     def __init__(self, config: DataIngestionConfig):
#         self.config = config

#     def extract_if_needed(self) -> str:
#         """
#         If the file is a .rar archive, extract it and return the CSV path.
#         Otherwise, return the configured CSV path.
#         """
#         if self.config.path.lower().endswith(".rar"):
#             print("[INFO] RAR archive detected. Extracting...")
#             extractor = RarExtractor(
#                 rar_path=self.config.path,
#                 extract_to="./data",
#                 output_filename="dataset.csv",
#                 auto_rename=True
#             )
#             return extractor.extract()
#         else:
#             return self.config.path

#     def load_data(self) -> pd.DataFrame:
#         """
#         Loads data into a pandas DataFrame after optional extraction.
#         """
#         file_path = self.extract_if_needed()

#         print(f"[INFO] Loading data from {file_path}")
#         df = pd.read_csv(file_path, low_memory=False)
#         return df


# if __name__ == "__main__":
#     from src.components.config import DataIngestionConfig

#     # You can set this to a .rar or .csv
#     config = DataIngestionConfig(path="./compressed/dataset.rar")
#     ingestion = DataIngestion(config)
#     df = ingestion.load_data()
#     print("[INFO] Data loaded. Shape:", df.shape)
