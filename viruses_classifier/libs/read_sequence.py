#! /usr/bin/python
# -*- coding: utf-8 -*-

import re

"""Routines for reading nucleotide sequences in different formats"""


class ReadSequenceException(IOError):

    def __init__(self, message=
    "Make sure your file contains either raw or FASTA-formatted sequence"):
        super(ReadSequenceException, self).__init__(message)


def read_raw(path):
    """
    Reads file containing raw sequence
    :param path: path to the file
    :return: sequence string
    """
    return ''.join(open(path).read().split()).upper()

