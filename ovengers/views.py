
from flask import request, jsonify

from flask_login import login_user, login_required, current_user, logout_user

from ovengers import app
from ovengers.models import User
from ovengers.database import db_session


@app.route('/signup/', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    message = '회원가입 실패'
    if username and password:
        user = User(username=username, password=password)
        db_session.add(user)
        db_session.commit()
        message = '회원가입 성공'
    data = {
        'result': message,
    }
    return jsonify(data)

@app.route('/login/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    message = '로그인 실패'
    if username and password:
        user = User.query.filter(
            User.username == username,
            User.password == password,
        ).first()
        if user:
            login_user(user)
            message = '로그인 성공'
    data = {
        'result': message,
    }
    return jsonify(data)

@app.route('/step/', methods=['GET','PATCH'])
@login_required
def step():
    if request.method == 'PATCH':
        step = request.form['step']
        current_user.step = step
        db_session.add(current_user)
        db_session.commit()
    data = {
        'step': current_user.step,
    }
    return jsonify(data)

@app.route('/heart-rate/', methods=['GET','PATCH'])
@login_required
def heart_rate():
    if request.method == 'PATCH':
        heart_rate = request.form['heart_rate']
        current_user.heart_rate = heart_rate
        db_session.add(current_user)
        db_session.commit()
    data = {
        'heart_rate': current_user.heart_rate,
    }
    return jsonify(data)

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    message = '로그아웃 성공'
    data = {
        'result': message,
    }
    return jsonify(data)
