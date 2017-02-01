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

import itertools

NA_IUPAC = {'A':('A',), 'C':('C',), 'G':('G',), 'T':('T',),
            'R':('A','G'), 'Y':('C','T'), 'M':('A','C'), 'K':('G','T'),
            'S':('C','G'), 'W':('A','T'), 'B':('C','G','T'), 'D':('A','G','T'),
            'H':('A','C','T'), 'V':('A','C','G'), 'N':('A','C','G','T')}

transcription_dict={'A':'T', 'C':'G', 'G':'C', 'T':'A', 'U':'A', 'R':'Y',
                    'Y':'R', 'N':'N', 'M':'K', 'K':'M', 'S':'W', 'W':'S',
                    'B':'V', 'V':'B', 'D':'H', 'H':'D'}

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

def reverseComplement(a_string, transcript_dict=transcription_dict):
    a_list=[transcript_dict[s] for s in a_string]
    a_list.reverse()
    return ''.join(a_list)

def thirdOrderBias( seq, strand, mono=('A', 'C', 'G', 'T'), transcript_dict=transcription_dict ):
	'''Częstotliwości względne nukleotdów w zależności od częstotliwości mono i di
	Patrz: http://www.pnas.org/content/89/4/1358.full.pdf '''
	assert len( seq ) > 2
	assert strand in ( 1, 2 )
	nuc_freqs = nucFrequencies( seq, 2 )
	mono_freqs 	= { k:v for k, v in nuc_freqs.iteritems() if len(k)==1 }
	di_freqs 	= { k:v for k, v in nuc_freqs.iteritems() if len(k)==2 }
	tri_freqs 	= { k:v for k, v in nucFrequencies( seq, 3 ).iteritems() if len(k)==3 }
	ret_dict = {}
	for key in tri_freqs:
		fxyz = tri_freqs[ key ]
		fixyz = tri_freqs[ reverseComplement(key) ]
		if fxyz==0 and ( strand==1 or (strand==2 and fixyz==0) ) :
			ret_dict[ key ] = 0.0
		else:
			fxy  = di_freqs [ key[:2] ]
			fyz  = di_freqs [ key[1:] ]
			fxnz = sum( tri_freqs[ '%s%s%s' %(key[0], n, key[2]) ] for n in mono )
			if strand==1:
				ret_dict[ key ] = float( fxyz ) * mono_freqs[ key[0] ] * mono_freqs[ key[1] ] * mono_freqs[ key[2] ] / ( fxy * fyz * fxnz )
			else:
				fix = mono_freqs[ transcript_dict[ key[0] ] ]
				fiy = mono_freqs[ transcript_dict[ key[1] ] ]
				fiz = mono_freqs[ transcript_dict[ key[2] ] ]
				fixy = di_freqs [ reverseComplement( key[:2] ) ]
				fiyz = di_freqs [ reverseComplement( key[1:] ) ]
				fixnz = sum( tri_freqs[ '%s%s%s' %(transcript_dict[key[2]], n, transcript_dict[key[0]]) ] for n in mono )
				ret_dict[ key ] = float(fxyz + fixyz) * (mono_freqs[key[0]] + fix) * (mono_freqs[key[1]] + fiy) * (mono_freqs[key[2]] + fiz) / ( 2 * (fxy + fixy) * (fyz + fiyz) * (fxnz + fixnz) )
	return ret_dict


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

def product(a_list):
    '''zwraca iloczyn elementow listy'''
    return reduce(lambda x, y: x*y, a_list)

def zeroDivision(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0

def relativeNucFrequencies(in_dict, strands, transcript_dict=transcription_dict):
    '''Przyjmuje wynik działania nucFrequencies. Zwraca słownik z względnymi
    częstościami występowania poszczególnych sekwencji. Przyjmujemy, że częstość występowania opigo zależy tylko od mono, a nie np trinuc od dinuc'''
    #częstotliwość oligonuc na obu niciach liczona według:
    #http://www.pnas.org/content/89/4/1358.full.pdf
    #raise Exception("sprawdzić poprawność liczenia częstości na dwu niciach")
    mono_dict=dict([(x, in_dict[x]) for x in in_dict if len(x)==1])
    oligo_dict=dict([(x, in_dict[x]) for x in in_dict if len(x)>1])
    nuc_len=len(oligo_dict.keys()[0])
    assert all( nuc_len == len(k) for k in oligo_dict )
    if len( mono_dict ) != 4:
    	for k in set([ 'A', 'C', 'G', 'T' ]) - set( mono_dict ):
    		mono_dict[ k ] = 0
    # jeśli oligo_dict jest niekompletny, tzn. dla niektórych oligo nie ma wpisów ( powinny być klucz:0 )
    if len( oligo_dict ) != nuc_len**2:
    	for k in [ ''.join(x) for x in itertools.product( mono_dict, repeat=nuc_len ) ]:
    		if k not in oligo_dict:
    			oligo_dict[ k ] = 0
    #pdb.set_trace()
    if not oligo_dict:
        return in_dict
    if strands-1:
        try:
            return { x:2**(nuc_len-1)*(oligo_dict[x]+oligo_dict[reverseComplement(x)])/product([mono_dict[y]+mono_dict[transcript_dict[y]] for y in x]) for x in oligo_dict}
        except ZeroDivisionError:
            return { x:2**(nuc_len-1)*zeroDivision((oligo_dict[x]+oligo_dict[reverseComplement(x)]),product([mono_dict[y]+mono_dict[transcript_dict[y]] for y in x])) for x in oligo_dict}
    else:
        try:
            return { x:float(oligo_dict[x])/product([mono_dict[y] for y in x]) for x in oligo_dict}
        except ZeroDivisionError:
            return { x:float( zeroDivision(oligo_dict[x],product([mono_dict[y] for y in x])) ) for x in oligo_dict}