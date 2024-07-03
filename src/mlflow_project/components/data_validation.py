import os
import pandas as pd
from mlflow_project import logger
from mlflow_project.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema

            # check if all columns match the schema
            if set(all_cols)!=set(all_schema.keys()):
                validation_status = False
            else:
                # check if all datatypes match
                for col, expected_dtype in all_schema.items():
                    actual_dtype = data[col].dtype.name
                    if actual_dtype != expected_dtype:
                        validation_status = False
                        break
                    
                validation_status = True

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}")

        except Exception as e:
            raise e