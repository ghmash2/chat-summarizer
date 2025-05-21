import argparse
import os
from pathlib import Path
from src.analyze_frequency_word import analyze_keywords_frequency
from src.analyze_tfidf_word import analyze_keywords_tfidf
from src.data_loader import parse_chat
from typing import List, Tuple
from src.generate_summary import generate_summary

if __name__ == "__main__":
    #file_path = "data/sample.txt"
    # Set up argument parser
    parser = argparse.ArgumentParser(description='AI Chat Log Summarizer')
    parser.add_argument('input_path', help='Path to the chat log file (e.g., data/sample.txt)')
    args = parser.parse_args()
    #path = os.path.normpath(args.path)
    input_path = Path(args.input_path).resolve()
    
    if os.path.isfile(args.input_path):
        try:
            data = parse_chat(args.input_path)
            messages = data['User'] + data['AI']

            frequency_based_word = analyze_keywords_frequency(messages, top_n=5)
            tfidf_based_word = analyze_keywords_tfidf(messages, top_n=5)
            summary = generate_summary(data, frequency_based_word, tfidf_based_word)
            print(summary)

        except FileNotFoundError:
            print(f"Error: File not found at {args.input_path}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    elif os.path.isdir(args.input_path):  
        txt_files = list(input_path.glob('*.txt')) + list(input_path.glob('*.TXT'))
        for filename in txt_files:
                try:
                    print(f"\nAnalyzing {filename.name}:")
                    print("=" * 50)
                    data = parse_chat(filename)
                    messages = data['User'] + data['AI']

                    frequency_based_word = analyze_keywords_frequency(messages, top_n=5)
                    tfidf_based_word = analyze_keywords_tfidf(messages, top_n=5)
                    summary = generate_summary(data, frequency_based_word, tfidf_based_word)
                    print(summary)

                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
    else:
        print(f"Error: The path {args.path} does not exist.")