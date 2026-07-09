#!/usr/bin/python3
"""Module that queries the Reddit API for subreddit subscriber counts."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    If the subreddit is invalid, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/UN-Bonasse)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
