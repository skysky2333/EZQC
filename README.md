[![EZQC Main Tests](https://github.com/skysky2333/EZQC/actions/workflows/ezqc_main_test.yml/badge.svg)](https://github.com/skysky2333/EZQC/actions/workflows/ezqc_main_test.yml)
[![PyPI](https://img.shields.io/pypi/v/ezqc?color=blue)](https://pypi.org/project/ezqc/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)



# EZQC: Easy Quality Control for FastQ Files
<p align="center">
  <img src="tests/test1.gif" alt="test Gif" width="100%">
</p>

## Table of Contents
- [EZQC: Easy Quality Control for FastQ Files](#ezqc-easy-quality-control-for-fastq-files)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Why Choose EZQC VS FastQC?](#why-choose-ezqc-vs-fastqc)
  - [Quick Start Guide](#quick-start-guide)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Analysis Methods](#analysis-methods)
  - [Contributing](#contributing)

## Introduction

EZQC is a streamlined, terminal-based alternative to FastQC. Instead of generating individual report files per analysis, EZQC displays the analysis results, reasons, and suggestions directly in the terminal, making it easier to quickly assess the quality of multiple files. Additionally, EZQC generates figures for each analysis, providing a visual aid to spot potential issues for further examination.

EZQC is capable of performing the following analyses:

1. Per base sequence quality
2. Per sequence quality scores
3. Per base sequence content
4. Per sequence GC content
5. Per base N content
6. Sequence Length Distribution
7. Overrepresented sequences
8. Adapter Content

## Why Choose EZQC VS FastQC?

- **Fast Result Readout When Batch Processing**: With EZQC, there's no need to click into each HTML report like you would with FastQC.
- **Automatic Interpretation of Analysis Results**: The results are color-coded and provided in plain English, complete with suggestions. This makes it easier for users to interpret the results quickly.
- **Generate Detailed Figures for Advanced Users**: For those who want a more in-depth analysis, EZQC is capable of generating detailed figures that aid in understanding the quality of your FastQ files.

## Quick Start Guide

1. Install EZQC following [Installation guide](#installation).
2. Run the tool on a toy example using the command `ezqc tests/SRR020192.fastq` (fastq file from [IGSR](https://www.internationalgenome.org/data-portal/sample/NA18486)).
3. The results will be displayed in the terminal, and figures as well as csv tables will be saved to a directory named `ezqc_output` in your current working directory. Note that this file is choosen intentionally to fail multiple QC tests.

## Installation

You can install EZQC using pip:
```
pip install ezqc
```

Alternatively, you can compile the latest version of EZQC from source using the provided `setup.py` script. Following steps:

1. Clone the repository:

```
git clone https://github.com/skysky2333/ezqc
```

2. Navigate to the EZQC directory:

```
cd ezqc
```

3. Install the package:

```
pip install .
```

Or

```
python setup.py install
```

EZQC requires Python 3.x and depends on the following packages, which will be installed automatically during setup:

- numpy
- matplotlib
- pandas
- scipy
- Bio

## Usage

After installation, you can use EZQC from the command line as follows:

```
ezqc <fastq file(s)>
```

Replace `<fastq file(s)>` with the path(s) to your FastQ files. If you want to analyze multiple files, separate the file paths with spaces:

```
ezqc file1.fastq file2.fastq file3.fastq
```
Use `-o` or `--output` to set the output directory.
Use `-h` or `--help` to see help messages.

## Analysis Methods

Here's a brief description of the analyses performed by EZQC:

1. **Per Base Sequence Quality**: Checks the quality of each base call in a sequence read.
2. **Per Sequence Quality Scores**: Provides a histogram of quality scores over all sequences.
3. **Per Base Sequence Content**: Analyzes the proportion of each base (A, T, G, C) at each position across all sequences.
4. **Per Sequence GC Content**: Calculates the GC content in each sequence.
5. **Per Base N Content**: Identifies sequences with a high proportion of unknown (N) bases.
6. **Sequence Length Distribution**: Provides a histogram showing the distribution of sequence lengths.
7. **Overrepresented sequences**: Identifies any sequences that occur more often than expected.
8. **Adapter Content**: Detects the presence of adapter sequences in the reads.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute.