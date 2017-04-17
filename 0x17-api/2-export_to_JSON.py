#!/usr/bin/python3
"""
Use https://jsonplaceholder.typicode.com/ to request user name and tasks
from given userID
Then export data as json format
"""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    if len(sys.argv) > 1:
        name = requests.get("{}/{}".format(
            base_url, sys.argv[1])).json().get("username")
        r = requests.get("{}/{}/todos".format(
            base_url, sys.argv[1])).json()
        with open("{}.json".format(sys.argv[1]), mode="w", newline="") as f:
            json.dump({sys.argv[1]: [
                {"task": e.get("title"), "completed": e.get("completed"),
                 "username": name} for e in r]}, f)
