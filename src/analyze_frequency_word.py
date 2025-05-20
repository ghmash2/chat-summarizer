from collections import Counter
from src.preprocess_text_data import preprocess_text

def analyze_keywords_frequency(messages, top_n=5):
    """
    Analyze messages to find most frequent keywords.
    
    Args:
        messages: List of message strings
        top_n: Number of top keywords to return
        
    Returns:
        List of tuples with (keyword, count) pairs, sorted by frequency
    """
    all_words = []
    for message in messages:
        all_words.extend(preprocess_text(message))
    
    word_counts = Counter(all_words)
    return word_counts.most_common(top_n)