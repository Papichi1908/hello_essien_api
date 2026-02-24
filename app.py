#Import flask
from flask import Flask, jsonify
#create the app instance
app = Flask(__name__)
define a route
@app.route('/')
def hello_essien():
    #Returns a plain text response with a status code of 200
    return 'Hello, Essien!', 200
#Second route-JSON Response
@app.route("api/hello")
def hello_api():
    #Jsonify conerts the dictionary into a JSON HTTP response
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
#Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)