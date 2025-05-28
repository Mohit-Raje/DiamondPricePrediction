from setuptools import find_packages , setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n"  , "") for req in requirements]
        return requirements
    
setup(
    name = "Diamond Price Prediction",
    version="0.0.1" , 
    author="Mohit Raje" ,
    author_email="mohitraje@xyz.com" ,
    install_requires=get_requirements('requirements.txt') ,
    packages=find_packages
)