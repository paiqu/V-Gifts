"""
    This file includes all functions can be directly called 
    by frontend
"""

import database as db
import user as usr
import admin as adm
import order as odr
import product as pdt
import webpage as wbp
import login as login
import error as err
from logging import DEBUG
from flask import Flask, request
from flask_cors import CORS
from flask_mail import Mail
from json import dumps
from werkzeug.utils import secure_filename
import random
import sys
import os


ALLOWED_IMAGES = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_image(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGES

def defaultHandler(err):
    response = err.get_response()
    print("response", err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = "application/json"
    return response

app = Flask(__name__)
CORS(app)
app.config.update(
    TRAP_HTTP_EXCEPTIONS = True,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "oldjeffspectator@gmail.com",
    MAIL_PASSWORD = "jeffLHR123"
)
app.register_error_handler(Exception, defaultHandler)

##########################
# admin related routes
##########################

mail = Mail(app)

@app.route("/user/login/send_mail/", methods = ["POST"])
def send_mail():
    data = request.get_json()
    email = data["email"]
    num_str = "".join(str(random.choice(range(10))) for i in range(6))
    user_test = usr.my_reset_passowrd(email)
    usr.change_password(user_test["id"], user_test["password"], num_str)
    msg = mail.send_message(
        "Send Mail for reset password",
        sender = ["ANONYMOUS", "oldjeffspectator@gmail.com"],
        recipients = [email],
        body="This is your temporary passowrd, please change it as soon as \
            possible! Password: " + num_str
    )
    mail.send(msg)
    return "Mail sent"

@app.route("/admin/register", methods = ["POST"])
def adm_register():
    data = request.get_json()
    name = data["name"]
    password = data["password"]
    email = data["email"].lower()
    try:
        result = login.register_admin(name, password, email)
    except err.InvalidUsername as iuerr:
        raise iuerr
    except err.InvalidEmail as ieerr:
        raise ieerr
    except err.UsernameAlreadyExit as uaerr:
        raise uaerr
    except err.EmailAlreadyExit as eaerr:
        raise eaerr
    return dumps({
        "admin_id": result["id"]
    })

@app.route("/admin/login", methods = ["POST"])
def adm_login():
    data = request.get_json()
    name = data["name"]
    password = data["password"]
    try:
        result = login.login_admin(name, password)
    except err.IncorrectUsername as uerr:
        raise uerr
    except err.InvalidPassword as perr:
        raise perr
    return dumps({
        "admin_id": result["id"],
        "token": result["token"]
    })

@app.route("/admin/logout", methods = ["POST"])
def adm_logout():
    data = request.get_json()
    token = data["token"]
    try:
        aid = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = login.logout_admin(token)
    return dumps({
        "is_success": result
    })

@app.route("/admin/profile", methods = ["GET"])
def adm_profile():
    token = request.args.get("token")
    try:
        aid = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = adm.show_profile(aid)
    return dumps(result)

@app.route("/admin/profile/edit", methods = ["POST"])
def adm_edit():
    data = request.get_json()
    token = data["token"]
    try:
        aid = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    name = data["name"]
    password = data["password"]
    email = data["email"].lower()
    result = adm.edit_admin(aid, name, password, email)
    return dumps({
        "id": result["id"]
    })

@app.route("/product/new", methods = ["POST"])
def new_product():
    data = request.form
    token = data["token"]
    try:
        admin_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    prod_name = data["name"]
    prod_descrip = data["description"]
    prod_price = data["price"]
    prod_delivery = data["delivery"]
    prod_category = None
    if "file" not in request.files:
        flag = False
    else:
        image = request.files["file"]
        if image.filename == "":
            flag = False
        elif allowed_image(image.filename) == False:
            flag = False
        else :
            flag = True
    if flag == True:
        path = "../frontend/public/img/products"
        filename = secure_filename(image.filename)
        image.save(os.path.join(path, filename))
        prod_pic = "/img/products/" + filename
    else:
        raise err.NoImage(description = "No image found, please upload one!")
    result = pdt.new_product(prod_name, prod_descrip, prod_category, prod_price, \
                prod_delivery, prod_pic, db_name = "database.json")
    db.add_prod(result)
    return dumps({
        "pic_link": prod_pic
    })

# @app.route("/admin/product/editcategory")

@app.route("/product/delete", methods = ["POST"])
def delete_product():
    data = request.get_json()
    token = data["token"]
    try:
        aid = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    id = data["id"]
    result = pdt.delete_product(id)
    return dumps({
        "status": "success"
    })

@app.route("/order/statechange", methods = ["POST"])
def order_state_change():
    data = request.get_json()
    token = data["token"]
    try:
        aid = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    order_id = data["id"]
    state = data["state"]
    result = odr.change_order_state(order_id, state)
    return dumps({
        "status": "success",
        "id": result["id"],
        "state": result["state"]
    })

##########################
# user side routes
##########################

@app.route("/user/register", methods = ["POST"])
def usr_register():
    data = request.get_json()
    aname = data["account_name"]
    fname = data["first_name"]
    lname = data["last_name"]
    password = data["password"]
    email = data["email"].lower()
    address = data["address"]
    city = data["city"]
    country = data["country"]
    try: 
        result = login.register_user(aname, fname, lname, password, email, address, city, country)
    except err.InvalidUsername as iuerr:
        raise iuerr
    except err.InvalidEmail as ieerr:
        raise ieerr
    except err.UsernameAlreadyExit as uaerr:
        raise uaerr
    except err.EmailAlreadyExit as eaerr:
        raise eaerr
    return dumps({
        "user_id": result["id"],
        "token": result["token"]
    })

@app.route("/user/login", methods = ["POST"])
def usr_login():
    data = request.get_json()
    name = data["account_name"]
    password = data["password"]
    try:
        result = login.login_user(name, password)
    except err.IncorrectUsername as uerr:
        raise uerr
    except err.InvalidPassword as perr:
        raise perr
    return dumps({
        "user_id": result["id"],
        "token": result["token"]
    })

@app.route("/user/logout", methods = ["POST"])
def usr_logout():
    data = request.get_json()
    token = data["token"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = login.logout_user(token)
    return dumps({
        "user_id": user_id,
        "status": result
    })

@app.route("/user/profile", methods = ["GET"])
def usr_profile():
    token = request.args.get("token")
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = usr.show_profile(user_id)
    return dumps(result)

# @app.route("user/profile/password/forget")

@app.route("/user/profile/password/change", methods = ["POST"])
def change_password():
    data = request.get_json()
    token = data["token"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    opassword = data["old_password"]
    npassword = data["new_password"]
    result = usr.change_password(user_id, opassword, npassword)
    return dumps({
        "status": result
    })

# @app.rounte("user/profile/edit")

@app.route("/user/profile/fund/add", methods = ["POST"])
def add_fund():
    data = request.get_json()
    token = data["token"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    num = int(data["num"])
    result = usr.add_fund(user_id, num)
    return dumps({
        "status": "success",
        "fund": result["fund"]
    })

@app.route("/user/cart/add", methods = ["POST"])
def add_cart():
    data = request.get_json()
    token = data["token"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    pid = data["product_id"]
    amount = data["amount"]
    pname = pdt.product_id_to_name(pid)
    result = usr.add_product_to_cart(user_id, pid, amount)
    price = usr.individual_price(pid, amount)
    return dumps({
        "product_id": pid,
        "product_name": pname,
        "amount": amount,
        "cost": price
    })

@app.route("/user/cart/remove", methods = ["POST"])
def remove_cart():
    data = request.get_json()
    token = data["token"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    pid = data["product_id"]
    cart = usr.show_user_cart(user_id)
    i = 0
    while (i < len(cart)):
        if (cart[i][0] == pid):
            break
        i = i + 1
    result = usr.remove_prod_from_cart(user_id, cart[i])
    return dumps({})

@app.route("/user/cart/change", methods = ["POST"])
def cart_change():
    data = request.get_json()
    token = data["token"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    pid = data["product_id"]
    amount = data["amount"]
    cart = usr.show_user_cart(user_id)
    i = 0
    while (i < len(cart)):
        if (cart[i][0] == pid):
            break
        i = i + 1
    result = usr.change_cart_amount(user_id, i, amount)
    return dumps({})

@app.route("/user/cart/cost", methods = ["GET"])
def cost_cart():
    # data = request.get_json()
    # token = data["token"]
    token = request.args.get("token")
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    cart = usr.show_user_cart(user_id)
    result = usr.total_price(cart)
    return dumps({
        "cost": result
    })

@app.route("/user/cart/list", methods = ["GET"])
def cart_list():
    token = request.args.get("token")
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = usr.show_all_cart(user_id)
    return dumps(result)

@app.route("/order/new", methods = ["POST"])
def create_order():
    data = request.get_json()
    token = data["token"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    # list : [[product_id, amount]
    products = data["list"]
    try:
        result = usr.purchase(user_id, products)
    except err.NotEoughFund as error:
        raise error
    return dumps({})

@app.route("/order/rate", methods = ["POST"])
def rate_order():
    data = request.get_json()
    token = data["token"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    oid = data["order_id"]
    rating = data["rating"]
    result = odr.rate_order(user_id, oid, rating)
    return dumps({
        "status": "success"
    })

@app.route("/order/refund", methods = ["POST"])
def refund_order():
    data = request.get_json()
    token = data["token"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    oid = data["order_id"]
    result = odr.order_refund(user_id, oid)
    return dumps({
        "status": result
    })

@app.route("/order/list", methods = ["GET"])
def order_list():
    token = request.args.get("token")
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = odr.show_all_order(user_id)
    return dumps(result)

@app.route("/admin/all_user", methods = ["GET"])
def admin_get_all_user():
    # date = request.get_json()
    token = request.args.get("token")
    try:
        aid = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = adm.get_user_list()
    return dumps(result)

@app.route("/admin/all_order", methods = ["GET"])
def admin_get_all_order():
    token = request.args.get("token")
    try:
        aid = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = adm.get_all_order()
    return dumps(result)

@app.route("/admin/all_admin", methods = ["GET"])
def all_admin():
    token = request.args.get("token")
    try:
        aid = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = adm.get_all_admin()
    return dumps(result)

@app.route("/admin/add_admin", methods = ["POST"])
def admin_regesiter_admin():
    data = request.get_json()
    token = data["token"]
    try:
        aid = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    name = data["name"]
    password = data["password"]
    email = data["email"].lower()
    try:
        result = login.register_admin_nologin(name, password, email)
    except err.InvalidUsername as iuerr:
        raise iuerr
    except err.InvalidEmail as ieerr:
        raise ieerr
    except err.UsernameAlreadyExit as uaerr:
        raise uaerr
    except err.EmailAlreadyExit as eaerr:
        raise eaerr
    return dumps({})

@app.route("/product/get_info", methods = ["GET"])
def get_product_info():
    # data = request.get_json()
    product_id = request.args.get("id")
    result = pdt.show_product_detail(product_id)
    return dumps(result)

@app.route("/product/get_all", methods = ["GET"])
def get_product_all():
    # data = request.get_json()
    token = request.args.get("token")
    page = int(request.args.get("page"))
    if token == "":
        user_id = -1
    else:
        try:
            user_id = login.token_to_id(token)
        except err.InvalidToken as error:
            raise error
    result = pdt.show_product_lst(page, user_id)
    return dumps(result)

@app.route("/product/search", methods = ["POST"])
def get_product_by_search():
    data = request.get_json()
    token = data["token"]
    if token == "":
        user_id = -1
    else:
        try:
            user_id = login.token_to_id(token)
        except err.InvalidToken as error:
            raise error
    page = int(data["page"])
    keyword = data["keyword"]
    ctgry = data["category"] # [1, 0, ..., 1] of len() = 11
    price_rg = data["price_range"] # [min_price, max_price]
    rec_lst = pdt.show_product_lst(page, user_id)["recommendation_list"]
    user_id = -1
    if price_rg == []:
        result = wbp.search_filter_recommendation(keyword, ctgry, [0, 999999], user_id, page)
    else:
        result = wbp.search_filter_recommendation(keyword, ctgry, price_rg, user_id, page)
    return dumps({
        "recommendation_list": rec_lst,
        "product_lst": result["product_lst"],
        "total_pages": result["total_pages"],
        "flag": result["flag"]
    })

@app.route("/user/edit", methods = ["POST"])
def user_edit_info():
    data = request.get_json()
    token       = data["token"]
    fname       = data["fname"]
    lname       = data["lname"]
    address     = data["address"]
    city        = data["city"]
    country     = data["country"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    result = usr.edit_info_user(user_id, fname, lname, address, city, \
            country, "database.json")
    return dumps(result)

@app.route("/product/edit", methods = ["POST"])
def prod_edit_info():
    data = request.form
    token = data["token"]
    try:
        admin_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    prod_id = data["id"]
    prod_name = data["name"]
    prod_descrip = data["description"]
    prod_price = data["price"]
    prod_delivery = data["delivery"]
    if "file" not in request.files:
        flag = False
    else:
        image = request.files["file"]
        if image.filename == "":
            flag = False
        elif allowed_image(image.filename) == False:
            flag = False
        else :
            flag = True
    if flag == True:
        path = "../frontend/public/img/products"
        filename = secure_filename(image.filename)
        image.save(os.path.join(path, filename))
        prod_pic = "/img/products/" + filename
    else:
        dbs = db.load_json()
        prod_pic = dbs["PRODUCT_DB"][str(prod_id)]["pic"]
    result = pdt.edit_product(prod_id, prod_name, prod_descrip, prod_price, \
                prod_delivery, prod_pic, db_name = "database.json")
    return dumps({
        "pic_link": prod_pic
    })

@app.route("/user/get_interest", methods = ["GET"])
def user_get_interest():
    token = request.args.get("token")
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    rt = db.get_interest_lst()
    return dumps({
        "interest_list": rt
    })

@app.route("/user/set_interest", methods = ["POST"])
def user_set_interest():
    data = request.get_json()
    token           = data["token"]
    interest_lst    = data["interest_lst"]
    try:
        user_id = login.token_to_id(token)
    except err.InvalidToken as error:
        raise error
    rt = db.edit_user_interest(user_id, interest_lst)
    return dumps(rt)

if __name__ == "__main__":
    app.run(port = (int(sys.argv[1]) if len(sys.argv) == 2 else 5000))
