#Import flask and jsonify
from flask import Flask, jsonify, request
#create the app instance
app = Flask(__name__)
#in-memory data store for items
items = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]
#define a route
@app.route('/')
def hello_essien():
    #Returns a plain text response with a status code of 200
    return 'Hello, Essien!', 200
#Second route-JSON Response
@app.route("/api/hello")
def hello_api():
    #Jsonify converts the dictionary into a JSON HTTP response
    data = {
        "message": "Hello, Essien!",
        "status": "success"
    }
    return jsonify(data), 200

#A route with a URL parameter
@app.route("/api/hello/<name>")
def hello_name(name):
    data = {
        "message": f"Hello, {name}!",
        "status": "success"
    }
    return jsonify(data), 200
#Health check route GET /api/status
@app.route("/api/status")
def status():
    return jsonify ({
        "status": "ok", #human-readble health indicator
        "version": "2.0.0", #lets you know which version of the API is running
        "uptime_check": True #indicates that the server is up and running
    }), 200

#Get all items GET /api/items
@app.route("/api/items", methods=["GET"])
def get_items():
    return jsonify ({
        "status": "success",
        "count": len(items), #tells the client how many items exist 
        "items": items
    }), 200

# Add an item POST /api/items
@app.route("/api/items", methods=["POST"])
def add_item():
    data = request.get_json() #get the JSON data from the request body

    #validation 
    # Rule1: To check if an JSON body was sent at all
    if data is None:
        return jsonify({
            "status": "error",
            "message": "Request body is missing or not valid JSON."
        }), 400
    #Rule2: Does the body contain the required "name" field?
    if "name" not in data:
        return jsonify({
            "status": "error",
            "message": "Missing required field: 'name'."
        }), 400
    #Rule3: Is the "name" field value a non-empty string?
    if not isinstance(data["name"], str) or not data["name"].strip():
        return jsonify({
            "status": "error",
            "message": "'name' must be a non-empty string."
        }), 422 #422 = UNprocessable Entity - data was not received but failed business logic validation
    
    #Create a new item
    # Auto-generate an ID. In a real DB, this is handled for you.
    new_item = {
        "id": len(items) + 1, #simple incrementing ID
        "name": data["name"].strip() #remove leading/trailing whitespace
    }

    items.append(new_item) #to add our in-memory list of items

    return jsonify({
        "status": "success",
        "message": f"Item added successfully.",
        "item": new_item
    }), 201

#Error Handlers -Gloal catches for HTTP errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Route not found. Check the URL and try again.",
        "code": 404 
    }), 404
@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "status": "error",
        "message": "HTTP method not allowed on this route.",
        "code": 405
    }), 405
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "status": "error",
        "message": "An internal server error occurred.",
        "code": 500
    }), 500
#Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)