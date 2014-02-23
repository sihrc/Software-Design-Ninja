from gene_finder import *
from load import load_seq
salmonella_dna = load_seq("./data/X73525.fa")

def two_lists_contain_same_elements(list1, list2):
    if len(list1) != len(list2):
        return False
    else: 
        for list_item in list1:
            if list_item in list2:
                continue
            else:
                return False
        return True


def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """

    # DNA input strands 
    dna_input1 = "ACTGCCCC"
    dna_input2 = "AGCTGAGGGTGTTTTGGA"
    dna_input3 = "CAGGCTTGCGGCTTCTTAA"

    # Expected output amino acid strands
    e_output1 = "TA"
    e_output2 = "S|GCFG"
    e_output3 = "QACGFL"

    # Actual output amino acid strands 
    a_output1 = coding_strand_to_AA(dna_input1)
    a_output2 = coding_strand_to_AA(dna_input2)
    a_output3 = coding_strand_to_AA(dna_input3)

    test1_result = (e_output1 == a_output1)
    test2_result = (e_output2 == a_output2)
    test3_result = (e_output3 == a_output3)

    if not test1_result:
        print "Test 1 FAILED: \n" + "Input DNA: " + dna_input1 + '\n' + "Expected Output: " + str(e_output1) + "\nActual (your) Output: " + str(a_output1)
    if not test2_result:
        print "Test 2 FAILED: \n" + "Input DNA: " + dna_input2 + '\n' + "Expected Output: " + str(e_output2) + "\nActual (your) Output: " + str(a_output2)
    if not test3_result:
        print "Test 3 FAILED: \n" + "Input DNA: " + dna_input3 + '\n' + "Expected Output: " + str(e_output3) + "\nActual (your) Output: " + str(a_output3)

    if test1_result and test2_result and test3_result:
        return 'PASSED'
    else:
        return 'FAILED'
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """

    # DNA input strands 
    dna_input1 = "ACTGCCCC"
    dna_input2 = "AGCTGAGGGTGTTTTGGA"
    dna_input3 = "CAGGCTTGCGGCTTCTTAA"

    # Expected output DNA strands
    e_output1 = "GGGGCAGT"
    e_output2 = "TCCAAAACACCCTCAGCT"
    e_output3 = "TTAAGAAGCCGCAAGCCTG"

    # Actual output DNA strands
    a_output1 = get_reverse_complement(dna_input1)
    a_output2 = get_reverse_complement(dna_input2)
    a_output3 = get_reverse_complement(dna_input3)

    test1_result = (e_output1 == a_output1)
    test2_result = (e_output2 == a_output2)
    test3_result = (e_output3 == a_output3)

    if not test1_result:
        print "Test 1 FAILED: \n" + "Input DNA: " + dna_input1 + '\n' + "Expected Output: " + str(e_output1) + "\nActual (your) Output: " + str(a_output1)
    if not test2_result:
        print "Test 2 FAILED: \n" + "Input DNA: " + dna_input2 + '\n' + "Expected Output: " + str(e_output2) + "\nActual (your) Output: " + str(a_output2)
    if not test3_result:
        print "Test 3 FAILED: \n" + "Input DNA: " + dna_input3 + '\n' + "Expected Output: " + str(e_output3) + "\nActual (your) Output: " + str(a_output3)

    if test1_result and test2_result and test3_result:
        return 'PASSED'
    else:
        return 'FAILED'

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """

    # DNA input strands 
    dna_input1 = "ATGTTTAAGCCGTAAATGAAACCGGGC"
    dna_input2 = "ATGTAG"
    dna_input3 = "ATGCCGATAGCCTGACCGATAAAATTG"
    dna_input4 = "ATGC"

    # Expected output DNA strands
    e_output1 = "ATGTTTAAGCCG"
    e_output2 = "ATG"
    e_output3 = "ATGCCGATAGCC"
    e_output4 = "ATGC"

    # Actual output DNA strands
    a_output1 = rest_of_ORF(dna_input1)
    a_output2 = rest_of_ORF(dna_input2)
    a_output3 = rest_of_ORF(dna_input3)
    a_output4 = rest_of_ORF(dna_input4)

    test1_result = (e_output1 == a_output1)
    test2_result = (e_output2 == a_output2)
    test3_result = (e_output3 == a_output3)
    test4_result = (e_output4 == a_output4)

    if not test1_result:
        print "Test 1 FAILED: \n" + "Input DNA: " + dna_input1 + '\n' + "Expected Output: " + str(e_output1) + "\nActual (your) Output: " + str(a_output1)
    if not test2_result:
        print "Test 2 FAILED: \n" + "Input DNA: " + dna_input2 + '\n' + "Expected Output: " + str(e_output2) + "\nActual (your) Output: " + str(a_output2)
    if not test3_result:
        print "Test 3 FAILED: \n" + "Input DNA: " + dna_input3 + '\n' + "Expected Output: " + str(e_output3) + "\nActual (your) Output: " + str(a_output3)
    if not test4_result:
        print "Test 4 FAILED: \n" + "Input DNA: " + dna_input4 + '\n' + "Expected Output: " + str(e_output4) + "\nActual (your) Output: " + str(a_output4)

    if test1_result and test2_result and test3_result and test4_result:
        return 'PASSED'
    else:
        return 'FAILED'
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    # DNA input strands 
    dna_input1 = "ATGCATGAATGTAGATAGATGTGCCC"
    dna_input2 = "ATGCCCGGGTATCCGGAAATAG"
    dna_input3 = "CCGTTTATGCCGTAGTTAGACATGCCCGAGTAAGCGATGTTTATAGGGC"

    # Expected output list of ORFs
    e_output1 = ['ATGCATGAATGTAGA', 'ATGTGCCC']
    e_output2 = ['ATGCCCGGGTATCCGGAAATAG']
    e_output3 = ['ATGCCG', 'ATGCCCGAG', 'ATGTTTATAGGGC']

    # Actual output list of ORFs
    a_output1 = find_all_ORFs_oneframe(dna_input1)
    a_output2 = find_all_ORFs_oneframe(dna_input2)
    a_output3 = find_all_ORFs_oneframe(dna_input3)

    test1_result = two_lists_contain_same_elements(e_output1, a_output1)
    test2_result = two_lists_contain_same_elements(e_output2, a_output2)
    test3_result = two_lists_contain_same_elements(e_output3, a_output3)

    if not test1_result:
        print "Test 1 FAILED: \n" + "Input DNA: " + dna_input1 + '\n' + "Expected Output: " + str(e_output1) + "\nActual (your) Output: " + str(a_output1)
    if not test2_result:
        print "Test 2 FAILED: \n" + "Input DNA: " + dna_input2 + '\n' + "Expected Output: " + str(e_output2) + "\nActual (your) Output: " + str(a_output2)
    if not test3_result:
        print "Test 3 FAILED: \n" + "Input DNA: " + dna_input3 + '\n' + "Expected Output: " + str(e_output3) + "\nActual (your) Output: " + str(a_output3)

    if test1_result and test2_result and test3_result:
        return 'PASSED'
    else:
        return 'FAILED'


def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """

    # DNA input strands 
    # tests offset by 2 and 0 ORFs, multiple ORFs
    dna_input1 = "ATGCATGAATGTAGATAGATGTGCCC"
    # tests offset by two and only one ORF
    dna_input2 = "GCATGCCCGGGTATCCGGAAATAG"
    # nested reading frame, that won't be included
    dna_input3 = "GATGTTTATGGGCTAGTAG"

    # Expected output list of ORFs
    e_output1 = ['ATGCATGAATGTAGA', 'ATGTGCCC', 'ATGAATGTAGATAGATGTGCCC', 'ATG']
    e_output2 = ['ATGCCCGGGTATCCGGAAATAG']
    e_output3 = ['ATGTTTATGGGC']

    # Actual output list of ORFs
    a_output1 = find_all_ORFs(dna_input1)
    a_output2 = find_all_ORFs(dna_input2)
    a_output3 = find_all_ORFs(dna_input3)

    test1_result = two_lists_contain_same_elements(e_output1, a_output1)
    test2_result = two_lists_contain_same_elements(e_output2, a_output2)
    test3_result = two_lists_contain_same_elements(e_output3, a_output3)

    if not test1_result:
        print "Test 1 FAILED: \n" + "Input DNA: " + dna_input1 + '\n' + "Expected Output: " + str(e_output1) + "\nActual (your) Output: " + str(a_output1)
    if not test2_result:
        print "Test 2 FAILED: \n" + "Input DNA: " + dna_input2 + '\n' + "Expected Output: " + str(e_output2) + "\nActual (your) Output: " + str(a_output2)
    if not test3_result:
        print "Test 3 FAILED: \n" + "Input DNA: " + dna_input3 + '\n' + "Expected Output: " + str(e_output3) + "\nActual (your) Output: " + str(a_output3)

    if test1_result and test2_result and test3_result:
        return 'PASSED'
    else:
        return 'FAILED'

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # stop codons: ['TAA', 'TAG', 'TGA']

    # DNA input strands 
    # reverse of 1 is GGGCACATCTATCTACATTCATGCAT
    dna_input1 = "ATGCATGAATGTAGATAGATGTGCCC"
    # reverse of 2 is CTATTTCATGATATAACCCATGCATGC
    dna_input2 = "GCATGCATGGGTTATATCATGAAATAG"
    # reverse of 3 is GATGTTTATGGGCCATTAGTAG
    dna_input3 = "CTACTAATGGCCCATAAACATC"

    # Expected output list of ORFs
    e_output1 = ['ATGCATGAATGTAGA', 'ATGTGCCC', 'ATGAATGTAGATAGATGTGCCC', 'ATG', 'ATGCAT']
    e_output2 = ['ATGCATGGGTTATATCATGAAATAG', 'ATGGGTTATATCATGAAA', 'ATGATA', 'ATGCATGC', 'ATGC']
    e_output3 = ['ATGTTTATGGGCCAT', 'ATGGCCCATAAACATC']

    # Actual output list of ORFs
    a_output1 = find_all_ORFs_both_strands(dna_input1)
    a_output2 = find_all_ORFs_both_strands(dna_input2)
    a_output3 = find_all_ORFs_both_strands(dna_input3)

    test1_result = two_lists_contain_same_elements(e_output1, a_output1)
    test2_result = two_lists_contain_same_elements(e_output2, a_output2)
    test3_result = two_lists_contain_same_elements(e_output3, a_output3)

    if not test1_result:
        print "Test 1 FAILED: \n" + "Input DNA: " + dna_input1 + '\n' + "Expected Output: " + str(e_output1) + "\nActual (your) Output: " + str(a_output1)
    if not test2_result:
        print "Test 2 FAILED: \n" + "Input DNA: " + dna_input2 + '\n' + "Expected Output: " + str(e_output2) + "\nActual (your) Output: " + str(a_output2)
    if not test3_result:
        print "Test 3 FAILED: \n" + "Input DNA: " + dna_input3 + '\n' + "Expected Output: " + str(e_output3) + "\nActual (your) Output: " + str(a_output3)

    if test1_result and test2_result and test3_result:
        return 'PASSED'
    else:
        return 'FAILED'

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # DNA input strands 
    dna_input1 = "ATGCATGAATGTAGATAGATGTGCCC"
    dna_input2 = "GCATGCATGGGTTATATCATGAAATAG"
    dna_input3 = "CTACTAATGGCCCATAAACATC"

    # Expected output list of ORFs
    e_output1 = 'ATGAATGTAGATAGATGTGCCC'
    e_output2 = 'ATGCATGGGTTATATCATGAAATAG'
    e_output3 = 'ATGGCCCATAAACATC'

    # Actual output list of ORFs
    a_output1 = longest_ORF(dna_input1)
    a_output2 = longest_ORF(dna_input2)
    a_output3 = longest_ORF(dna_input3)

    test1_result = (e_output1 == a_output1)
    test2_result = (e_output2 == a_output2)
    test3_result = (e_output3 == a_output3)

    if not test1_result:
        print "Test 1 FAILED: \n" + "Input DNA: " + dna_input1 + '\n' + "Expected Output: " + str(e_output1) + "\nActual (your) Output: " + str(a_output1)
    if not test2_result:
        print "Test 2 FAILED: \n" + "Input DNA: " + dna_input2 + '\n' + "Expected Output: " + str(e_output2) + "\nActual (your) Output: " + str(a_output2)
    if not test3_result:
        print "Test 3 FAILED: \n" + "Input DNA: " + dna_input3 + '\n' + "Expected Output: " + str(e_output3) + "\nActual (your) Output: " + str(a_output3)

    if test1_result and test2_result and test3_result:
        return 'PASSED'
    else:
        return 'FAILED'

def gene_finder_unit_test():

    # DNA input strands 
    dna_input1 = "ATGCATGAATGTAGATAGATGTGCCC"
    dna_input2 = "GCATGCATGGGTTATATCATGAAATAG"
    dna_input3 = "CTACTAATGGCCCATAAACATC"

    # Threshold inputs
    t1 = 8
    t2 = 5
    t3 = 20

    # Expected output list of ORFs
    # ['ATGCATGAATGTAGA', 'ATGTGCCC', 'ATGAATGTAGATAGATGTGCCC', 'ATG', 'ATGCAT']
    e_output1 = ['MHECR', 'MC', 'MNVDRCA']
    # ['ATGCATGGGTTATATCATGAAATAG', 'ATGGGTTATATCATGAAA', 'ATGATA', 'ATGCATGC', 'ATGC']
    e_output2 = ['MHGLYHEI', 'MGYIMK', 'MI', 'MH']
    # ['ATGTTTATGGGCCAT', 'ATGGCCCATAAACATC']
    e_output3 = []

    # Actual output list of ORFs
    a_output1 = gene_finder(dna_input1, t1)
    a_output2 = gene_finder(dna_input2, t2)
    a_output3 = gene_finder(dna_input3, t3)

    test1_result = two_lists_contain_same_elements(e_output1, a_output1)
    test2_result = two_lists_contain_same_elements(e_output2, a_output2)
    test3_result = two_lists_contain_same_elements(e_output3, a_output3)

    if not test1_result:
        print "Test 1 FAILED: \n" + "Input DNA: " + dna_input1 + '\n' + "Expected Output: " + str(e_output1) + "\nActual (your) Output: " + str(a_output1)
    if not test2_result:
        print "Test 2 FAILED: \n" + "Input DNA: " + dna_input2 + '\n' + "Expected Output: " + str(e_output2) + "\nActual (your) Output: " + str(a_output2)
    if not test3_result:
        print "Test 3 FAILED: \n" + "Input DNA: " + dna_input3 + '\n' + "Expected Output: " + str(e_output3) + "\nActual (your) Output: " + str(a_output3)

    if test1_result and test2_result and test3_result:
        return 'PASSED'
    else:
        return 'FAILED'


if __name__ == "__main__":
    print coding_strand_to_AA_unit_tests() + " - DNA to AA strand conversion\n"
    print get_reverse_complement_unit_tests() + " - reverse complement of DNA strand\n"
    print rest_of_ORF_unit_tests() + " - get ORF that starts with a start codon\n"
    print find_all_ORFs_oneframe_unit_tests() + ' - find all ORFs one frame\n'
    print find_all_ORFs_unit_tests() + ' - find all ORFs all frames\n'
    print find_all_ORFs_both_strands_unit_tests() + ' - finds all ORFs all frames, reverse strand included\n'
    print longest_ORF_unit_tests() + ' - finds the longest ORF, reverse strand included\n'

    longest_ORF_noncoding_test_string = "Sample longest_ORF_noncoding results: ["
    for i in range(10):
        longest_ORF_noncoding_test_string += str(longest_ORF_noncoding(salmonella_dna, 100))
        if i < 9:
            longest_ORF_noncoding_test_string += ", "
        else:
            longest_ORF_noncoding_test_string += "]\n"
    print longest_ORF_noncoding_test_string

    print gene_finder_unit_test() + ' - find the AA sequences in a gene based on the ORFs'



    