#! /usr/bin/python
# -*- coding: utf-8 -*-

""" This file is a part of an application named enc-genetic-codes
    If you have any questions and/or comments, don't hesitate to 
    contact me by email wojciech.galan@gmail.com
    
    Copyright (C) 2015  Wojciech Gałan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>"""

#todo nazwa do poprawy

import argparse
import os

from sklearn.externals import joblib

import constants

from libs import sequence_processing

def classify(seq, nuc_acid, scaller, classifier):
    """
    Classify viral sequence
    :param seq: - sequence in upperrcase. Can contain degenerate nucleotides in IUPAC notation
    :param nuc_acid: either 'dna' or 'rna'
    :param scaller: trained scaller
    :param classifier: trained classifier
    :return:
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
    vals = [acid_code, length]
    vals.extend([freqs[k] for k in sorted(freqs)])
    vals = scaller.transform(vals)
    return classifier.predict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='') #todo dodać opis
    parser.add_argument('classifier', type=str, help='classifier: SVM, kNN or QDA')
    args = parser.parse_args()
    if not (args.classifier.lower() == 'svm' or args.classifier.lower() == 'knn' or args.classifier.lower() == 'qda'):
        raise ValueError("Classifier should be SVM, kNN or QDA")
    classify('AGATA', 'dna', None, None)
    classifier = joblib.load(os.path.join())

