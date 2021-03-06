#!/usr/bin/python
from flask import Flask, render_template, session, url_for, redirect, request
import db
import os

app=Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/home",methods=["GET","POST"])
def home():
	pass

@app.route("/userpage",methods=["GET","POST"])
def userpage():
	pass

@app.route("/settings",methods=["GET","POST"])
def settings():
	pass

@app.route("/submit",methods=["GET","POST"])
def submitItem():
	pass

@app.route("/search",methods=["GET","POST"])
def search():
	pass

@app.route("/searchResults",methods=["GET","POST"])
def searchResults():
	pass

@app.route("/about",methods=["GET","POST"])
def about():
	pass

if __name__=="__main__":
    app.debug=True
    db.startup()
    app.run(port=5000)
