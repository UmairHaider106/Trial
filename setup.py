from setuptools import find_packages,setup

from typing import List


hypen="-e ."

def get_requirement(file_path:str)->list[str]:






    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[i.replace("\n","") for i in req]

        if hypen in req:
            req.remove(hypen)


    return req


setup(
    name="ML",
    version="0.0.1",
    packages=find_packages(),
    install_require=get_requirement("requirements.txt"),


)