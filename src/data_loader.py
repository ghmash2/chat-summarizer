from typing import Dict, List, Tuple
import re

def parse_chat(file_path: str) -> Dict[str, List[str]]:
        """
        Parse the chat  file and separate messages by speaker.
        
        Args:
            file_path: Path to the chat .txt file
            
        Returns:
            Dictionary with keys 'User' and 'AI' containing lists of their messages
        """
        chat_data = {'User': [], 'AI': []}
        
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                    
                # Match speaker and message
                match = re.match(r'^(User|AI):\s*(.*)', line, re.IGNORECASE)

                if match:
                    speaker = match.group(1)
                
                    message = match.group(2).strip()
                    if message:
                        chat_data[speaker].append(message)
        
        return chat_data


