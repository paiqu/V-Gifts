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

##########################
# admin related routes
##########################

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

@app.route("/admin/logout", methods = ["POST"])
def adm_logout():
    data = request.get_json
    name = data['name']
    result = login.logout_admin(name)
    return dumps({
        'is_success': result
    })

@app.rounte("/admin/profile/edit", methods = ["POST"])
def adm_edit():
    data = request.get_json
    aid = data['admin_id']
    name = data['name']
    password = data['password']
    email = data['email']
    result = adm.edit_admin(aid, name, password, email)
    return dumps({
        'id': result['id']
    })

@app.route("/admin/product/new", methods = ["POST"])
def new_product():
    data = request.get_json
    name = data['name']
    price = data['price']
    description = data['description']
    feature = data['feature']
    deli_days = data['deli_days']
    result = adm.new_product(name, price, description, feature, deli_days)
    db.add_prod(result)
    return dumps({
        'id': result['id']
    })

@app.route("/admin/product/edit", methods = ["POST"])
def edit_product():
    data = request.get_json
    id = data['id']
    name = data['name']
    feature = data['feature']
    description = data['description']
    result = adm.edit_product(id, name, feature, description)
    return dumps({
        'id': result['id']
    })

# @app.route("/admin/product/editfeature")

@app.route("admin/product/delete", methods = ["POST"])
def delete_product():
    data = request.get_json
    id = data['id']
    result = adm.delete_product(id)
    return dumps({
        'status': "success"
    })

@app.route("admin/order/statechange", methods = ["POST"])
def order_state_change():
    data = request.get_json
    id = data['id']
    state = data['state']
    result = adm.change_order_state(id, state)
    return dumps({
        'status': "success",
        'id': result['id'],
        'state': result['state']
    })

##########################
# user side routes
##########################

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

@app.route("/user/logout", methods = ["POST"])
def usr_logout():
    data = request.get_json
    name = data['name']
    result = login.logout_user(name)
    return dumps({
        'is_success': result
    })

@app.route("user/profile/fund/add", methods = ["POST"])
def add_fund():
    data = request.get_json
    uid = data['u_id']
    num = data['num']
    result = usr.add_fund(uid, num)
    return dumps({
        'status': "success"
    })

# @app.route("user/profile/password/forget")

@app.route("user/profile/password/change", methods = ["POST"])
def change_password():
    data = request.get_json
    uname = data['name']
    opassword = data['old_password']
    result = usr.change_password(uname, opassword)
    return dumps({
        'status': result
    })

# @app.rounte("user/profile/edit")

@app.route("user/order/new", methods = ["POST"])
def create_order():
    data = request.get_json
    uid = data['user_id']
    pid = data['product_id']
    amount = data['amount']
    result = usr.create_order(uid, pid, amount)
    return dumps({})
