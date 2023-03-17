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
    GITHUB_JOB = os.environ["GITHUB_JOB"]
    GITHUB_RUN_ID= os.environ["GITHUB_RUN_ID"]
    GIT_EVENT_NAME = os.environ["GITHUB_EVENT_NAME"]

    print (GITHUB_REF)
    print(GIT_EVENT_NAME)
    print (os.environ["GITHUB_REF_NAME"])
    

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
       
    