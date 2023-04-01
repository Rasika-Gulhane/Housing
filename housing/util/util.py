import sys
sys.path.append("/Users/rasikagulhane/Housing/housing")

import yaml
from exception import HousingException
import os




# Read Yaml file in form of dictionarty every time we call it

def read_yaml_file(file_path:str)-> dict:
    try:

        Config_Info=None
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    
    except Exception as e:
        raise HousingException(e, sys) from e
