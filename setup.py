from setuptools import setup, find_packages

setup(
    name='django-enhanced-cbv',
    version='0.1.dev',
    author='Ivan Raskovsky (rasca)',
    author_email='raskovsky@gmail.com',
    packages=find_packages(),
    license='BSD',
    description='generic class based views with enhanced functionallity',
    long_description=open('README.txt').read(),
)
