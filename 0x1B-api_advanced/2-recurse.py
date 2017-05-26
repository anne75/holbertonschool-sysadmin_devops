#!/usr/bin/python3
"""
recurse a request, poor api
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    entry point for the recursion
    """
    url = "https://www.reddit.com/r/{}.json?limit=100".format(subreddit)
    h = requests.utils.default_headers()
    headers = {'User-Agent': "ubuntu:noredditapp (by /u/noone)'"}
    h.update(headers)
    return (helper(url, h, "start"))


def helper(url, headers, after, hot_list=[]):
    """
    the recursion
    """
    base_url = url
    if after != "start":
        url += "&after={}".format(after)
    r = requests.get(url, headers=headers, allow_redirect=False)
    if r.status_code != 200:
        return None
    for value in r.json()['data'].get('children', []):
        hot_list.append(value['data']['title'])
    after = r['data'].get('after')
    if not after:
        return hot_list
    return (helper(base_url, headers, after, hot_list))
