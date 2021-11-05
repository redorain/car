# coding: utf-8

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def Tuling(words):
    Tuling_API_KEY = "868060590e26490b84a2487cd8de0879"

    body = {"key": Tuling_API_KEY, "info": words.encode("utf-8")}

    url = "http://www.tuling123.com/openapi/api"
    r = requests.post(url, data=body, verify=True)

    if r:
        date = json.loads(r.text)
        print date["text"]
        return date["text"]
    else:
        return None
