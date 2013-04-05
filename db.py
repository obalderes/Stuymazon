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

def drop():
	global col
	col.drop()

def userexists(username = ""):
	username = str(username)
	global col
	res = [x for x in col.find({"entry":"user","user":username})]
	if len(res) == 0:
		return False
	return True

def authuser(username="", password=""):
	username = str(username)
	password = str(password)
	global col
	res = [x for x in col.find({"entry":"user","user":username, "password":password})]#entries in the db can be user, items, etc
	if len(res) == 0:
		return False
	return True

def newuser(username="", password=""):
	username = str(username)
	password = str(password)
	global col
	nuser = {"entry":"user","user":username, "password":password}
	res = [x for x in col.find(nuser)]#entries in the db can be user, items, etc
	if len(res) > 0 or username == "" or password == "":
		return False
	col.insert(nuser)
	return True

def deleteuser(username="", password=""):
	username = str(username)
	password = str(password)
	global col
	nuser = {"entry":"user","user":username, "password":password}
	res = [x for x in col.find(nuser)]#entries in the db can be user, items, etc
	if len(res) == 0 or username == "" or password == "":
		return False
	col.remove(nuser)
	return True

def newsale(itemname="",description="",seller="",startprice=0):#need pic
	seller = str(seller)
	description = str(description)
	startprice = float(startprice)
	itemname = str(itemname)
	if seller == "" or itemname == "" or userexists(seller) == False:
		return False
	global col
	item = {"entry":"sale","user":seller,"description":description,"item":itemname, "pricehistory":[startprice],"highestbidder":seller}
	num = 1 + len([x for x in col.find({"entry":"sale","user":seller,"item":itemname})])
	item["number"] = num 
	print [item[x] for x in item.keys()]
	col.insert(item)
	return len([x for x in col.find({"entry":"sale","user":seller,"item":itemname})])

def bidonsale(itemname="",seller = "", bidder="",bid = -1, number = -1):
	seller = str(seller)
	bidder = str(bidder)
	bid = float(bid)
	number = int(number)
	itemname = str(itemname)#db.bidonsale("boot","name","name2",200,1)
	if bid < 0 or number < 0 or seller == "" or itemname == "" or bidder == "" or userexists(seller) == False or userexists(bidder) == False:
		return False
	item = {"number":number, "entry":"sale","user":seller,"item":itemname}
	l =  [x[unicode("pricehistory")] for x in col.find(item)]
	print l[len(l) - 1]
	if len(l) == 1 and (l[0][len(l) - 1] < bid): 	
		l.append(bid)
		col.update(item, {"$set": {"highestbidder":bidder,"pricehistory":l}})
		print list(col.find())
		return True
	return False

def sold():
	pass

def newpurchaseoffer():#need pic
	pass

def search():
	pass
