import pytest
import os
import numpy as np
from ezqc.pbsq1 import run_pbsq1
from ezqc.psqs2 import run_psqs2
from ezqc.pbsc3 import run_pbsc3
from ezqc.psgc4 import run_psgc4
from ezqc.pbnc5 import run_pbnc5
from ezqc.sld6 import run_sld6
from ezqc.os7 import run_os7
from ezqc.ac8 import run_ac8

def parse_fastq_file(file_obj):
    while True:
        header = file_obj.readline().strip()
        if not header:
            break
        sequence = file_obj.readline().strip()
        file_obj.readline()
        quality_str = file_obj.readline().strip()
        yield header, sequence, quality_str

headers = []
sequences = []
quality_strings = []

with open("tests/SRR020192.fastq", 'r') as fastq_file:
     for header, sequence, quality_str in parse_fastq_file(fastq_file):
        headers.append(header)
        sequences.append(sequence)
        quality_strings.append(quality_str)

def test1_function1_FALSE():
    assert run_pbsq1(quality_strings) == False
def test1_function2_TRUE():
    assert run_psqs2(quality_strings) == True
def test1_function3_FALSE():
    assert run_pbsc3(sequences) == False
def test1_function4_FALSE():
    assert run_psgc4(sequences) == False
def test1_function5_FALSE():
    assert run_pbnc5(sequences) == False
def test1_function6_FALSE():
    assert run_sld6(sequences) == False
def test1_function7_FALSE():
    assert run_os7(sequences) == False
def test1_function8_TURE():
    assert run_ac8(sequences) == True

# # test 2
# with open("tests/SRR24755455.fastq", 'r') as fastq_file:
#      for header, sequence, quality_str in parse_fastq_file(fastq_file):
#         headers.append(header)
#         sequences.append(sequence)
#         quality_strings.append(quality_str)

# def test2_function1_FALSE():
#     pnp = run_pbsq1(quality_strings)
#     assert pnp == False
# def test2_function2_TRUE():
#     pnp2 = run_psqs2(quality_strings)
#     assert pnp2 == True
# def test2_function3_FALSE():
#     pnp3 = run_pbsc3(sequences)
#     assert run_pbsc3(sequences) == False
# def test2_function4_FALSE():
#     pnp4 = run_psgc4(sequences)
#     assert pnp4 == False
# def test2_function5_FALSE():
#     pnp5 = run_pbnc5(sequences)
#     assert pnp5 == False
# def test2_function6_FALSE():
#     pnp6 = run_sld6(sequences)
#     assert pnp6 == False
# def test2_function7_FALSE():
#     pnp7 = run_os7(sequences)
#     assert pnp7 == False
# def test2_function8_TURE():
#     pnp8 = run_ac8(sequences)
#     assert pnp8 == True