#!/usr/local/bin/python
# -*- coding: utf-8 -*

import json
import sys, os
sys.setdefaultencoding('UTF-8')
import site
site.addsitedir('/path/to/site-packages')
from datetime import datetime
import urllib2
import base64

def stripAllLineFeed(line):
    smartline = ""
    for l in line:
        if(l != "\r" and l != "\n" and l != "\r\n"):
            smartline = smartline + l
    return smartline

def saveJson(line):
    a = open("/path/to/text.txt", "a")
    now = datetime.now()
    tweets = json.loads(line)
    print tweets
    for tweet in tweets["results"]:
        uid = tweet["from_user_id"]
        tid = tweet["id"]
        screen_name = tweet["from_user"]
        user_name = tweet["from_user"]
        source = tweet["source"]
        text = tweet["text"]
        created_at = datetime.strptime(tweet["created_at"],"%a, %d %b %Y %H:%M:%S +0000")
        image_url = tweet["profile_image_url"]
        in_reply_to_status_id = tweet["to_user_id"]
        a.write("%s\t'%s\t'%s\t'%s\t'%s\t'%s\t'%s\t'%s\t'%s\n" % (uid, tid, screen_name, user_name, source, text, created_at, image_url, in_reply_to_status_id))
        
    a.close()

def main():
    username = "hoge"
    password = "hogehoge"
    basic = base64.encodestring('%s:%s' % (username, password))[:-1]
    req = urllib2.Request("http://search.twitter.com/search.json?q=%23haiku&rpp=50")
    req.add_header('Authorization', 'Basic %s' % basic)
    res = urllib2.urlopen(req)
    jsonVal = res.read()
    saveJson(jsonVal)

if __name__ == "__main__" : main()