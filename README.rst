.. -*- mode: rst -*-
viruses_classifier
====
Predict host of a virus based on its (possibly complete) genomic sequence. Could be run in two modes:
- all_viruses (default) mode - predict whether a virus infects Eukaryotes
- ssRNA+ mode - predict whether a ssRNA+ virus infects Deuterostomia

Installation
------------

Dependencies
~~~~~~~~~~~~

viruses_classifier requires:

- Python >= 2.6
- NumPy >= 1.6.1
- scikit-learn >= 0.18


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

    viruses_classifier raw_or_FASTA-formatted_sequence_file dna svc

ssRNA+ - you only have to provide path to the sequence file

    viruses_classifier raw_or_FASTA-formatted_sequence_file --ssRNAplus

In both cases you can provide also optional algument --probas for class probabilities

Citation
--------

# TODO
