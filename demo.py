import sys
sys.path.append('/Users/rasikagulhane/Desktop/Housing/housing')

from pipeline.pipeline import Pipeline
from exception import HousingException
from logger import logging
from config.configuration import Configuration
#from Housing.component.data_transformation import Datatr
import os

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # config_path = os.path.join("config","config.yaml")
        # pipeline = Pipeline(Configuartion(config_file_path=config_path))
        #pipeline.run_pipeline()
        # pipeline.start()
        # logging.info("main function execution completed.")
        # # data_validation_config = Configuartion().get_data_transformation_config()
        # # print(data_validation_config)
        # schema_file_path=r"D:\Project\machine_learning_project\config\schema.yaml"
        # file_path=r"D:\Project\machine_learning_project\housing\artifact\data_ingestion\2022-06-27-19-13-17\ingested_data\train\housing.csv"

        # df= DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)
        # data_validation_config = Configuration().get_data_validation_config()
        # print(data_validation_config)


    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()