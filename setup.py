from importlib.metadata import entry_points
from setuptools import setup, find_namespace_packages

setup(name='Bot_addressbook',
      version='0.0.1',
      description='Addressbook bot',
      url='https://github.com/gorandalex/Bot_addressbook',
      author='Andrii Horobets',
      author_email='andrii.gorobets@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points = {'console_scripts': ['bot-addressbook = Bot_addressbook.__main__:main']})