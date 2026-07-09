import pandas as pd
import ast

# Load datasets
movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

# Merge datasets
movies = movies.merge(credits, on="title")

# Select required columns
movies = movies[
    [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew"
    ]
]

# Remove missing values
movies.dropna(inplace=True)


# Convert JSON-like string to list of names
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i["name"])
    return L


# Extract top 3 cast members
def convert_cast(text):
    L = []
    counter = 0

    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i["name"])
            counter += 1
        else:
            break

    return L


# Extract director name
def fetch_director(text):
    L = []

    for i in ast.literal_eval(text):
        if i["job"] == "Director":
            L.append(i["name"])
            break

    return L


# Apply transformations
movies["genres"] = movies["genres"].apply(convert)
movies["keywords"] = movies["keywords"].apply(convert)
movies["cast"] = movies["cast"].apply(convert_cast)
movies["crew"] = movies["crew"].apply(fetch_director)

# Convert overview into words
movies["overview"] = movies["overview"].apply(lambda x: x.split())

# Remove spaces
movies["genres"] = movies["genres"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["keywords"] = movies["keywords"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["cast"] = movies["cast"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["crew"] = movies["crew"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

# Create tags column
movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)

# Keep only title and tags
new_df = movies[["movie_id", "title", "tags"]]

# Convert list into string
new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))

# Lowercase
new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())

# Save cleaned dataset
new_df.to_csv("cleaned_movies.csv", index=False)

print("✅ Data cleaning completed successfully!")
print(new_df.head())