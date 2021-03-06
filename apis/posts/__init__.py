from flask import Blueprint, request, make_response, jsonify
import requests

# Decorators
from decorators.validateToken import validateToken

# Blueprint Prefix
posts = Blueprint('posts', __name__)



# ------------------------ Routes ------------------------
@posts.route('/', methods=['GET'])
@validateToken
def getAllPosts():
	response = requests.get("https://jsonplaceholder.typicode.com/posts")
	return make_response(jsonify(response.json()))

@posts.route('/<post_id>', methods=['GET'])
@validateToken
def getPostDetails(post_id):
	response = requests.get("https://jsonplaceholder.typicode.com/posts/" + post_id)
	return make_response(jsonify(response.json()))

@posts.route('/', methods=['POST'])
@validateToken
def addPost():
	response = requests.post("https://jsonplaceholder.typicode.com/posts", data = request.get_json())
	return make_response(jsonify(response.json()))

@posts.route('/<post_id>', methods=['PUT'])
@validateToken
def updatePost(post_id):
	# JSONPlaceholder isn't accepting ID>100 for PUT Requests - This is a walkaround for simulating it
	original_post_id = post_id
	if(int(post_id)>100):
		post_id = "100"
	response = requests.put("https://jsonplaceholder.typicode.com/posts/" + post_id, data = request.get_json())
	response = response.json()
	response["id"] = int(original_post_id)
	return make_response(jsonify(response))

@posts.route('/<post_id>', methods=['DELETE'])
@validateToken
def deletePost(post_id):
	response = requests.delete("https://jsonplaceholder.typicode.com/posts/" + post_id)
	return make_response(jsonify(response.json()))