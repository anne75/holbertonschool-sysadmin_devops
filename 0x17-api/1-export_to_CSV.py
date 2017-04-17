#!/usr/bin/python3
"""
Use https://jsonplaceholder.typicode.com/ to request user name and tasks
from given userID
then export data as csv format
"""
import sys
import requests
import csv


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    if len(sys.argv) > 1:
        name = requests.get("{}/{}".format(
            base_url, sys.argv[1])).json().get("username")
        r = requests.get("{}/{}/todos".format(
            base_url, sys.argv[1])).json()
        with open ("{}.csv".format(sys.argv[1]), mode="w", newline="") as f:
            csvwriter = csv.writer(f, delimiter=",",
                                   quotechar='"', quoting=csv.QUOTE_ALL)
            csvwriter.writerows([sys.argv[1], name,
                                 e.get("completed"),
                                 e.get("title")] for e in r)
