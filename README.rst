.. -*- mode: rst -*-
viruses_classifier
====
Predict host of a virus based on its (possibly complete) genomic sequence

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
the easiest way to install pbil is using ``pip`` ::

    pip install -U git+https://github.com/wojciech-galan/viruses_classifier.git


Source code
-----------

You can check the latest sources with the command::

    git clone https://github.com/wojciech-galan/viruses_classifier


Usage
-----

for example:

    viruses_classifier raw_or_FASTA-formatted_sequence_file dna svm


Citation
--------

# TODO