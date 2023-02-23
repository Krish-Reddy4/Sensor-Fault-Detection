from setuptools import find_packages, setup

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:list[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="krishhg97@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)
