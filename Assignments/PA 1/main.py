"""
Zach Fechko
Comp Sci 315
PA 1
"""

#from apyori import apriori
from itertools import combinations, chain
import progressbar as pb

INFILE = 'data/browsing-data.txt'
OUTFILE = 'output.txt'
SUPPORT = 100

def read_infile():
    """
    reads in the input file and returns groomed data in a list of lists
    """
    with open(INFILE, 'r') as infile:
        all_lines = infile.readlines()

    return [[data_point for data_point in line.split()] for line in all_lines]

def apriori_pass_1(dataset, support) -> dict:
    """
    finds the singles in the dataset
    """
    bar = pb.ProgressBar().start()
    item_count = {}
    line_count = 0
    for basket in dataset:
        for item in basket:
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
        line_count += 1
        bar.update(line_count / len(dataset) * 100)
    bar.finish()
    return {key: value for key, value in item_count.items() if value >= support}

def apriori_pass_2(dataset, singles, support) -> dict:
    """
    finds the frequent pairs in the dataset
    """
    item_counts = {} #dictionary of item counts
    line_count = 0
    bar = pb.ProgressBar().start()
    combos = set(combinations(singles, 2)) #set of tuples that have all possible combinations of 2 items
    for line in dataset:
        for combination in combos: #for each combination
            if combination[0] in line and combination[1] in line: #if both items are in the same line
                if combination not in item_counts: #if the combination is not in the dictionary
                    item_counts[combination] = 1 #add it to the dictionary and set its value to 1
                else:
                    item_counts[combination] += 1 #if it is in the dictionary, increment its value
        line_count += 1
        bar.update(line_count / len(dataset) * 100)
    bar.finish()
    return {key: value for key, value in item_counts.items() if value >= support} #return the dictionary with only the items that meet the support


def apriori_pass_3(dataset, support, singles) -> dict:
    """
    finds the frequent triples in the dataset
    """
    item_counts = {} #dictionary of item counts
    line_count = 0
    bar = pb.ProgressBar().start() #progress bar
    combos = set(combinations(singles, 3)) #set of tuples that have all possible combinations of 3 items
    for line in dataset:
        for combination in combos:
            if combination[0] in line and combination[1] in line and combination[2] in line:
                if combination not in item_counts:
                    item_counts[combination] = 1
                else:
                    item_counts[combination] += 1
        line_count += 1
        bar.update(line_count / len(dataset) * 100) #update the progress bar based on the number of lines processed
    bar.finish() #finish the progress bar
    return {key: value for key, value in item_counts.items() if value >= support}

def calculate_doubles_confidence(frequent_pairs, frequent_singles):
    """
    calculates the confidence for each pair
    """

def calculate_triples_confidence(frequent_triples, frequent_pairs, frequent_singles):
    """
    calculates the confidence for each triple
    """

def dump_to_file(pairs_output, triples_output):
    """
    dumps the output to a file following the format in the assignment description
    """
    with open(OUTFILE, 'w') as outfile:
        #write the pairs + associated confidence
        outfile.write("Output A:\n")
        

def main():
    """
    Carries out assignment flow
    - reads in the data
    - finds the pairs that fit the support
    - finds the triples that fit the support
    - calculates confidence value for each pair/triple
    - dumps output to file
    """
    groomed_data = read_infile()
    print("finding singles")
    support_singles = apriori_pass_1(groomed_data, SUPPORT)
    singles = list(support_singles.keys())
    print("finding pairs")
    support_pairs = apriori_pass_2(groomed_data, singles, SUPPORT)
    frequent_items = set(chain.from_iterable(support_pairs.keys()))
    print(frequent_items)

    
if __name__ == '__main__':
    main()

