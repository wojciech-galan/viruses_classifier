#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
from sklearn.externals import joblib

import constants
from classifier import classify, seq_to_features
from libs import read_sequence


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='') #todo dodać opis
    parser.add_argument('sequence', type=str, help='sequence in plaintekst')
    parser.add_argument('nucleic_acid', type=str, help='nucleic acid: either DNA or RNA')
    parser.add_argument('classifier', type=str, help='classifier: SVC, kNN or QDA')
    parser.add_argument('--probas', '-p', dest='probas', action='store_true')
    parsed_args = parser.parse_args(args)
    if not (parsed_args.classifier.lower() == 'svc' or parsed_args.classifier.lower() == 'knn' or
                    parsed_args.classifier.lower() == 'qda'):
        raise ValueError("Classifier should be SVC, kNN or QDA")
    if not (parsed_args.nucleic_acid.lower() == 'dna' or parsed_args.nucleic_acid.lower() == 'rna'):
        raise ValueError("Nucleic acid tye should be either DNA or RNA")
    sequence = read_sequence.read_raw(parsed_args.sequence)
    scaler = joblib.load(constants.scaler_path)
    classifier = joblib.load(constants.classifier_paths[parsed_args.classifier.lower()])
    seq_features = seq_to_features(sequence, parsed_args.nucleic_acid.lower())
    print classify(seq_features, scaler, classifier,
                   constants.feature_indices[parsed_args.classifier.lower()], parsed_args.probas)


if __name__ == '__main__':
    main()
    # TODO poprawa konfiguracji,żeby działała pod windowsem