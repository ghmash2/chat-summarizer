from typing import Dict, List, Tuple
import re


def parse_chat(text):
    lines = text.splitlines()
    result = []
    current_speaker = None
    current_message = []

    for line in lines:
        if ':' in line:
            speaker, message_part = line.split(':', 1)
            speaker = speaker.strip()
            message_part = message_part.strip()

            # Save previous message
            if current_speaker is not None:
                result.append((current_speaker, ' '.join(current_message)))

            # Start new message
            current_speaker = speaker
            current_message = [message_part]
        else:
            # Continuation of current message
            current_message.append(line.strip())

    # Append the last message
    if current_speaker and current_message:
        result.append((current_speaker, ' '.join(current_message)))

    return result


