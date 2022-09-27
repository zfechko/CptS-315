# PA 2: Movie Reccomendations via Item-Item Collaborative Filtering

## Instructions
You are provided with real-data (Movie-Lens dataset) of user ratings for different movies. There is a readme file that describes the data format. In this project you will implement the *item-item collaborative filtering* algorithm that we discussed in lecture. The high-level steps are as follows  

a. Construct the profile of each item (i.e. movie). At the minimum you should use the ratings given by each user for a given item. Optionally, you can use other information (e.g. genre information for each movie and tag information given by the user for each movie) creatively. If you used this additional information, you should explain your methodology in the submitted report

b. Compute similarity score for all item-item (movie-movie) pairs. You will use the *centered cosine* similarity metric that we discussed in class.

c. Comput the neighborhood set $N$ for each item. You will select the movies that have the highest similarity score for the given movie. Use a neighborhood of size $5$. Break ties using lexicographic ordering over movie-IDs.

d. Estimate the ratings of other users who didn't rate this item using the neighborhood set. Repeat for each item

e. Compute the recommended items for each user. Pick the top 5 movies with highest setimated ratings. Break ties using lexicographic ordering over movie IDs

Your prograpm should output top 5 recommendations for each user.

### Output
- The output of your program should be dumped in a file named `output.txt` in the following format. One line for each user
```
1 2938 1356 1 2 3
2 708 237 1554 2696 805
3 590 587 150 2478 648
4 4453 595 6170 780 1517
5 539 1517 6333 587 3988
...
671 8360 7153 6377 6539 1210
```
- Line 1 should have the first user-id followed by the movie IDs of recommended movies.
- Line 2 should have the second user-id followed by the movie IDs of recommended movies
- Repeat for each user in the dataset