#!/usr/bin/python3
"""
Counts keyword occurrences in hot post titles
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursive word count."""
    if counts is None:
        counts = {}

    word_list = [w.lower() for w in word_list]

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-Project"}
    params = {"after": after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for item in posts:
            title = item.get("data", {}).get("title", "").lower().split()

            for word in word_list:
                counts[word] = counts.get(word, 0) + title.count(word)

        next_after = data.get("after")
        if next_after:
            return count_words(subreddit, word_list, next_after, counts)

        final = {w: c for w, c in counts.items() if c > 0}

        for word, count in sorted(final.items(),
                                  key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(word, count))

    except Exception:
        return
