"""
Zach Fechko
Comp Sci 315
PA 1
Note: If there's any similarity to anthony ghimpu's code, we helped each other out a bit
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
        bar.update((line_count / len(dataset)) * 100)
    bar.finish()
    return {key: value for key, value in item_count.items() if value >= support}

def apriori_pass_2(dataset, singles, support) -> dict:
    """
    - finds the frequent pairs in the dataset. 
    - Returns a dictionary of pairs and their support
    """
    item_counts = {} #dictionary of item counts
    line_count = 0
    bar = pb.ProgressBar().start()
    for line in dataset:
        temp = set(line).intersection(singles) #only look at the frequent singles
        combos = list(map(frozenset, combinations(temp, 2))) #get all combinations of size 2 from temp
        for combination in combos: #for each combination
            if item_counts.get(combination): #if the combination is already in the dictionary
                item_counts[combination] += 1 #increment the count
            else:
                item_counts[combination] = 1 #otherwise, add the combination to the dictionary
        line_count += 1
        bar.update((line_count / len(dataset)) * 100) #update the progress bar based on the number of lines processed
    bar.finish()
    return {key: value for key, value in item_counts.items() if value >= support} #return the dictionary with only the items that meet the support


def apriori_pass_3(dataset, support, singles) -> dict:
    """
    - finds the frequent triples in the dataset
    - returns a dictionary of triples and their support
    """
    item_counts = {} #dictionary of item counts
    line_count = 0
    bar = pb.ProgressBar().start() #progress bar
    for line in dataset:
        temp = set(line).intersection(singles) #only look at the items that are frequent singles
        combos = list(map(frozenset, combinations(temp, 3))) #get all combinations of size 3 from temp
        for combination in combos: #for each combination
            if item_counts.get(combination): #if the combination is already in the dictionary
                item_counts[combination] += 1 #increment the count
            else:
                item_counts[combination] = 1 #otherwise, add the combination to the dictionary
        line_count += 1
        bar.update((line_count / len(dataset)) * 100) #update the progress bar based on the number of lines processed
    bar.finish() #finish the progress bar
    return {key: value for key, value in item_counts.items() if value >= support}

def calculate_doubles_confidence(frequent_pairs, frequent_singles):
    """
    - calculates the confidence of the association rules for each pair, which is calculated as
    number of times the pair occurs / number of times the first item occurs. 
    - Returns a list of tuples sorted by confidence in descending order
    """
    confidence = {}
    for pair in list(map(tuple, frequent_pairs.keys())):
        #X => Y
        confidence[(pair[0], pair[1])] = frequent_pairs[frozenset(pair)] / frequent_singles[pair[0]]
        #Y => X
        confidence[(pair[1], pair[0])] = frequent_pairs[frozenset(pair)] / frequent_singles[pair[1]]
    return sorted(confidence.items(), key=lambda item: item[1], reverse=True) #return sorted confidence list

    
    

def calculate_triples_confidence(frequent_triples, frequent_pairs):
    """
    - calculates the confidence for each triple
    - returns a list of tuples sorted by confidence in descending order
    """
    confidence = {}
    for triple in list(map(tuple, frequent_triples.keys())):
        #(X, Y) => Z
        confidence[(triple[0], triple[1], triple[2])] = frequent_triples[frozenset(triple)] / frequent_pairs[frozenset((triple[0], triple[1]))]
        #(X, Z) => Y
        confidence[(triple[0], triple[2], triple[1])] = frequent_triples[frozenset(triple)] / frequent_pairs[frozenset((triple[0], triple[2]))]
        #(Y, Z) => X
        confidence[(triple[1], triple[2], triple[0])] = frequent_triples[frozenset(triple)] / frequent_pairs[frozenset((triple[1], triple[2]))]
    return sorted(confidence.items(), key=lambda item: item[1], reverse=True)

def print_doubles_confidence(doubles_confidence):
    """
    Prints the pairs and their confidence the same way we would for dumping to the txt file
    """
    print("Output A:")
    for pair in doubles_confidence:
        print(f"{pair[0][0]} {pair[0][1]} {pair[1]}\n")

def print_triples_confidence(triples_confidence):
    """
    Prints the triples and their confidence the same way we would for dumping to the txt file
    """
    print("Output B:")
    for triple in triples_confidence:
        print(f"{triple[0][0]} {triple[0][1]} {triple[0][2]} {triple[1]}\n")

def dump_to_file(pairs_output: list[tuple], triples_output: list[tuple]):
    """
    dumps the output to a file following the format in the assignment description
    """
    with open(OUTFILE, 'w') as outfile:
        #write the pairs + associated confidence
        outfile.write("Output A:\n")
        for pair in pairs_output:
            outfile.write(f"{pair[0][0]} {pair[0][1]} {pair[1]}\n")
        #write the triples + associated confidence
        outfile.write("\nOutput B:\n")
        for triple in triples_output:
            outfile.write(f"{triple[0][0]} {triple[0][1]} {triple[0][2]} {triple[1]}\n")
        

def main():
    """
    Carries out assignment flow
    - reads in the data
    - finds the pairs that fit the support s = 100
    - finds the triples that fit the support s = 100
    - calculates confidence value for each pair/triple
    - dumps output to file
    """
    groomed_data = read_infile()

    print("finding singles")
    support_singles = apriori_pass_1(groomed_data, SUPPORT)
    singles = set(support_singles.keys())

    print("finding pairs")
    support_pairs = apriori_pass_2(groomed_data, singles, SUPPORT)
    
    frequent_items = set(chain.from_iterable(support_pairs.keys()))

    print("finding triples")
    support_triples = apriori_pass_3(groomed_data, SUPPORT, frequent_items)

    pairs_confidence = calculate_doubles_confidence(support_pairs, support_singles)
    triples_confidence = calculate_triples_confidence(support_triples, support_pairs)
    
    print_doubles_confidence(pairs_confidence[:5])
    print_triples_confidence(triples_confidence[:5])

    dump_to_file(pairs_confidence[:5], triples_confidence[:5])

    
if __name__ == '__main__':
    main()

