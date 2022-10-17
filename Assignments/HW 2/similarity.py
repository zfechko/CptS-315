import pandas as pd 
import numpy as np
from numpy.linalg import norm

# Read in the data
ratings = pd.read_csv('ratings.csv').set_index('User')

def jaccard(a: list, b: list):
    """
    Calculates the Jaccard similarity between two lists.
    """
    set_a = set(a)
    set_b = set(b)
    set_a.remove(0) #removing because rating only goes 1-5
    set_b.remove(0)
    union = len(set_a.union(set_b))
    intersection = len(set_a.intersection(set_b))
    print(union, intersection)
    return float(intersection / union)

def cosine(a: list, b: list):
    """
    Calculates the cosine similarity between two lists
    """
    A = np.array(a)
    B = np.array(b)
    return np.dot(A, B) / (norm(A) * norm(B))

def normalize_matrix(matrix: pd.DataFrame):
    """
    Normalizes a matrix by subtracting the mean from each value.
    """
    return matrix.sub(matrix.mean(axis=1), axis=0)

print(jaccard(list(ratings.loc["User 1"]), list(ratings.loc["User 2"])))
