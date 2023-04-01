import sys
sys.path.append("/Users/rasikagulhane/Housing/housing")

from entity.config_entity import DataIntegrationConfig, DataValidationConfig, DataTransformationConfig, ModelEvaluationConfig, ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig
from util.util import read_yaml_file
from constant import *
from exception import HousingException
import logging

# print(CONFIG_FILE_PATH)


class Configuration:
    def __init__(self, config_file_path:str = '/Users/rasikagulhane/Housing/config/config.yaml', 
                 current_time_stamp:str = CURRENT_TIME_STAMP) -> None:
        self.config_info= read_yaml_file(file_path=config_file_path)
        self.training_pipeline_config= self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp

    def get_data_ingestion_config(self) -> DataIntegrationConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_madel_evaluation_config(self) -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        
        except Exception as e:
            raise HousingException(e,sys) from e


