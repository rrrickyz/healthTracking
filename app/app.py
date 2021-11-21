from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config("SQLALCHEMY_DATABASE_URI") = "postgresql:///user"
db = SQLAlchemy(app)


