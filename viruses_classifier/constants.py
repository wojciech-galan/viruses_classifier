#! /usr/bin/python
# -*- coding: utf-8 -*-

# todo zmienić nazwę


import os
import json
import cPickle as pickle
from libs.get_feature_indices import _get_feature_indices

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG = json.load(open(os.path.join(DIR_PATH, 'conf.json')))
ACID_TO_NUMBER = {'dna':1.0, 'rna':0.0}
feature_indices = {
    'qda':_get_feature_indices(pickle.load(open(os.path.join(DIR_PATH, 'files', CONFIG['all_features_file']))),
                              json.load(open(os.path.join(DIR_PATH, 'files', CONFIG['features_file'])))['qda']),
    'knn':_get_feature_indices(pickle.load(open(os.path.join(DIR_PATH, 'files', CONFIG['all_features_file']))),
                              json.load(open(os.path.join(DIR_PATH, 'files', CONFIG['features_file'])))['knn'])
}
