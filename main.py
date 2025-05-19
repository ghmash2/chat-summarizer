from src.data_loader import parse_chat
from typing import List, Tuple

def parse_file(file_path: str) -> List[Tuple[str, str]]:

    with open(file_path, "r") as file:
        chat_text = file.read()
    
    return parse_chat(chat_text)


if __name__ == "__main__":
    file_path = "data/sample.txt"
    parsed_chat = parse_file(file_path)
    
    for speaker, message in parsed_chat:
        print(f"{speaker}: {message}")