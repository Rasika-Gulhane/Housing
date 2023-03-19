from setuptools import setup, find_packages
from typing import List

#Declairing variables for setup function


PROJECT_NAME = "HOUSE PRICE PREDDICTION"
VERSION ='0.0.1'
AUTHOR= "Rasika Gulhane"
DESCRIPTION = "This is House Price Prediction ML project "
PACKAGES = ['housing']
REQUIREMNETS_FILE_NAME = 'requirements.txt'

HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """ 
    This function is going to return list of 
    requirements mentioned in requirements.txt file
    return this function going to return llist which contain name of 
    libraries mention in requirement.txt file
    """
    with open(REQUIREMNETS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    
    

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requirements = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())















