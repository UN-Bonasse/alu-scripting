#!/usr/bin/python3
"""
Prints titles of first 10 hot posts
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "python:alu.api:v1.0 (by /u/student)"
    }

    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data").get("title"))
