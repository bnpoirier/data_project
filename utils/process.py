from sklearn.preprocessing import StandardScaler
from unidecode import unidecode as undcd
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

characters_to_remove = [
    ")",
    "(",
    ",",
    ";",
    ":",
    "+",
    "&"
]

french_stopwords = stopwords.words('french') + characters_to_remove
stemmer = SnowballStemmer('french')

# Converts string to categorical numbers
def categorize(column):
    column = column.astype('category')
    column = column.cat.reorder_categories(column.unique(), ordered=True)
    column = column.cat.codes

    return column

# Apply normalization to specific columns
def scale(df):
    scaler = StandardScaler()
    return scaler.fit_transform(df)

# Tokenize string
def tokenize(df):
    return df.apply(word_tokenize)

# Unidecode
def unidecode(df):
    return df.apply(undcd)

# Stemming
def stem(df):
    return df.apply(lambda row: [stemmer.stem(words) for words in row])

# Stop pointless words
def stop_words(df):
    return df.apply(lambda row: [word for word in row if word not in french_stopwords and len(word) > 1])

