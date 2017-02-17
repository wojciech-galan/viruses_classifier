#! /usr/bin/python
# -*- coding: utf-8 -*-

# todo zmienić nazwę


import os
import json

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG = json.load(open(os.path.join(DIR_PATH, 'conf.json')))
ACID_TO_NUMBER = {'dna':1.0, 'rna':0.0}
feature_indices = json.load(open(os.path.join(DIR_PATH, 'files', 'features.json'))) #TODO zrobić rzeczywiste indeksy, a nie
# to, co teraz np.array([features.index(feat) for feat in feats])