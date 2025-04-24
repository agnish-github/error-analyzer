from setuptools import setup, find_packages

setup(
    name='error-analyzer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'error-helper=error_analyzer.main:main'
        ]
    },
    author='Agnish Choudhury',
    description='Runtime error analyzer using ChatGPT',
)
