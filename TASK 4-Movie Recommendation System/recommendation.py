import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load processed dataset
movies = pd.read_csv("processed_movies.csv")

# Create TF-IDF Vectorizer
tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

# Convert text into vectors
vectors = tfidf.fit_transform(movies["tags"]).toarray()

print("TF-IDF Vector Shape:", vectors.shape)

# Calculate cosine similarity
similarity = cosine_similarity(vectors)

print("Similarity Matrix Shape:", similarity.shape)


# Recommendation Function
def recommend(movie_name):

    movie_name = movie_name.lower()

    movie_list = movies[
        movies["title"].str.lower() == movie_name
    ]

    if movie_list.empty:
        print("\nMovie not found!\n")
        return

    index = movie_list.index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print("\nTop 5 Recommended Movies\n")

    for movie in movie_list:
        print(movies.iloc[movie[0]].title)


# Save files for Streamlit
pickle.dump(movies, open("movies.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("\nModels saved successfully!")

# Sample Test
recommend("Avatar")