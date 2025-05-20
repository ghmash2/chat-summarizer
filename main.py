from src.analyze_frequency_word import analyze_keywords_frequency
from src.analyze_tfidf_word import analyze_keywords_tfidf
from src.data_loader import parse_chat
from typing import List, Tuple

from src.generate_summary import generate_summary
if __name__ == "__main__":
    file_path = "data/sample.txt"
    try:
        data = parse_chat(file_path)
        messages = data['User'] + data['AI']
        
        frequency_based_word = analyze_keywords_frequency(messages, top_n=5)
        tfidf_based_word = analyze_keywords_tfidf(messages, top_n=5)
        summary = generate_summary(data, frequency_based_word, tfidf_based_word)
        print(summary)
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")