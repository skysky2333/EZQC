from setuptools import setup, find_packages

setup(
    name='ezqc',
    version='0.1',
    author='Tinger Shi & Sky Li',
    description='EZQC is a streamlined, terminal-based alternative to FastQC. Instead of generating individual report files per analysis, EZQC displays the analysis results, reasons, and suggestions directly in the terminal, making it easier to quickly assess the quality of multiple files. Additionally, EZQC generates figures for each analysis, providing a visual aid to spot potential issues for further examination.',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        'numpy',
        'matplotlib',
        'pandas',
        'scipy',
        'Bio',
    ],
    entry_points={
        'console_scripts': [
            'ezqc=ezqc.ezqc:main',
        ],
    },
)
