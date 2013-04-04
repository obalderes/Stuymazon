#!usr/bin/python
from pymongo import Connection

global con
con = Connection("mongo.stuycs.org")
global db
global col

def startup():
	global db
	db = con.admin
	global res
	res = db.authenticate("ml7","ml7")
	db = con["stuymazon"]
	global col
	col = db["sales"]



