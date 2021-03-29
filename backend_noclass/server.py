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
import error as err

from logging import DEBUG
from flask import Flask, request
from flask_cors import CORS
from json import dumps
import sys

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
    # DEBUG = True, ## remeber to change later
    # TESTING = True,
    TRAP_HTTP_EXCEPTIONS = True
)
app.register_error_handler(Exception, defaultHandler)

##########################
# admin related routes
##########################

@app.route("/admin/register", methods = ["POST"])
def adm_register():
    data = request.get_json()
    name = data['name']
    password = data['password']
    email = data['email']
    result = login.register_admin(name, password, email)
    return dumps({
        'admin_id': result['id']
    })

@app.route("/admin/login", methods = ["POST"])
def adm_login():
    data = request.get_json()
    name = data['name']
    password = data['password']
    result = login.login_admin(name, password)
    return dumps({
        'token': result
    })

@app.route("/admin/logout", methods = ["POST"])
def adm_logout():
    data = request.get_json()
    name = data['name']
    token = data['token']
    result = login.logout_admin(name, token)
    return dumps({
        'is_success': result
    })

@app.route("/admin/profile/edit", methods = ["POST"])
def adm_edit():
    data = request.get_json()
    aid = data['admin_id']
    name = data['name']
    password = data['password']
    email = data['email']
    result = adm.edit_admin(aid, name, password, email)
    return dumps({
        'id': result['id']
    })

@app.route("/product/new", methods = ["POST"])
def new_product():
    data = request.get_json()
    name = data['name']
    price = data['price']
    description = data['description']
    category = data['category']
    deli_days = data['deli_days']
    result = adm.new_product(name, price, description, category, deli_days)
    db.add_prod(result)
    return dumps({
        'id': result['id']
    })

@app.route("/product/edit", methods = ["POST"])
def edit_product():
    data = request.get_json()
    id = data['id']
    name = data['name']
    category = data['category']
    description = data['description']
    result = adm.edit_product(id, name, category, description)
    return dumps({
        'id': result['id']
    })

# @app.route("/admin/product/editcategory")

@app.route("/product/delete", methods = ["POST"])
def delete_product():
    data = request.get_json()
    id = data['id']
    result = adm.delete_product(id)
    return dumps({
        'status': "success"
    })

@app.route("/order/statechange", methods = ["POST"])
def order_state_change():
    data = request.get_json()
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
    data = request.get_json()
    aname = data['account_name']
    fname = data['first_name']
    lname = data['last_name']
    password = data['password']
    email = data['email']
    address = data['address']
    city = data['city']
    country = data['country']
    try: 
        result = login.register_user(aname, fname, lname, password, email, address, city, country)
    except err.InvalidUsername as iuerr:
        raise iuerr
    except err.InvalidEmail as ieerr:
        raise ieerr
    except err.UsernameAlreadyExit as uaerr:
        raise uaerr
    return dumps({
        'user_id': result['id'],
        'token': result['token']
    })

@app.route("/user/login", methods = ["POST"])
def usr_login():
    data = request.get_json()
    name = data['account_name']
    password = data['password']
    try:
        result = login.login_user(name, password)
    except err.IncorrectUsername as uerr:
        raise uerr
    except err.InvalidPassword as perr:
        raise perr
    return dumps({
        'user_id': result['id'],
        'token': result['token']
    })

@app.route("/user/logout", methods = ["POST"])
def usr_logout():
    data = request.get_json()
    token = data['token']
    try:
        user_id = login.token_to_idd(token)
    except err.InvalidToken as error:
        raise error
    result = login.logout_user(token)
    return dumps({
        'user_id': user_id,
        'status': result
    })

@app.route("/user/profile", methods = ["GET"])
def usr_profile():
    # data = request.get_json()
    # token = data['token']

    token = request.args.get('token')

    try:
        user_id = login.token_to_idd(token)
    except err.InvalidToken as error:
        raise error
    result = usr.show_profile(user_id)
    return dumps(result)

# @app.route("user/profile/password/forget")

@app.route("/user/profile/password/change", methods = ["POST"])
def change_password():
    data = request.get_json()
    uname = data['name']
    opassword = data['old_password']
    result = usr.change_password(uname, opassword)
    return dumps({
        'status': result
    })

# @app.rounte("user/profile/edit")

@app.route("/user/profile/fund/add", methods = ["POST"])
def add_fund():
    data = request.get_json()
    uid = data['user_id']
    num = data['num']
    result = usr.add_fund(uid, num)
    return dumps({
        'status': "success",
        'fund': result['fund']
    })

@app.route("/user/cart/add", methods = ["POST"])
def add_cart():
    data = request.get_json()
    uid = data['user_id']
    pid = data['product_id']
    amount = data['amount']
    result = usr.add_product_to_cart(uid, pid, amount)
    price = usr.individual_price(pid, amount)
    return dumps({
        'pid': result['pid'],
        'amount': result['amount'],
        'cost': price
    })

@app.route("/user/cart/remove", methods = ["POST"])
def remove_cart():
    data = request.get_json()
    uid = data['user_id']
    pid = data['product_id']
    cart = usr.show_user_cart(uid)
    i = 0
    while (i < len(cart)):
        if (cart[i][0] == pid):
            break
    result = usr.remove_prod_from_cart(uid, cart[i])
    return dumps({
        'pid': result['pid']
    })

@app.route("/user/cart/cost", methods = ["POST"])
def cost_cart():
    data = request.get_json()
    uid = data['user_id']
    cart = usr.show_user_cart(uid)
    result = usr.total_price(cart)
    return dumps({
        'cost': result
    })

@app.route("/order/new", methods = ["POST"])
def create_order():
    data = request.get_json()
    uid = data['user_id']
    cart = usr.show_user_cart(uid)
    result = usr.purchase(uid, cart)
    return dumps({
        'id': result['id']
    })

@app.route("/order/rate", methods = ["POST"])
def rate_order():
    data = request.get_json()
    uid = data['user_id']
    oid = data['order_id']
    rating = data['rating']
    result = rate_order(uid, oid, rating)
    return dumps({
        'status': "success"
    })

@app.route("/order/refund", methods = ["POST"])
def refund_order():
    data = request.get_json()
    uid = data['user_id']
    oid = data['order_id']
    result = usr.order_refund(uid, oid)
    return dumps({
        'status': result
    })

@app.route("/admin/all_user", methods = ["GET"])
def admin_get_all_user():
    # date = request.get_json()
    result = adm.get_user_list()
    return dumps(result)

@app.route("/product/get_info", methods = ["GET"])
def get_product_info():
    # data = request.get_json()
    product_id = request.args.get('id')

    result = usr.show_product_detail(product_id)
    return dumps(result)


if __name__ == "__main__":
    app.run(port=(int(sys.argv[1]) if len(sys.argv) == 2 else 5000))
