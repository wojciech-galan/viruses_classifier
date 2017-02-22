#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Routines for reading nucleotide sequences in different formats"""


def read_raw(path):
    return ''.join(open(path).read().split()).upper()
