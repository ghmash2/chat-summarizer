def generate_summary(chat_data, freq_keywords, tfidf_keywords):
    """
    Generate a comprehensive summary of the chat log analysis.
    
    Args:
        chat_data: Parsed chat data dictionary
        freq_keywords: Frequency-based keywords
        tfidf_keywords: TF-IDF based keywords
        
    Returns:
        Formatted summary string
    """
    # Message statistics
    user_count = len(chat_data['User'])
    ai_count = len(chat_data['AI'])
    total_exchanges = user_count + ai_count
    
    # Generate summary parts
    summary_parts = [
        '\n',"Summary:",
        f"- The conversation had {total_exchanges} exchanges.",
    ]
    """
    # Frequency keywords
    if freq_keywords:
        freq_kw_str = ', '.join([f"{word} ({count})" for word, count in freq_keywords])
        summary_parts.append(f"- Most frequent keywords: {freq_kw_str}")
    """
     # Conversation topics
    if tfidf_keywords:
        main_topics = [word for word, score in tfidf_keywords[:2]]
        summary_parts.append(f"- The User mainly asked about {main_topics[1]} and its {main_topics[0]}s")
    
    # TF-IDF keywords
    if tfidf_keywords:
        tfidf_kw_str = ', '.join([f"{word}" for word, score in tfidf_keywords])
        summary_parts.append(f"- Most Common keywords: {tfidf_kw_str}")
    
   
    return '\n'.join(summary_parts)