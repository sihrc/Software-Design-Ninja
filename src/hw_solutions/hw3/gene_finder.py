from amino_acids import aa, codons
from random import shuffle

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    amino_acid_output = ""
    for i in xrange(0,len(dna),3):
        my_codon = dna[i:i+3]
        for j in range(len(codons)):
            if my_codon in codons[j]:
                amino_acid_output += aa[j]
                break
    return amino_acid_output
    

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    reverse_complement_output = ""
    for i in range(len(dna)):
        base = dna[len(dna)-(i+1)]
        complementary_base = ""
        if base == 'T':
            complementary_base = 'A'
        elif base == 'A':
            complementary_base = 'T'
        elif base == 'G':
            complementary_base = 'C'
        elif base == 'C':
            complementary_base = 'G'
        reverse_complement_output += complementary_base
    return reverse_complement_output


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    ORF_output = ""
    for i in xrange(0,len(dna),3):
        my_codon = dna[i:i+3]
        if my_codon == 'TAA' or my_codon == 'TAG' or my_codon == 'TGA':
            return ORF_output
        else:
            ORF_output += my_codon
    return ORF_output

        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    all_ORFs_output = []
    dna_length = len(dna)
    current_dna_location = 0
    while(current_dna_location < dna_length):
        my_codon = dna[current_dna_location : current_dna_location + 3]
        if my_codon == 'ATG':
            discovered_ORF = rest_of_ORF(dna[current_dna_location : dna_length])
            all_ORFs_output.append(discovered_ORF)
            current_dna_location += len(discovered_ORF)
        else:
            current_dna_location += 3
    return all_ORFs_output

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    dna_frame_0 = dna
    dna_frame_1 = dna[1:]
    dna_frame_2 = dna[2:]

    ORFs_frame_0 = find_all_ORFs_oneframe(dna_frame_0)
    ORFs_frame_1 = find_all_ORFs_oneframe(dna_frame_1)
    ORFs_frame_2 = find_all_ORFs_oneframe(dna_frame_2)

    return ORFs_frame_0 + ORFs_frame_1 + ORFs_frame_2


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    reversed_dna = get_reverse_complement(dna)

    non_reversed_all_ORFs = find_all_ORFs(dna)
    reversed_all_ORFs = find_all_ORFs(reversed_dna)

    return non_reversed_all_ORFs + reversed_all_ORFs

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    all_ORFs = find_all_ORFs_both_strands(dna)
    max_len = 0
    max_len_index = 0
    for i in range(len(all_ORFs)):
        if len(all_ORFs[i]) > max_len:
            max_len = len(all_ORFs[i])
            max_len_index = i
    return all_ORFs[max_len_index]

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    dna_list = list(dna)
    
    for k in range(0,num_trials):
        shuffle(dna_list)
        collapse(dna_list)
    return len(longest_ORF(collapse(dna_list)))

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    amino_acid_squences_output = []
    all_ORFs = find_all_ORFs_both_strands(dna)
    for ORF in all_ORFs:
        if len(ORF) >= threshold:
            amino_acid_sequence = coding_strand_to_AA(ORF)
            amino_acid_squences_output.append(amino_acid_sequence)
    return amino_acid_squences_output
