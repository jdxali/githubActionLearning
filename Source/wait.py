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

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "token " + MY_TOKEN,
        "User-Agent": "jedox_ag",
        "body" : "Great stuff!",
    }
 
    conn = http.client.HTTPSConnection("api.github.com")
    conn.request("POST", "/repos/jdxali/githubActionLearning/issues/1627522244/comments", None, headers)
    resp = conn.getresponse()
    body = resp.read()
    print(body)
       
    