#responsible for creating ml application as a package that can be installed and used
#find_packages auto find all ml appln in the dir we have created
from setuptools import find_packages,setup 
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List(str):
    '''
    This function will return the list of requirements.
    Next open the file requirements.txt and read each line by removing "\n" as shown below
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readLines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Uday',
    author_email='mhatre.uday@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')
)


'''
setup.py can be directly installed or when trying to install all reuirements.txt at that point
setup.py file should also run to build the package.For enabling that put -e . at the end of this file
which will auto trigger setup.py.

Secondly in get_requirements() when reading  -e . will also come, which should not be read 
'''
