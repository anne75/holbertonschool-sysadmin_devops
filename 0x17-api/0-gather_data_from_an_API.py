#!/usr/bin/python3
"""
Use https://jsonplaceholder.typicode.com/ to request user name and tasks
from given userID
"""
import json
import urllib.request
import sys


def get_user_info(userid):
    """
    Request info to above api

    Arguments:
        userid: a user id
    """
    base_url = "https://jsonplaceholder.typicode.com"
    with urllib.request.urlopen("{}/users/{}".format(
            base_url, userid)) as f:
        html = f.read()
    if html:
        r = json.loads(html.decode('utf-8'))
        name = r.get("name")
        if name is None:
            return
        with urllib.request.urlopen("{}/todos?userId={}".format(
                base_url, userid)) as f:
            html2 = f.read()
        if html2:
            r2 = json.loads(html2.decode('utf-8'))
            completed_tasks = [e for e in r2 if e.get("completed") is True]
            print("Employee {} is done with tasks({:d}/{:d}):".format(
                name, len(completed_tasks), len(r)))
            if completed_tasks:
                print("\t", end="")
                print("\n\t".join(e.get("title") for e in completed_tasks))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_user_info(sys.argv[1])
