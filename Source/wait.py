import http.client
import json
import os
import ssl
import time
import sys


if __name__ == "__main__":
    #GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
    MY_TOKEN = os.environ["MY_TOKEN"]
    GITHUB_REF = os.environ["GITHUB_REF"]
    GIT_EVENT_NAME = os.environ["GITHUB_EVENT_NAME"]


    x = os.environ["GITHUB_REF_NAME"].split("/")
    print(x[0])

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "token " + MY_TOKEN,
        "User-Agent": "jedox_ag",
    }

    data = { "body" : "new comment" }
    json_data = json.dumps(data)
 
    conn = http.client.HTTPSConnection("api.github.com")
    conn.request("POST", "/repos/jdxali/githubActionLearning/issues/5/comments", json_data, headers) 
    resp = conn.getresponse()
    body = resp.read()
    print(resp.status)
    print(body)
       
    