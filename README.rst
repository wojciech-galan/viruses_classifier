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

    pip install git+https://github.com/wojciech-galan/viruses_classifier.git


General issues
*************
kNN classifier may not work on 32-bit python, so stick to the 64-bit one. Also, all of the classifiers were trained with a distinct version of scikit-learn, and may not work for the newer/older ones.

Windows installation issues
*************

Under windows you may encounter problems with installing libraries for linear algebra required by scipy. The recommended solution is to install Anaconda which has a proper version of scikit-learn (for example Anaconda2-4.4.0). Then, in Anaconda console, run::

    conda install qt

and proceed with the above pip command.

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
