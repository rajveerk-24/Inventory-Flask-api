import sqlite3
import uuid
from datetime import datetime
import random
from flask import jsonify


def createTables():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id VARCHAR(255),
                    password VARCHAR(255),
                    level INTEGER,
                    dateOfAccountCreation DATE,
                    approved BOOLEAN,
                    block BOOLEAN,
                    name VARCHAR(255),
                    address VARCHAR(255),
                    email VARCHAR(255),
                    phone VARCHAR(255),
                    pincode VARCHAR(255) );
                ''')
    
    conn.commit()
    conn.close()

def createUser(name , email, phone,  address, pincode , password):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    #user_id = str(uuid.uuid4())
    randomNumber1 = random.randint(1001, 99999)
    randomNumber2 = random.randint(101, 999)
    user_id = name[0:5] + str(randomNumber1) + "-" + str(randomNumber2)
    dateOfAccountCreation = datetime.now().strftime("%Y-%m-%d")
    cursor.execute('''INSERT INTO user (id, user_id, password, level, dateOfAccountCreation, approved, block, name, address, email, phone, pincode) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (None, user_id, password, -1, dateOfAccountCreation, 0, 0, name, address, email, phone, pincode))
    conn.commit()
    conn.close()
    return True

def getAllUsers():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    conn.close()

    user_list = []
    for user in users:
        user_dict = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "level": user[3],
            "dateOfAccountCreation": user[4],
            "approved": bool(user[5]),
            "block": bool(user[6]),
            "name": user[7],
            "address": user[8],
            "email": user[9],
            "phone": user[10],
            "pincode": user[11]
        }
        user_list.append(user_dict)

    return jsonify({"users": user_list})

def getUserById(user_id):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        user_dict = {
            "id": user[0],
            "user_id": user[1],
            "password": user[2],
            "level": user[3],
            "dateOfAccountCreation": user[4],
            "approved": bool(user[5]),
            "block": bool(user[6]),
            "name": user[7],
            "address": user[8],
            "email": user[9],
            "phone": user[10],
            "pincode": user[11]
        }
        return jsonify({"user": user_dict})
    else:
        return jsonify({"message": "User not found"}), 404


def updateUserAccessApproved(id, approved):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()



    cursor.execute('''UPDATE user SET approved = ? WHERE id = ?''', 
               (approved, id))


    conn.commit()
    conn.close()
    return True

def updateUserAccessBlocked(id, block):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()



    cursor.execute('''UPDATE user SET block = ? WHERE id = ?''', 
               (block, id))


    conn.commit()
    conn.close()
    return True


def updateUserAccessLevel(id, level):
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()

    cursor.execute('''UPDATE user SET level = ? WHERE id = ?''', 
               (level, id))


    conn.commit()
    conn.close()
    return True



#************************************create table for products**************************



def createTables():
    conn = sqlite3.connect("my_medicalShop.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255),
                    price FLOAT,
                    category VARCHAR(255),
                    stock INTEGER,
                    isActive BOOLEAN);
                ''')
    
    conn.commit()
    conn.close()
