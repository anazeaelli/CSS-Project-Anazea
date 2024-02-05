# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:05:54 2024

@author: User
"""

import pandas
file = pandas.read_csv("movie_dataset.csv")
print(file)
print(file.info())

import pandas as pd

file_path = 'movie_dataset.csv'
df = pd.read_csv(file_path)  # Use read_csv for CSV files
fill_value = 0
df.fillna(fill_value, inplace=True)
df.to_csv(file_path, index=False)
target_column = 'Revenue (Millions)'
column_average = df[target_column].mean()

filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

movies_in_2016 = df[df['Year'] == 2016]
number_of_movies_in_2016 = len(movies_in_2016)

nolan_movies = df[df['Director'].str.contains('Christopher Nolan', case=False, na=False)]
number_of_nolan_movies = len(nolan_movies)
print("Number of movies directed by Christopher Nolan:", number_of_nolan_movies)

high_rated_movies = df[df['Rating'] >= 8.0]
number_of_high_rated_movies = len(high_rated_movies)

nolan_movies = df[df['Director'].str.contains('Christopher Nolan', case=False, na=False)]
median_rating_nolan_movies = nolan_movies['Rating'].median()

print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan_movies)

average_rating_by_year = df.groupby('Year')['Rating'].mean()
year_highest_average_rating = average_rating_by_year.idxmax()

print("Year with the highest average rating:", year_highest_average_rating)

movies_2006_to_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]
movies_count_2006 = len(df[df['Year'] == 2006])
movies_count_2016 = len(df[df['Year'] == 2016])
percentage_increase = ((movies_count_2016 - movies_count_2006) / movies_count_2006) * 100

print("Percentage increase in number of movies made between 2006 and 2016:", percentage_increase)

all_actors = df['Actors'].str.split(', ', expand=True).stack()
most_common_actor = all_actors.mode().iloc[0]

print("Most common actor in all the movies:", most_common_actor)

all_genres = df['Genre'].str.split(', ', expand=True).stack()

unique_genres_count = len(all_genres.unique())

print("Number of unique genres in the dataset:", unique_genres_count)

all_genres = df['Genre'].str.split(', ')

# Create a list of unique genres
unique_genres = set(genre for genres_list in all_genres.dropna() for genre in genres_list)

print("List of unique genres:", unique_genres)
print("Number of unique genres:", len(unique_genres))
all_genres = df['Genre'].str.split(', ', expand=True).stack()
unique_genres_count = len(all_genres.unique())

print("Number of unique genres in the dataset:", unique_genres_count)

genres_df = df['Genre'].str.split(',').explode()
unique_genres_count = genres_df.nunique()
unique_genres_list = genres_df.unique()

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numerical_columns].corr()
print("Correlation Matrix:")
print(correlation_matrix)




