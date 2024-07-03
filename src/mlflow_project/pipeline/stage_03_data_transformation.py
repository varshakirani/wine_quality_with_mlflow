from pathlib import Path

from mlflow_project import logger
from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.data_transformation import DataTransformation

STAGE_NAME = "Data Transformation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        try:
            with open(data_validation_config.STATUS_FILE, "r") as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            
            else:
                logger.exception("Your data schema is not valid")
                raise Exception("Your data schema is not valid")
            
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e