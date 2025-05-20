import string
from typing import List, Tuple
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# Initialize NLTK components once
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
punctuation = string.punctuation + '’‘”“`'


def preprocess_text(text):
    """
    Clean and tokenize text for analysis.
    
    Args:
        text: Input text string
        
    Returns:
        List of cleaned and tokenized words
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', punctuation))
    
    # Tokenize using NLTK
    tokens = word_tokenize(text)
    
    # Lemmatize and filter
    words = [
        lemmatizer.lemmatize(token) 
        for token in tokens 
        if token not in stop_words and len(token) > 2 and token.isalpha()
    ]
    
    return words