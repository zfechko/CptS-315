"""
Zach Fechko
CptS 315
PA 2: Item-Item Collaborative Filtering
"""

import numpy as np
from itertools import combinations
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Read in the data
movies = pd.read_csv('data/movies.csv')
links = pd.read_csv('data/links.csv')
ratings = pd.read_csv('data/ratings.csv')
tags = pd.read_csv('data/tags.csv')

df = pd.merge(ratings, movies, on='movieId')
movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')
corr_matrix = movie_matrix.corr(method='pearson', min_periods=100)

for i in range(1, 2):
    userratings = movie_matrix.iloc[i].dropna()
    print("Ratings for user " + str(i) + ":")
    print(userratings)
    recommendations = pd.Series()
    for j in range(0, len(userratings)):
        print("Adding recommendations for " + userratings.index[j] + ":")
        similar = corr_matrix[userratings.index[j]].dropna()
        similar = similar.map(lambda x: x * userratings[j])
        recommendations = pd.concat([recommendations, similar])
    
    print("Sorting recommendations:")
    recommendations.sort_values(inplace=True, ascending=False)
    print("User ID: " + str(i))
    print(recommendations.head(10))
    x = pd.DataFrame(recommendations)
    recommendations_filter = x[~x.index.isin(userratings.index)]
    print(recommendations_filter.head(5))
        