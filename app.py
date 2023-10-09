import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    # Find the index of the input movie in the 'movies' DataFrame
    movie_index = movies[movies['title'] == movie].index[0]

    # Get the similarity scores for the input movie
    distances = similarity[movie_index]

    # Combine movie indices and similarity scores into a list of tuples
    movies_list = list(enumerate(distances))

    # Sort movies_list based on similarity scores (descending order)
    sorted_movies = sorted(movies_list, key=lambda x: x[1], reverse=True)
    sorted_movies = sorted_movies[1:6]

    # Extract the titles of the recommended movies
    recommend_movies = [movies.iloc[i[0]].title for i in sorted_movies]

    return recommend_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Which movie would you like to see?',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
