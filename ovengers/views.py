from flask import request, jsonify, Response

from flask_login import login_user

from ovengers import app
from ovengers.models import User
from ovengers.database import db_session


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/signup/', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    if username and password:
        user = User(username=username, password=password)
        db_session.add(user)
        db_session.commit()
        return Response(status=200)
    return Response(status=400)

@app.route('/login/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username and password:
        user = User.query.filter(
            User.username == username,
            User.password == password,
        ).first() 
        if user:
            login_user(user)
            return Response(status=200)
    return Response(status=400)
