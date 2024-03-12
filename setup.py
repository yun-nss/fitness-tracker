# setup.py

from setuptools import setup

setup(
    name='fitness-tracker',
    version='0.1',
    packages=['fitness_tracker'],
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'fitness-tracker=fitness_tracker.__main__:main'
        ]
    },
    author='Your Name',
    description='A fitness tracker package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/fitness-tracker',
)
