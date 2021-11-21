from app import app
from flask import render_template, request
import users

#the defualt page
@app.route("/")
def index():
  return render_template("index.html")

#page for login
@app.route("/login")
def login():
  username = request.form['username']
  password = request.form['password']
  if users.login(username,password):
    return redirect("/feed")
  else:
    return render_template("error.html",message="Incorrect username or password. Please try again.")


@app.route("/register", methods=["POST"])
def register():
return redirect("/")


@app.route("/feed")
def feed(id):
  return render_template("feed.html")

@app.route("/diet")

@app.route("/exercise")
