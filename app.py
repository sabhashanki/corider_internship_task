# Importing libraries
from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

MONGO_URL = os.environ.get('MONGO_URI')

# Connecting MongoDB
cluster = MongoClient(MONGO_URL)
database = cluster['YOOGLE']
collection = database['USER_DATABASE']


# Print all user_data
@app.route('/users', methods = ['GET'])
def allusers_data():
    all_users = collection.find()
    user_data = []
    for data in all_users:
        user_dict = {
            'ID' : data['user_id'],
            'Name' : data['name'],
            'Email' : data['email'],
            'Password' : data['password']
        }
        user_data.append(user_dict)
    return jsonify(user_data)


# Returns user_info with ID
@app.route('/users/<user_id>', methods = ['GET'])
def user_info_ID(user_id):
    userid_exist = collection.count_documents({'user_id' : int(user_id)})
    print(userid_exist)
    if userid_exist > 0:
        data = collection.find_one({'user_id' : int(user_id)})
        user_dict = {
                'ID' : data['user_id'],
                'Name' : data['name'],
                'Email' : data['email'],
                'Password' : data['password']
        }
        return jsonify(user_dict)
    else:
        return "User ID does'nt exist"

# Create new user
@app.route('/users', methods = ['POST'])
def new_user():
    user_dict = dict(
        user_id = request.json['ID'],
        name = request.json['Name'],
        email = request.json['Email'],
        password = request.json['Password']
    )
    duplicates = collection.count_documents({'user_id' : user_dict['user_id']})
    if duplicates > 0:
        return 'User ID already exist'
    else:
        collection.insert_one(user_dict)
        return 'User data addedd successfully'


# Updates user_data with ID
@app.route('/users/<user_id>', methods = ['PUT'])
def update_userinfo(user_id):
    user_dict = dict(
        name = request.json['Name'],
        email = request.json['Email'],
        password = request.json['Password']
    )
    userid_exist = collection.count_documents({'user_id' : int(user_id)})
    if userid_exist > 0:
        collection.update_one({'user_id' : int(user_id)},
                           {'$set' : user_dict})
        return 'User info updated successfully'
    else:
        return "User ID does'nt exist"


# Deletes user_data with ID
@app.route('/users/<user_id>', methods = ['DELETE'])
def delete_userinfo(user_id):
    userid_exist = collection.count_documents({'user_id' : int(user_id)})
    if userid_exist > 0:
        collection.delete_one({'user_id' : int(user_id)})
        return 'User info deleted successfully'
    else:
        return "User ID does'nt exist"


if __name__ == "__main__":
    app.run()

