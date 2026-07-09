import streamlit as st
import pickle

# Load Data

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Recommendation Function

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



# Streamlit UI

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommendation System")

st.write(
    "Get movie recommendations based on content similarity using "
    "TF-IDF and Cosine Similarity."
)

selected_movie = st.selectbox(
    "Select a Movie",
    movies['title'].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.success("Top 5 Recommended Movies")

    for movie in recommendations:
        st.write("⭐", movie)