from src.preprocess_text_data import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer

def analyze_keywords_tfidf(messages, top_n=5):
    """
    Analyze messages using TF-IDF to find most important keywords.
    
    Args:
        messages: List of message strings
        top_n: Number of top keywords to return
        
    Returns:
        List of tuples with (keyword, TF-IDF score) pairs, sorted by score
    """
    # Preprocess messages
    processed_messages = [
        ' '.join(preprocess_text(message))
        for message in messages
    ]
    
    # Calculate TF-IDF
    vectorizer = TfidfVectorizer(max_features=100)
    tfidf_matrix = vectorizer.fit_transform(processed_messages)
    
    # Get results
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.sum(axis=0).A1
    word_scores = list(zip(feature_names, tfidf_scores))
    word_scores.sort(key=lambda x: x[1], reverse=True)
    
    return word_scores[:top_n]