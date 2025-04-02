from setuptools import setup, find_packages 

with open('requirements.txt','r') as f:
    install_requires=f.read().splitlines()
    
    setup(name='crop_recommendation_model',
        version='1.0.0',
        description='This is a crop recommendation model for crops based on weather data',
        author='Sai Mehtre',
        author_email='mrsolo0318@gmail.com')