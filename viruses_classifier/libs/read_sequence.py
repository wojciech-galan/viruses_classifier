#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Routines for reading nucleotide sequences in different formats"""

import re
import os

RE_NA_IUPAC = '[ACGTRYSWKMBDHVN]*'


class ReadSequenceException(IOError):

    def __init__(self, message="Make sure your file contains either \
raw or FASTA-formatted sequence"):
        super(ReadSequenceException, self).__init__(message)

def read_sequence(path):
    """
    Reads a sequence file
    :param path: path to the file
    :return: sequence string
    """
    txt = open(path).read().strip()
    if txt.startswith('>'):
        return read_fasta(txt)
    return read_raw(txt)

def is_nucleotide_sequence(txt):
    """
    Checks whether txt is nucleotide sequence
    :param txt: should be raw string in uppercase without whitespases
    :return:
    """
    found = re.search(RE_NA_IUPAC, txt)
    return found.start()==0 and found.end()==len(txt)

def read_raw(txt):
    """
    Reads file containing raw sequence
    :param txt: content of the sequence file
    :return: sequence string
    """
    txt_without_whitespaces = ''.join(txt.split()).upper()
    if not is_nucleotide_sequence(txt_without_whitespaces):
        raise ReadSequenceException("Is it really single nucleotide sequence in one of the supported formats?")
    return txt_without_whitespaces


def read_fasta(txt):
    """
    Reads file cotaining FASTA-formatted sequence
    :param txt: content of the sequence file
    :return: raw sequence string
    """
    seqs = {}
    if txt.count('>') != 1 or txt[0] != '>':
        raise ReadSequenceException()
    txt_without_whitespaces = ''.join(txt.split(os.linesep)[1:]).upper()
    if not is_nucleotide_sequence(txt_without_whitespaces):
        raise ReadSequenceException("Is it really single nucleotide sequence in one of the supported formats?")
    return txt_without_whitespaces