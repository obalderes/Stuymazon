#!usr/bin/python
from pymongo import Connection

global con
con = Connection("mongo2.stuycs.org")
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

def authuser(username="", password=""):
	global col
	res = [x for x in col.find({"entry":"user","user":username, "password":password})]#entries in the db can be user, items, etc
	if len(res) == 0:
		return False
	return True

def newuser(username="", password=""):
	global col
	nuser = {"entry":"user","user":str(username), "password":str(password)}
	res = [x for x in col.find(nuser)]#entries in the db can be user, items, etc
	if len(res) > 0 or username == "" or password == "":
		return False
	col.insert(nuser)
	return True

def deleteuser(username="", password=""):
	global col
	nuser = {"entry":"user","user":str(username), "password":str(password)}
	res = [x for x in col.find(nuser)]#entries in the db can be user, items, etc
	if len(res) == 0 or username == "" or password == "":
		return False
	col.remove(nuser)
	return True


