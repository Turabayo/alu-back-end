#!/usr/bin/python3
"""get TODO list"""

import json
import requests
import sys
if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    res = requests.get(link)
    user = json.loads(res.text)
    num = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/users/{}/todos".format(num)
    res = requests.get(link)
    todos = json.loads(res.text)
    done = []
    for x in todos:
        if x['completed']:
            done.append(x)
    print("Employee {} is done with tasks({}/{}):".format(
                                                          user['name'],
                                                          len(done),
                                                          len(todos)))
    for x in done:
        print("\t {}".format(x["title"]))
