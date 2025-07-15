import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.components.config import DataTransformationConfig

@dataclass
class DataTransformer:
    config: DataTransformationConfig
    def load_data(self) -> pd.DataFrame:
        pass