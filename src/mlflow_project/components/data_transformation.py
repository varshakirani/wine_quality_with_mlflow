import os
import pandas as pd

from sklearn.model_selection import train_test_split
from mlflow_project import logger
from mlflow_project.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: You can add different data transformation techniques such as Scaler, PCA etc
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model
    # Since this data is already clean, this notebook does only train_test splitting

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # split the data into train and test sets. (0.75, 0.25) split
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data is splitted into train and test sets")
        logger.info(f"train set contains: {train.shape}")
        logger.info(f"test set contains: {test.shape}")

        print(train.shape)
        print(test.shape)