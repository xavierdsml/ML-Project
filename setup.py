from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'

## function that return the list to the install_requires from the requirements.txt
def get_requirements(file_path:str)->List[str]:

  requirements = []
  with open (file_path) as file_obj:
    requirements = file_obj.readlines() # this will read the /n also so,
    requirements = [req.replace("\n", "")for req in requirements]

    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
  
  return requirements



setup(
  name = 'mlproject',
  version = '0.0.1',
  author = 'Tushar Gupta',
  author_email = 'guptaatusharr@gmail.com',
  packages = find_packages(),
  install_requries = get_requirements('requirements.txt')

)