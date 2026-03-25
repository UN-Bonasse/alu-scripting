#!/usr/bin/python3
"""
Counts occurrences of keywords recursively in hot post titles
"""
from 2-recurse import recurse

def count_words(subreddit, word_list):
    """
    Recursively count keywords in hot posts of a subreddit.
    Prints counts in descending order, alphabetically for ties.
    """
    if not subreddit or not word_list:
        return

    hot_titles = recurse(subreddit)
    if hot_titles is None:
        return

    # Normalize keywords to lowercase
    keywords = [w.lower() for w in word_list]
    counts = {}

    # Count occurrences
    for title in hot_titles:
        words_in_title = title.lower().split()
        for k in keywords:
            counts[k] = counts.get(k, 0) + words_in_title.count(k)

    # Filter out keywords with 0 count
    counts = {k: v for k, v in counts.items() if v > 0}

    # Sort: descending count, then alphabetically
    for k, v in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{k}: {v}")
