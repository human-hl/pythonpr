from flask import Flask, render_template
# , request, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import mysql.connector
app = Flask(__name__)
mysql = MySQL(app)
app.secret_key = 'key'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'LOGIN'
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Users.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/')
def glav():
    return render_template('glav.html')

@app.route('/karta')
def about():
    return render_template('karta.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/user')
def user():
    return render_template('user.html')
app.run()
