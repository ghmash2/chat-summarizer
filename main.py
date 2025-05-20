from src.analyze_frequency_word import analyze_keywords_frequency
from src.data_loader import parse_chat
from typing import List, Tuple
if __name__ == "__main__":
    file_path = "data/sample.txt"

    data = parse_chat(file_path)
    messages = data['User'] + data['AI']
    print(analyze_keywords_frequency(messages, top_n=5))
    print(data)