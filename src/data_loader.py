from typing import Dict, List, Tuple
import re


def parse_chat(file_path):
   
    chat_data = {'User': [], 'AI': []}
    current_speaker = None
    current_message = []
    with open(file_path, "r") as file:
         for line in file:
            line = line.strip()
            if not line:
                continue
    
    
            # Check if the line starts with a speaker label
            match = re.match(r'^(User|AI):\s*(.*)', line, re.IGNORECASE)
            if match:
                # Save the previous message if any
                if current_speaker and current_message:
                    chat_data[current_speaker].append(' '.join(current_message))

                current_speaker = match.group(1)
                message = match.group(2).strip()
                current_message = [message] if message else []
            else:
                # Line is a continuation of the previous message
                if current_speaker:
                    current_message.append(line)

            # Append the last message
            if current_speaker and current_message:
                chat_data[current_speaker].append(' '.join(current_message))

    return chat_data


