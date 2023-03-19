from setuptools import setup
from typing import List

#Declairing variables for setup function


PROJECT_NAME = "HOUSE PRICE PREDDICTION"
VERSION ='0.0.1'
AUTHOR= "Rasika Gulhane"
DESCRIPTION = "This is House Price Prediction ML project "
PACKAGES = ['housing']
REQUIREMNETS_FILE_NAME = 'requirements.txt'

def get_requirements_list() -> List[str]:
    """ 
    This function is going to return list of 
    requirements mentioned in requirements.txt file
    return this function going to return llist which contain name of 
    libraries mention in requirement.txt file
    """
    with open(REQUIREMNETS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = PACKAGES,
    install_requirements = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())
