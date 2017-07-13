.. -*- mode: rst -*-
viruses_classifier
====
Predicts host of a virus based on its (possibly complete) genomic sequence. Could be run in two modes:

- all_viruses (default) mode - predicts whether a virus infects Eukaryotes
- ssRNA+ mode - predicts whether a ssRNA+ virus infects Deuterostomia

Installation
------------

Dependencies
~~~~~~~~~~~~

viruses_classifier requires:

- Python = 2.7
- NumPy >= 1.6.1
- SciPy >= 0.9
- scikit-learn = 0.18.1


User installation
~~~~~~~~~~~~~~~~~

If you already have a working installation of numpy and scipy,
the easiest way to install viruses_classifier is using ``pip`` ::

    pip install -U git+https://github.com/wojciech-galan/viruses_classifier.git


Source code
-----------

You can check the latest sources with the command::

    git clone https://github.com/wojciech-galan/viruses_classifier


Usage
-----

all_viruses mode - you have to provide path to the sequence file, nucleic acid type and classifier name:

    viruses_classifier raw_or_FASTA-formatted_sequence_file --nucleic_acid rna --classifier qda --probas

ssRNA+ - you only have to provide path to the sequence file

    viruses_classifier raw_or_FASTA-formatted_sequence_file --ssRNAplus

In both cases you can provide optional argument --probas for class probabilities. This is a switch, so if you run the command with --probas you will obtain class probabilities and if you don't you will obtain only exact class. In all_viruses mode you can use one of three trained classifiers: SVC, kNN and QDA.

Citation
--------

# TODO
