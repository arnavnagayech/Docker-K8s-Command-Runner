#!/usr/bin/python3

import cgi , subprocess

print("content-type: text/html")
print()

a = cgi.FieldStorage()
cmd = a.getvalue("s")

if "kubectl" in cmd:
	o= subprocess.getoutput("sudo "+ cmd)
else:
	o = subprocess.getoutput(cmd)

print(o)