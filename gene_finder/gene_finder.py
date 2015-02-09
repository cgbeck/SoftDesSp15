# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Christopher Beck

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    # This is not sufficient because there is a loop for each nucleotide thus only 2 tests is insufficient
    # Also this doesnt test for when the nucleotide is fake (meaning it isnt atgc)
    # >>> get_complement('T')
    # 'A'
    # >>> get_complement('G')
    # 'C'

    nucl_matchings = {"A": 'T', "T": 'A', "G": 'C', "C": 'G'}
    return nucl_matchings[nucleotide]
    print nucl_matchings[nucleotide]




def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence

        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # It is probably sufficient because it tests everything including flipping

    n = 0
    Fdna = ''
    while n < len(dna):
        nuc = dna[n] 
        Fdna = Fdna + get_complement(nuc)
        n += 1
    Final = Fdna[::-1] 
    return Final
    print Final

    # for n in range(len(dna)):
    #     nuc = dna(n)

    # for nuc in dna:



# def rest_of_ORF(dna):
#     """ Takes a DNA sequence that is assumed to begin with a start codon and returns
#         the sequence up to but not including the first in frame stop codon.  If there
#         is no in frame stop codon, returns the whole string.
        
#         dna: a DNA sequence
#         returns: the open reading frame represented as a string
#     >>> rest_of_ORF("ATGTGAA")
#     'ATG'
#     >>> rest_of_ORF("ATGAGATAGG")
#     'ATGAGA'
#     """

#     # TODO: implement this
#     pass

# def find_all_ORFs_oneframe(dna):
#     """ Finds all non-nested open reading frames in the given DNA sequence and returns
#         them as a list.  This function should only find ORFs that are in the default
#         frame of the sequence (i.e. they start on indices that are multiples of 3).
#         By non-nested we mean that if an ORF occurs entirely within
#         another ORF, it should not be included in the returned list of ORFs.
        
#         dna: a DNA sequence
#         returns: a list of non-nested ORFs
#     >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
#     ['ATGCATGAATGTAGA', 'ATGTGCCC']
#     """


#     # TODO: implement this
#     pass

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    #  this is not sufficient because it doenst test different end codons.

    orf = []
    pass_num = 0
    CurrentStr = dna
    # n < len(CurrentStr)
    while pass_num + 3 < len(CurrentStr):
        n = 3 + pass_num
        while CurrentStr[n-3:n] != 'ATG':
            n += 3
        m = n
        while CurrentStr[m-3:m] != 'TAG' & CurrentStr[m-3:m] != 'TAA' & CurrentStr[m-3:m] != 'TGA':
            m += 3
        x = CurrentStr[n-3:m-3]
        return x
        orfs.append(x)
        m = 0
        pass_num += 1
    return orfs


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """

    # The number of test is sufficient because it looks in both directions

    orfpt1 = find_all_ORFs(dna)
    x = get_reverse_complement(dna)
    orfpt2 = find_all_ORFs(x)
    allORF = orfpt1 + orfpt2
    return allORF



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """ 
    # this one needs another test going in the opposite direction to show that it works in reverse as well as forward like normal

    Orf.sort(cmp,key = 0,reverse = True)
    longest = Orf.pop(0)
    print longest
    return longest

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    length_orf = []
    i = 0
    while i < num_trials:
        x = shuffle_string(dna)
        longestStr = longest_ORF(find_all_ORFs_both_strands(x))
        length_LORF = len(longestStr)
        length_orf.append(length_LORF)
        i += 1
    length_orf.sort(cmp,key = 0,reverse = True)
    longest = length_orf.pop(0)
    return longest


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    #  This function has enough tests to show it works, so no new ones are needed.

    codon_matchings =  {'TTT': 'F', 'TTC': 'F', 
                        'TTA': 'L', 'TTG': 'L', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
                        'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
                        'ATG': 'M',
                        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
                        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'AGT': 'S', 'AGC': 'S', 
                        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                        'TAT': 'Y', 'TAC': 'Y',
                        'TAA': '|', 'TAG': '|', 'TGA': '|',
                        'CAT': 'H', 'CAC': 'H',
                        'CAA': 'Q', 'CAG': 'Q',
                        'AAT': 'N', 'AAC': 'N',
                        'AAA': 'K', 'AAG': 'K',
                        'GAT': 'D', 'GAC': 'D',
                        'GAA': 'E', 'GAG': 'E',
                        'TGT': 'C', 'TGC': 'C',
                        'TGG': 'W',
                        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
                        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

    n = 3
    m = 0
    Final = ''
    CurrentStr = dna
    while n < len(CurrentStr) + 3:
        if len(CurrentStr[m:n]) == 3: 
            StrSection = CurrentStr[m:n]
            x = codon_matchings[StrSection]
            Final = Final + x
            m = n
            n += 3
            n = m + 3
        else:
            x = ''
    return Final


def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    n = 0
    Final_ORFS = []
    strands = find_all_ORFs_both_strands(dna)
    largestVal = longest_ORF_noncoding(dna, 1500)
    while n < len(strands):
        x = strands.Pop(n)
        if len(x) >= largestVal:
            aa_strand = coding_strand_to_AA(x)
            Final_ORFS.append(aa_strand)
            n += 1
        else:
            n += 1
    return Final_ORFS


if __name__ == "__main__":
    import doctest
    doctest.testmod()