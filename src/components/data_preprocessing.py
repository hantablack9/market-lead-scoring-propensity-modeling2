import os
import sys

sys.path.append("..")
from dataclasses import dataclass

import pandas as pd
from pandas import DataFrame

from src.components.config import DataPreprocessingConfig

@dataclass
class DataPreprocessor:
    config: DataPreprocessingConfig

    def load_data(self) -> pd.DataFrame:
        """
        Loads the raw CSV from config.path.
        """
        if not os.path.exists(self.config.path):
            raise FileNotFoundError(f"[ERROR] File not found: {self.config.path}")  # noqa: TRY003
        return pd.read_csv(self.config.path, low_memory=False)

    def change_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardizes and renames columns for consistency.
        """
        df.columns = (
            df.columns.str.lower()
            .str.replace("-", " ")
            .str.replace(" ", "_")
            .str.replace("__", "_")
            .str.replace("/", "_by_")
            .str.replace("(", "")
            .str.replace(")", "")
            .str.replace("-", "")
            .str.replace(".1", "")
        )

        rename_map = {
            "year": "opp_year",
            "month": "opp_month",
            "month_name": "opp_month_name",
            "week_of_year": "opp_week_of_year",
            "week_of_month": "opp_week_of_month",
            "day_of_year": "opp_day_of_year",
            "day_of_week": "opp_day_of_week",
            "day_name": "opp_day_name",
            "hour": "opp_hour",
        }
        df = df.rename(columns=rename_map)
        return df

    def data_cleaning(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the DataFrame by removing duplicates and
         transforming preliminary feature data types.
        """
        df = df.drop_duplicates()
        # Change temporal features to a pandas datetime format
        datetme = [
            "opportunity_created_date",
            "laststagechangedate",
            "lastactivitydate",
            "program_start_date_c",
            "program_end_date_c",
            "sales_end_",
            "sales_start_date",
        ]
        for feature in datetme:
            df[feature] = pd.to_datetime(df[feature], dayfirst=True, infer_datetime_format=True)
        return df
    def encode_target(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Encodes the target variable 'lead_status' into binary format.
        """
        # Sales team's leystone metric for success is the conversion of customer status
        # from "Engaged" to "Applications"
        # I will create a new target column based on this conversion
        target = "funnel_category"
        target_replace_dict = {
            "Wasted_leads": "0",
            "Engaged": "1",
            "Payment Initiated": "2",
            "Applications": "2",
            "Enrolled": "2"
        }
        df["target_sales"] = df[target].replace(target_replace_dict)
        df = df.drop(columns=[target])
        return df
    def save(self, df: pd.DataFrame) -> str:
        """
        Saves the cleaned dataframe to the configured output directory with optional versioning.
        """
        if not os.path.exists(self.config.extract_to):
            os.makedirs(self.config.extract_to)

        output_path = os.path.join(self.config.extract_to, self.config.output_filename)

        if not self.config.auto_rename and os.path.exists(output_path):
            raise FileExistsError(f"[ERROR] Output file already exists: {output_path}")

        # Handle auto versioning
        if self.config.auto_rename:
            base, ext = os.path.splitext(self.config.output_filename)
            count = 1
            while os.path.exists(output_path):
                output_path = os.path.join(self.config.extract_to, f"{base}_{count}{ext}")
                count += 1

        df.to_csv(output_path, index=False)
        print(f"[INFO] Preprocessed data saved to: {output_path}")
        return output_path


if __name__ == "__main__":
    config = DataPreprocessingConfig()
    processor = DataPreprocessor(config)

    raw_df = processor.load_data()
    clean_df = processor.change_column_names(raw_df)
    processor.save(clean_df)

    print(f"[INFO] Preprocessing complete: {clean_df.shape[0]} rows, {clean_df.shape[1]} columns.")
