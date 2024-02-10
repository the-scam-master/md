# streamlit_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity

# Load the MovieLens dataset
movies_url = 'https://raw.githubusercontent.com/tanmay-kalbande/Movie-Recommendation-System/main/MovieLens%20dataset/movies.csv'
ratings_url = 'https://raw.githubusercontent.com/tanmay-kalbande/Movie-Recommendation-System/main/MovieLens%20dataset/ratings.csv'

movies = pd.read_csv(movies_url)
ratings = pd.read_csv(ratings_url)

# Data Cleaning and Manipulation
movies = movies.drop(['genres'], axis=1)
movie_data = pd.merge(ratings, movies, on='movieId')

# Collaborative Filtering
user_movie_matrix = movie_data.pivot_table(index='userId', columns='title', values='rating')
user_movie_matrix = user_movie_matrix.fillna(0)
movie_similarity = cosine_similarity(user_movie_matrix.T)
movie_similarity_df = pd.DataFrame(movie_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# Streamlit App
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon=":movie_camera:",
    layout="wide"
)

# Title and Introduction
st.title("Movie Recommendation System")
st.write("Welcome to our movie recommendation system. Discover exciting movies that match your preferences!")

# Introduction
st.markdown("## Introduction")
st.write("This recommendation system uses collaborative filtering to provide personalized movie recommendations based on user preferences.")

# Sidebar with movie selection
st.sidebar.title("Movie Selection")
selected_movie = st.sidebar.text_input("Enter the title of a movie:", "Toy Story (1995)")

# Number of Recommendations
num_recommendations = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# Recommendation Function
def recommend_movies(movie_title, top_n=5):
    similar_movies = movie_similarity_df[movie_title].sort_values(ascending=False)
    similar_movies = similar_movies.drop(movie_title)
    top_similar_movies = similar_movies.head(top_n)
    return top_similar_movies.index

# Display Recommendations
recommended_movies = recommend_movies(selected_movie, num_recommendations)
st.subheader("Recommended Movies:")
for movie in recommended_movies:
    st.write(f"- {movie}")

# Explanation
st.markdown("## How It Works")
st.write("Our recommendation system analyzes user ratings to identify movies similar to the one you selected. "
         "The results are based on collaborative filtering, which leverages the preferences of users with similar taste.")