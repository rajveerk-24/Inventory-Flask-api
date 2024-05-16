from flask import Flask, jsonify, request
import sqlite3
from db import createTables, createUser, getAllUsers, getUserById, updateUserAccessApproved, updateUserAccessBlocked, updateUserAccessLevel

app = Flask(__name__)

@app.route('/CreateUser', methods=['POST'])
def CreateUser():
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    pincode = request.form['pincode']
    dbRes = createUser(name = name, password = password, email = email, phone = phone, address = address, pincode = pincode)


    if dbRes == True:
        return jsonify({"success": 200, "message" : "User created successfully"})
    else:
        return jsonify({"success": 400, "message" : "User creation failed"})


@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the inventory flask API"

@app.route('/allUsers', methods=['GET'])
def users():
    return getAllUsers()


@app.route('/user', methods=['GET'])
def getUser():
    user_id = request.form['user_id']
    if user_id:
        return getUserById(user_id=str(user_id))
    else:
        return jsonify({"error": "user_id parameter is missing"}), 400


@app.route('/updateUserAccessApproved', methods=['PATCH'])
def UpdateUserAccess1():
    user_id = request.form['user_id']
    approved = request.form['approved']
    updateUserAccessApproved(id=str(user_id), approved=str(approved))
    return "Approved access updated successfully"

@app.route('/updateUserAccessBlocked', methods=['PATCH'])
def UpdateUserAccess2():
    user_id = request.form['user_id']
    block = request.form['block']
    updateUserAccessBlocked(id=str(user_id), block=str(block))
    return "Blocked access updated successfully"


@app.route('/updateUserAccessLevel', methods=['PATCH'])
def UpdateUserAccess3():
    user_id = request.form['user_id']
    level = request.form['level']
    updateUserAccessLevel(id=str(user_id), level=str(level))
    return "Level access updated successfully"




#if __name__ == "__main__":
    createTables()
    app.run(debug=True)
