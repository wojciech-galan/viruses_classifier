#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

import constants
from libs import sequence_processing

def probas_to_dict(probas, translation_dict):
    """
    Transtorms vector of probabilities to dictionary {"type of virus":probability, ...}
    :param probas:
    :param translation_dict:
    :return:
    """
    return {translation_dict[i]:probas[i] for i in range(len(probas))}


def seq_to_features(seq, nuc_acid):
    """
    Transforms sequence to its features
    :param seq: nucleotide sequence
    :param nuc_acid: either dna or rna
    :return: list of sequence features(numbers)
    """
    acid_code = constants.ACID_TO_NUMBER[nuc_acid]
    length = len(seq)
    nuc_frequencies = sequence_processing.nucFrequencies(seq, 2)
    nuc_frequencies_ = {'nuc_frequencies__'+key : value for key, value in
                       nuc_frequencies.iteritems()}
    relative_nuc_frequencies_one_strand_ = {'relative_nuc_frequencies_one_strand__'+key : value for key, value in
                                           sequence_processing.relativeNucFrequencies(nuc_frequencies, 1).iteritems()}
    relative_trinuc_freqs_one_strand_ = {'relative_trinuc_freqs_one_strand__'+key : value for key, value in
                                        sequence_processing.thirdOrderBias(seq, 1).iteritems()}
    freqs = nuc_frequencies_
    freqs.update(relative_nuc_frequencies_one_strand_)
    freqs.update(relative_trinuc_freqs_one_strand_)
    vals = [length, acid_code]
    vals.extend([freqs[k] for k in sorted(freqs)])
    return vals


def classify(sequence_features, scaller, classifier, feature_indices=None, probas=False, analysis_type='all_viruses'):
    """
    Classify viral sequence
    :param sequence_features: (list of numbers) - features of the sequence to be classified
    :param scaller: trained scaller
    :param classifier: trained classifier
    :param feature_indices: indices of selected features
    :param probas: when True function returns class probabilities instead of class
    :return: class code (for example 0 or 1) or class probabilities
    """
    if feature_indices is not None:
        vals = scaller.transform(np.array(sequence_features).reshape(1, -1))[:, feature_indices]
    else:
        # no feature selection
        vals = scaller.transform(np.array(sequence_features).reshape(1, -1))
    if probas:
        clf_val = classifier.predict_proba(vals)[0]
        return probas_to_dict(clf_val, constants.NUM_TO_CLASS[analysis_type])
    return constants.NUM_TO_CLASS[analysis_type][classifier.predict(vals)[0]]
