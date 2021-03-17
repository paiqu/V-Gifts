'''
    This file includes all functions can be directly called 
    by frontend
'''

import database as db
import user as usr
import admin as adm
import webpage as wbp
import SAMPLE_DB as samp
import login as login

from logging import DEBUG
from flask import Flask, request
from flask_cors import CORS
from error import InputError, AccessError
from json import dumps

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

app = Flask(__name__)
CORS(app)
app.config.update(
    DEBUG = True, ## remeber to change later
    TESTING = True,
    TRAP_HTTP_EXCEPTIONS = True
)
app.register_error_handler(Exception, defaultHandler)

@app.route("/user/register", methods = ["POST"])
def usr_register():
    data = request.get_json
    name = data['name']
    password = data['password']
    email = data['email']
    address = data['address']
    try:
        result = login.register_user(name, password, email)
    except InputError:
        raise InputError()
    return dumps({
        'id': result['id'],
        'name': result['name'],
        'email': result['email']
    })

@app.route("/admin/register", methods = ["POST"])
def adm_register():
    data = request.get_json
    name = data['name']
    password = data['password']
    email = data['email']
    try:
        result = login.register_admin(name, password, email)
    except InputError:
        raise InputError()
    return dumps({
        'id': result['id'],
        'name': result['name'],
        'email': result['email']
    })


@app.route("/user/login", methods = ["POST"])
def usr_login():
    data = request.get_json
    name = data['name']
    password = data['password']
    try:
        result = login.login_user(name, password)
    except InputError:
        raise InputError()
    return dumps({
        'token': result
    })

@app.route("/admin/login", methods = ["POST"])
def adm_login():
    data = request.get_json
    name = data['name']
    password = data['password']
    try:
        result = login.login_admin(name, password)
    except InputError:
        raise InputError()
    return dumps({
        'token': result
    })

@app.route("/user/logout", methods = ["POST"])
def usr_logout():
    data = request.get_json
    name = data['name']
    result = login.logout_user(name)
    return dumps({
        'is_success': result
    })

@app.route("/admin/logout", methods = ["POST"])
def adm_logout():
    data = request.get_json
    name = data['name']
    result = login.logout_admin(name)
    return dumps({
        'is_success': result
    })
