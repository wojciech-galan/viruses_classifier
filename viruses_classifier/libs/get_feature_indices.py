#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def _get_feature_indices(all_features, specific_features):
    return np.array([all_features.index(feat) for feat in specific_features])
