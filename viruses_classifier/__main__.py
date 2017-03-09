#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
import numpy as np
from sklearn.externals import joblib

import constants
from classifier import classify, seq_to_features
from libs import read_sequence


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='') #todo dodać opis
    parser.add_argument('sequence', type=str, help='sequence in plaintekst')
    parser.add_argument('--nucleic_acid', type=str, help='nucleic acid: either DNA or RNA',
                        choices=['DNA', 'RNA', 'dna', 'rna'])
    parser.add_argument('--classifier', type=str, help='classifier: SVC, kNN or QDA',
                        choices=['SVC','kNN', 'QDA', 'svc', 'knn', 'qda'])
    parser.add_argument('--ssRNAplus', '-s', dest='ssRNAplus', action='store_true')
    parser.add_argument('--probas', '-p', dest='probas', action='store_true')
    parsed_args = parser.parse_args(args)
    if parsed_args.ssRNAplus:
        classifier_name = analysis_type = 'ssRNA+'
        nucleic_acid = 'rna'
        feature_indices = np.linspace(0, 101, num=102, dtype=int) # no feature selection
    else:
        classifier_name = parsed_args.classifier.lower()
        nucleic_acid = parsed_args.nucleic_acid.lower()
        feature_indices = constants.feature_indices[parsed_args.classifier.lower()]
        analysis_type = 'all_viruses'
    # if not (parsed_args.classifier.lower() == 'svc' or parsed_args.classifier.lower() == 'knn' or
    #                 parsed_args.classifier.lower() == 'qda'):
    #     raise ValueError("Classifier should be SVC, kNN or QDA")
    # if not (parsed_args.nucleic_acid.lower() == 'dna' or parsed_args.nucleic_acid.lower() == 'rna'):
    #     raise ValueError("Nucleic acid tye should be either DNA or RNA")
    sequence = read_sequence.read_sequence(parsed_args.sequence)
    scaler = joblib.load(constants.scaler_path[analysis_type])
    classifier = joblib.load(constants.classifier_paths[classifier_name])
    seq_features = seq_to_features(sequence, nucleic_acid)
    print classify(seq_features, scaler, classifier,
                   feature_indices, parsed_args.probas, analysis_type)

    # TODO also classifiers trained on all available data


if __name__ == '__main__':
    main()
    # TODO poprawa konfiguracji,żeby działała pod windowsem