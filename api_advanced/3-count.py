#!/usr/bin/python3
"""Module that recursively counts keyword occurrences in hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of given keywords found in hot post titles.

    Uses recursion to page through Reddit's pagination.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/UN-Bonasse)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                             allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
    except ValueError:
        return

    posts = data.get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title", "")
        for token in title.split():
            token_lower = token.lower()
            if token_lower in counts:
                counts[token_lower] += 1

    next_after = data.get("after")
    if next_after is not None:
        count_words(subreddit, word_list, next_after, counts)
        return

    results = [(word, cnt) for word, cnt in counts.items() if cnt > 0]
    results.sort(key=lambda item: (-item[1], item[0]))

    for word, cnt in results:
        print("{}: {}".format(word, cnt))
