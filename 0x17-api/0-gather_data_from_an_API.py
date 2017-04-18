#!/usr/bin/python3
"""
Use https://jsonplaceholder.typicode.com/ to request user name and tasks
from given userID
"""
import json
import requests
import sys


def get_user_info(userid):
    """
    Request info to above api

    Arguments:
        userid: a user id
    """
    name = requests.get("{}/users/{}".format(
        base_url, sys.argv[1])).json().get("name")
    if name is None:
        return
    r = requests.get("{}/todos?userId={}".format(
        base_url, sys.argv[1])).json()
    completed_tasks = [e for e in r if e.get("completed") is True]
    print("Employee {} is done with tasks({:d}/{:d}):".format(
        name, len(completed_tasks), len(r)))
    if completed_tasks:
        print("\t", end="")
        print("\n\t".join(e.get("title") for e in completed_tasks))


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    if len(sys.argv) > 1:
        try:
            userid = int(sys.argv[1])
            get_user_info(userid)
        except (ValueError, TypeError):
            pass
