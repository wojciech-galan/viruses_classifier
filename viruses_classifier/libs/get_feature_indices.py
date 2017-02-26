#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def _get_feature_indices(all_features, specific_features):
    """
    Returns indices of some specific features in list containing all the features
    :param all_features:
    :param specific_features:
    :return:
    """
    return np.array([all_features.index(feat) for feat in specific_features])
