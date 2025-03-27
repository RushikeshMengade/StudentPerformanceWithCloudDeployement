from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    packeges=[]
    with open(file_path) as files:
        file_name=files.readlines()
        packeges=[lines.replace("\n","") for lines in file_name]

        if "-e ." in  packeges:
            packeges.remove("-e .")
    return packeges
            
        

setup(
name='MachineLearning Project',
version='0.0.1' ,
author='Rushikesh mengade',
author_email='mengaderushikesh@gmail.com',
packages=find_packages (),
install_requires=get_requirements ('requirement.txt')
)


