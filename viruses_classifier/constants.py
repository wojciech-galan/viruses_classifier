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

# todo zmienić nazwę


import os
import json

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CONFIG = json.load(open(os.path.join(DIR_PATH, 'conf.json')))
ACID_TO_NUMBER = {'dna':1.0, 'rna':0.0}
