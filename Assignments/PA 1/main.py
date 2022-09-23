"""
Zach Fechko
Comp Sci 315
PA 1
"""

from apyori import apriori
from itertools import combinations, chain

INFILE = 'data/browsing_data.txt'
OUTFILE = 'output.txt'
SUPPORT = 100

def read_infile():
    """
    reads in the input file and returns groomed data in a list of lists
    """
    with open(INFILE, 'r') as infile:
        all_lines = infile.readlines()

    return [[data_point for data_point in line.split()] for line in all_lines]

def apriori_pass_1(dataset, support):
    """
    finds the singles in the dataset
    """
    item_count = {}
    for basket in dataset:
        for item in basket:
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    return {key: value for key, value in item_count.items() if value >= support}

def apriori_pass_2(dataset, support, singles):
    """
    finds the doubles in the dataset
    """
    
    

