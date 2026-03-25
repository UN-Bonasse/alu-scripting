#!/usr/bin/python3
"""
2-recurse: Recursively gets all hot posts for a subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=""):
    """Return a list of all hot post titles, or None if invalid subreddit"""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alu.api:v1.0 (by /u/student)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    for post in children:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
