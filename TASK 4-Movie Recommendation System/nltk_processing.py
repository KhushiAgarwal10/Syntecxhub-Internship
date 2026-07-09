import pandas as pd
from nltk.stem.porter import PorterStemmer
import nltk

# Download NLTK resources (only first time)
nltk.download('punkt')

# Load cleaned dataset
movies = pd.read_csv("cleaned_movies.csv")

# Initialize stemmer
ps = PorterStemmer()

# Stemming function
def stem(text):
    words = text.split()
    stemmed_words = []

    for word in words:
        stemmed_words.append(ps.stem(word))

    return " ".join(stemmed_words)

# Apply stemming
movies["tags"] = movies["tags"].apply(stem)

# Save processed dataset
movies.to_csv("processed_movies.csv", index=False)

print("✅ NLTK preprocessing completed successfully!")
print(movies.head())