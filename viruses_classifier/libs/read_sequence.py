#! /usr/bin/python
# -*- coding: utf-8 -*-

import re

"""Routines for reading nucleotide sequences in different formats"""


class ReadSequenceException(IOError):

    def __init__(self, message="Make sure your file contains either \
    raw or FASTA-formatted sequence"):
        super(ReadSequenceException, self).__init__(message)


def read_raw(path):
    """
    Reads file containing raw sequence
    :param path: path to the file
    :return: sequence string
    """
    return ''.join(open(path).read().split()).upper()


def read_fasta(path):
    """
    Reads file cotaining FASTA-formatted sequence
    :param path: path to the file
    :return: raw sequence string
    """
    seqs = {}
    text = open(path).read().strip()
    if text.count('>') != 1 or text[0] != '>':
        raise ReadSequenceException()
    seq = text.split('\n',1)[1]
    return ''.join(seq.split()).upper()