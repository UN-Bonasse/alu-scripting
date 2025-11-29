#!/usr/bin/python3
"""
Recursive function to get all hot post titles
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return list of all hot post titles recursively."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Student-Project"}
    params = {"after": after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            hot_list.append(post.get("data", {}).get("title"))

        next_after = data.get("after")
        if next_after is not None:
            return recurse(subreddit, hot_list, next_after)

        return hot_list

    except Exception:
        return None
