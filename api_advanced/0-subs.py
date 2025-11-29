#!/usr/bin/python3
"""
Returns number of subscribers for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Return subscriber count or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-Project"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0

        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
