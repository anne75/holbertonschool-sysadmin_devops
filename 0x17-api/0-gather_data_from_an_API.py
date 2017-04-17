#!/usr/bin/python3
"""
Use https://jsonplaceholder.typicode.com/ to request user name and tasks
from given userID
"""
import sys
import requests
import json


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    if len(sys.argv) > 1:
        name = requests.get("{}/users/{}".format(
            base_url, sys.argv[1])).json().get("name")
        r = requests.get("{}/todos?userId={}".format(
            base_url, sys.argv[1])).json()
        completed_tasks = [e for e in r if e.get("completed") == True]
        print("Employee {} is done with tasks({:d}/{:d}):".format(
            name, len(completed_tasks), len(r)))
        if completed_tasks:
            print("\t", end = "")
            print("\n\t".join(e.get("title") for e in completed_tasks))
