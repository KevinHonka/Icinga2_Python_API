import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='icinga2',
    packages=['icinga2'],  # this must be the same as the name above
    package_data={'icinga2': ['*/*', '*']},
    include_package_data=True,
    version='0.4',
    description='An enhanced API to communicate with Icinga2',
    author='Kevin Honka',
    author_email='kevin.honka@astosch.de',
    url='https://github.com/KevinHonka/Icinga2_Python_API',  # use the URL to the github repo
    keywords=['Icinga2', 'API'],  # arbitrary keywords
    classifiers=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
