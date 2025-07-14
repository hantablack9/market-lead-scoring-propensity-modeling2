from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    path: str = "./compressed/dataset.rar"  # Can be .rar or .csv
    extract_to: str = "./src/data"
    output_filename: str = "dataset.csv"
    auto_rename: bool = True


@dataclass
class DataPreprocessingConfig:
    path: str = "./src/data/dataset.csv"
    extract_to: str = "./src/data/preprocessed"
    output_filename: str = "clean_data.csv"
    auto_rename: bool = True


@dataclass
class DataTransformationConfig:
    path: str = "./src/data/preprocessed/clean_data.csv"
    extract_to: str = "./src/data/transformed"
    output_filename: str = "transformed_data.csv"
    auto_rename: bool = True


@dataclass
class ModelTrainingConfig:
    data
    model_path: str = "./src/models"
    model_filename: str = "trained_model.pkl"
    auto_rename: bool = True
    test_size: float = 0.2
    random_state: int = 42
