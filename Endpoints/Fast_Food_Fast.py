""""my project"""
from flask import jsonify,json,Flask,request,session,redirect,url_for
app = Flask(__name__)
app.config["SECRET_KEY"] = 'silasomurunga'


user_details = dict()
user_order ={1:{"order":"chips","username":"paul"},
2:{"order":"snacks","username":"silas"},
3:{"order":"coffee","username":"joshua"}}

@app.route('/api/v1/', methods=['GET']) #index endpoint
def home():
    """ route for the index page"""
    return jsonify({"message" : "welcome to fast_Food_Fast online restaurant"})

@app.route("/api/v1/auth/signup", methods=['POST'])#signup endpoint
def signup():
    """route for signup for user"""
    data = request.get_json()
    username = data["username"]
    if username in user_details:
        return jsonify({"message":"username already taken choosen another username"})
    fname = data["fname"]
    lname = data["lname"]
    email = data["email"]
    password = data["password"]
    cpassword = data["cpassword"]
    user_details.update({"username":username, "fname":fname, "lname":lname,\
                          "email" :email, "password":password, "cpassword":cpassword})
    return jsonify({"message" : "successful signup"})

@app.route("/api/v1/auth/confirmation", methods=['POST']) #confirmation endpoint
def confirmation():
    """route for confirming a user"""
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]
    if user_details["username"] == username:
        if user_details["email"] == email:
            if user_details["password"] == password:
                return jsonify({"message" : "You acount has been activated"})
                return redirect(url_for('login'))
        return redirect(url_for('signup'))
    return redirect(url_for('signup'))

@app.route("/api/v1/auth/login", methods=['POST'])#login endpoint
def login():
    """route for login for activate account"""
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]
    if user_details["username"] == username:
        if user_details["email"] == email:
            if user_details["password"] == password:
                return jsonify({"message":"logged in successful"})
                return redirect(url_for('order'))
        return redirect(url_for('forget_password_or_username'))
    return redirect(url_for('forget_password_or_username'))

@app.route('/api/v1/auth/admin', methods=['GET'])
def hello_admin():
    """route for admin privilege only"""
    return jsonify({"message":"Hello Admin"})

@app.route('/api/v1/auth/user/<name>', methods=['GET'])#guest/admin endpoint
def hello_user(name):
    """route to detremine whether you are admin or guest user """
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

@app.route('/api/v1/auth/guest/<guest>', methods=['GET'])#guest endpoint
def hello_guest(guest):
    """route for user privelege only"""
    return 'Hello %s as Guest' % guest

@app.route("/api/v1/auth/forgetpassword", methods=['POST'])
 #resetpassword/username endpoint
def forget_password_or_username():
    """route to reset your password and username"""
    data = request.get_json()
    del user_details["username"]
    del user_details["password"]
    username = data["username"]
    password = data["password"]
    details.update({"username" : username, "password" : password})
    return redirect(url_for('confirmation'))

@app.route("/api/v1/account",methods=['GET'])
def account():
    return jsonify(user_details)


@app.route("/api/v1/order", methods=['POST']) #post an order endpoint
def order():
    """route to post your order"""
    data = request.get_json()
    order = data["order"]
    username = data["username"]
    user_order.update({len(user_order) + 1:{"username":username,"order":order}})
    return redirect(url_for('all_orders'))

@app.route("/api/v1/order/<int:orderid>", methods=['DELETE']) #delete an order endpoint
def delete_order(orderid):
    """route to delete your order"""
    del user_order[orderid]
    return jsonify({"message":"order has been deleted"})

@app.route("/api/v1/order/<int:orderid>", methods=['PUT']) #modify an order endpoint
def modify_order(orderid):
    """route to delete your order"""
    del user_order[orderid]
    data = request.get_json()
    order = data["order"]
    username = data["username"]
    user_order.update({len(user_order) + 1:{"username":username,"order":order}})
    return jsonify({"message":"order has been updated"})
    return redirect(url_for('all_orders'))
    return jsonify({"message":"order has been updated"})

@app.route("/api/v1/order", methods=["GET"]) #all orders endpoint
def all_orders():
    """route to view all orders posted"""
    return jsonify(user_order)

@app.route("/api/v1/order/<int:orderid>", methods=['GET'])
#specific order endpoint
def orders_view(orderid):
    """route to view specific order as per they id"""
    return jsonify({"Order":"Your  order: {} ".format(user_order[orderid])})

@app.route("/api/v1/logout", methods=['GET']) #logout endpoint
def logout():
    """route for logging out"""
    return jsonify({"message":"successful logout"})

if __name__ == '__main__':
    app.run(debug=True)
