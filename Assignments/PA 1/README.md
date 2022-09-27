# Programming Assignment 1

## Instructions

### Requirements
- [x] include a 'readme.txt' file on full instructions to run your program, within this folder. A list of all libraries used should also be included
- [x] This folder should have a script file named run_code.sh
- Assume relative paths
- Submit as a zip file

### Assignment instructions
Suppose we want to recommend new products to the customer based on the products they have already browsed online. Write a program using the A-priori algorithm to find products which are frequently browsed together. Fix the support to $s= 100$ (i.e products need to occur together at least 100 times to be considered frequent) and find item sets of size 2 and 3.

Use the online browsing behavior dataset provided. Each line represents a customer's browsing session. On each line, each string of characters represents the ID of an item browsed during that session. The items are separated by spaces.

- Identify pairs of items $(X,Y)$ such that the support of $\{X,Y\}$ is at least 100. For all such pairs, compute the confidence scores of the corresponding association rules $X\implies Y, Y\implies X$. Sort the rules in decreasing order of confidence scores and list the top 5 rules in the writeup. Break ties, if any, by lexicographically increasing order on the left hand side of the rule
- Identify item triples $(X, Y, Z)$ such that the support of $\{X, Y, Z\}$ is at 
least 100. For all such triples, compute the confidence scores of the 
corresponding association rules: $(X, Y) \implies Z, (X, Z) \implies Y, (Y, Z) \implies X$. 
Sort the rules in decreasing order of confidence scores and list the top 5 
rules in the writeup. Order the left-hand-side pair lexicographically and 
break ties, if any, by lexicographical order of the first then the second 
item in the pair. 
- The output of your program should be dumped in a file named "output.txt" in the following format:
```
OUTPUT A
DAI93865 FRO40251 1.0
GRO85051 FRO40251 0.999176276771005
GRO38636 FRO40251 0.9906542056074766
ELE12951 FRO40251 0.9905660377358491
DAI88079 FRO40251 0.9867256637168141
OUTPUT B
DAI23334 ELE92920 DAI62779 1.0
DAI31081 GRO85051 FRO40251 1.0
DAI55911 GRO85051 FRO40251 1.0
DAI62779 DAI88079 FRO40251 1.0
DAI75645 GRO85051 FRO40251 1.0
```
- Output breakdown:
    - Line 1 should have "Output A"
    - Next five lines should have the top five rules with decreasing confidence scores for part A of the assignment
        - Format:
        - `<item 1><item 2><confidence> meaning {item 1} => item 2`
    - line 2 should have "Output B"
    - Next five lines should have the top five rules with decreasing confidence scores for part B of the assignment.
        - Format:
        - `<item 1> <item 2> <item 3> <confidence> meaning {item 1, item 2} => item 3`

### Instructions to run
- Libraries used:
    - itertools combinations, chain 
    - progressbar
- To run the program
    - Either run `main.py` or `run_code.sh`