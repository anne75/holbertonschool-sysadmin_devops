#!/usr/bin/python3
"""
Use https://jsonplaceholder.typicode.com/ to request all users and their tasks
Then export data as json format
Pushing comprehension to the unreadable
"""
import requests
import json


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(base_url).json()
    with open("todo_all_employees.json", mode="w", newline="") as f:
        json.dump(
            {user.get("id"): [
                {"task": e.get("title"), "completed": e.get("completed"),
                 "username": user.get("username")} for e in \
                 requests.get("{}/{}/todos".format(
                     base_url, user.get("id"))).json()] for user in users}, f)
