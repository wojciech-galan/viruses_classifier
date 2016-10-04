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

#todo nazwa do zmiany

NA_IUPAC = {'A':('A',), 'C':('C',), 'G':('G',), 'T':('T',),
            'R':('A','G'), 'Y':('C','T'), 'M':('A','C'), 'K':('G','T'),
            'S':('C','G'), 'W':('A','T'), 'B':('C','G','T'), 'D':('A','G','T'),
            'H':('A','C','T'), 'V':('A','C','G'), 'N':('A','C','G','T')}

def combinations (n, inlist, outlist=[]):
    '''Funkcja rekurencyjna ktora tworzy wszystkie mozliwe kombinacje
    danych znakow o okreslonej dlugosci
    - n - dlugosc
    - inlist - lista znakow
    - outlist - wynik'''
    if n==0:
        return outlist
    else:
        if outlist:
            new_outlist=[]
            for element in outlist:
                new_outlist.extend([element+x for x in inlist])
            return combinations(n-1, inlist, new_outlist)
        else:
            return combinations(n-1, inlist, inlist)

def betterCount(sequence, word):
    '''Return the number of overlapping occurrences of substring 'word' in
    string 'sequence' '''
    ret_val=0
    pos=sequence.find(word)
    pos+=1
    while pos:
        pos=sequence.find(word, pos)
        ret_val+=1
        pos+=1
    return ret_val

def frequence(sequence, nuc, count=0):
    if len(nuc)==1:
        count = count or sequence.count(nuc)
        return count/float(len(sequence))
    count = count or betterCount(sequence, nuc)
    return count/float(len(sequence)-len(nuc)+1)

def nucList(sequence, length):
    '''Zwraca zakładające się podsekwencje danej sekwencji o żądanej długości'''
    return [sequence[x:x+length] for x in range(len(sequence)-length+1)]

def makeCombinations(oligo_nuc, iupac=NA_IUPAC):
    '''Zwraca listę rzeczywistych oligonukleotydów na podstawie
    oligonukleotydu w skład którego wchodzą nuc zdegenerowane'''
    oligo_nuc_list=[]
    for nuc in oligo_nuc:
        for key in iupac.keys():
            if nuc in key:
                nucs=iupac[key]
                break
        if oligo_nuc_list:
            new_oligo_nuc_list=[]
            for element in oligo_nuc_list:
                new_oligo_nuc_list.extend(['%s%s'%(element, x) for x in nucs])
            oligo_nuc_list = new_oligo_nuc_list
        else:
            oligo_nuc_list=nucs
    return set(oligo_nuc_list)

def nucFrequencies(sequence, length, mono=('A', 'C', 'G', 'T')):
    '''zwraca częstości oligonukleotydów o zadanej długości + częstości mononukleotydów
    na danej nici'''
    ret_dict={}
    seq_len=len(sequence)
    mono_count=dict([(nuc, 0) for nuc in mono])
    desired_nucs=combinations(length, mono)

    for nuc in mono:
        count = betterCount(sequence, nuc)
        ret_dict[nuc]=frequence(sequence, nuc, count)
        mono_count[nuc]=count

    for nuc in desired_nucs:
        ret_dict[nuc]=frequence(sequence, nuc)

    if seq_len!=sum(mono_count.values()):
        #mamy zdegenerowane
        for nuc in sequence:
            if not nuc in mono:
                for sub_nuc in NA_IUPAC[nuc]:
                    ret_dict[sub_nuc]+=1.0/seq_len/len(NA_IUPAC[nuc])
        if length-1:
            for nuc in nucList(sequence, length):
                if not nuc in desired_nucs:
                    real_nucs=makeCombinations(nuc)
                    for real_nuc in real_nucs:
                        ret_dict[real_nuc]+=1.0/(seq_len-length+1)/len(real_nucs)
    return ret_dict