#!/usr/bin/env python
#coding:utf8
import json
import base64
import urllib2
from sys import argv

marathon_address = argv[1]
marathon_app = argv[2]

username = ''
password = ''

request = urllib2.Request(marathon_address + marathon_app)
base64string = base64.b64encode('%s:%s' % (username, password))
request.add_header("Authorization", "Basic %s" % base64string)
html = urllib2.urlopen(request)

hjson = json.loads(html.read())
args = hjson['app']['instances']

print args
