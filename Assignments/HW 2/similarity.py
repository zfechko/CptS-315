import pandas as pd 
import numpy as np
from numpy.linalg import norm

# Read in the data
ratings = pd.read_csv('ratings.csv').set_index('User')

def jaccard(a, b):
    """
    Calculates the Jaccard similarity between two lists.
    """
    a = set(a)
    b = set(b)
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

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

print(ratings.sub(1, axis=0))

