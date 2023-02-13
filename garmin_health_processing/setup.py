from setuptools import setup

setup(
    name='garmin_health_processing',
    version='0.2.0',
    author='Luca Cossu',
    author_email='cossu.luca@gmail.com',
    packages=['garmin_health_processing', 'garmin_health_processing.hrv', 'garmin_health_processing.utils',
              'garmin_health_processing.activity', 'garmin_health_processing.spo2',
              'garmin_health_processing.respiration'],
    scripts=['bin/pipeline.py'],
    # url='http://pypi.python.org/pypi/PackageName/',
    # license='LICENSE.txt',
    description='A package to preprocess data coming from Garmin Vivoactive 4 via web API',
    long_description=open('README.txt').read(),
    install_requires=[
        "matplotlib==3.5.2",
        "pandas==1.3.4",
        "pobm==1.1.1",
        "numpy==1.21.6",
        "hrv-analysis==1.0.4",
        "scipy==1.7.3",
        "antropy==0.1.4"
    ],
)
