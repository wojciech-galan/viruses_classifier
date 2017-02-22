#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import argparse
from sklearn.externals import joblib

import constants
from classifier import classify


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='') #todo dodać opis
    parser.add_argument('sequence', type=str, help='sequence in plaintekst')
    parser.add_argument('nucleic_acid', type=str, help='nucleic acid: either DNA or RNA')
    parser.add_argument('classifier', type=str, help='classifier: SVM, kNN or QDA')
    parser.add_argument('--probas', '-p', dest='probas', action='store_true')
    parsed_args = parser.parse_args(args)
    if not (parsed_args.classifier.lower() == 'svm' or parsed_args.classifier.lower() == 'knn' or
                    parsed_args.classifier.lower() == 'qda'):
        raise ValueError("Classifier should be SVM, kNN or QDA")
    if not (parsed_args.nucleic_acid.lower() == 'dna' or parsed_args.nucleic_acid.lower() == 'rna'):
        raise ValueError("Nucleic acid tye should be either DNA or RNA")
    scaler_path = os.path.join(constants.DIR_PATH, constants.CONFIG['scaler_path'])
    classifier_path = os.path.join(constants.DIR_PATH,
                                  constants.CONFIG['classifier_paths'][parsed_args.classifier.lower()])
    scaler = joblib.load(scaler_path)
    classifier = joblib.load(classifier_path)
    print classify(parsed_args.sequence, parsed_args.nucleic_acid.lower(), scaler, classifier,
                   constants.feature_indices[parsed_args.classifier.lower()], parsed_args.probas)


if __name__ == '__main__':
    main()
    # TODO poprawa konfiguracji,żeby działała pod windowsem