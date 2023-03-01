import http.client
import json
import os
import ssl
import time


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

    job_names = [
       "build",
       "unit-test",
    ]
    
    check_status = True
    while check_status:
        conn = http.client.HTTPSConnection("api.github.com")
        conn.request("GET", "/repos/jdxali/githubActionLearning/actions/runs/" +GITHUB_RUN_ID +"/jobs", None, headers)
        resp = conn.getresponse()
        body = resp.read()
        print(body)
        print(resp.status)
        if resp.status == 200:
            body = resp.read()
            status = json.loads(body)["conclusion"]
            print ("job status")
            print (body)
            print(status)
            if status == "success":
                check_status =False
            time.sleep(5)

_