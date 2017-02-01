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
    parser.add_argument('--probas', action='store_true')
    args = parser.parse_args(args)
    if not (args.classifier.lower() == 'svm' or args.classifier.lower() == 'knn' or args.classifier.lower() == 'qda'):
        raise ValueError("Classifier should be SVM, kNN or QDA")
    if not (args.nucleic_acid.lower() == 'dna' or args.nucleic_acid.lower() == 'rna'):
        raise ValueError("Nucleic acid tye should be either DNA or RNA")
    classify('AGATA', 'dna', None, None)
    classifier = joblib.load(os.path.join())
    scaller = joblib.load()

if __name__ == '__main__':
    main()