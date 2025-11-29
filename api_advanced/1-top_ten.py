#!/usr/bin/python3
"""
Prints titles of first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Print top 10 hot posts or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-Project"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
