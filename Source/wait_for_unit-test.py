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
        "User-Agent": "jedox-ag",
    }
 
    check_status = True
    conn = http.client.HTTPSConnection("api.github.com")
    while check_status:
        conn.request("GET", "/repos/jdxali/githubActionLearning/actions/runs/" +GITHUB_RUN_ID +"/jobs", None, headers)
        resp = conn.getresponse()
        body = resp.read()
        print(body)
        if resp.status == 200:
            jobs = json.loads(body)["jobs"]
            for job in jobs:
                if job["name"] == "second job":
                   print (job["status"])
                   if job["conclusion"] == "success":
                      check_status =False
                   if job["conclusion"] == "failure":
                       print("unit test job failed")
                       os._exit(1)
        time.sleep(5)
    
    while (True):
        conn.request("GET", "/repos/jdxali/githubActionLearning/actions/runs/" +GITHUB_RUN_ID +"/artifacts", None, headers)
        resp = conn.getresponse()
        body = resp.read()
        print(body)
        if resp.status == 200:
            artifacts = json.loads(body)["artifacts"]
            if len(artifacts) != 0:
             for artifact in artifacts:
                if artifact["name"] == "file":
                    print (artifact["id"])
                    os.environ["ARTIFACT_ID"] = str(artifact["id"])
                    break