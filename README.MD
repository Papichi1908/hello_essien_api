Hello Essien API
A minimal Python REST API built with Flask.
Setup & Run
bash   
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the server
python app.py

Endpoints

Method        URL              Response
GET            /               Hello, Essien! (plain text)
GET           /api/hello{     "message": "Hello, World!"}
GET           /api/hello/Ali  {"message": "Hello, Ali!"}

Hello World API — v2
A Python REST API built with Flask featuring multiple routes, input validation, and error handling.

Setup & Run
bash
pip install -r requirements.txt
python app.py

API Endpoints
Method    Route                          Description                                    Status 
GET      /                               Root hello world                                200 
GET      /api/hello                      JSON hello world                                200
GET      /api/hello/<name>               Personalized greeting                           200
GET      /api/status                     Health check (DevOps use)                       200
GET     /api/items                       Get all items                                   200
POST    /api/items                       Add a new item                                  201


Error Responses
All errors return JSON (never HTML):
Code              Meaning
400               Bad request / missing body
404               Route not found
405               Wrong HTTP method
422               Validation failed 
500               Server error

Testing Locally
bash
# Terminal 1 — start the server
python app.py

# Terminal 2 — run all tests
bash test_api.sh

Clean Git Commit Workflow
bash
# After making each focused change:
git add .
git commit -m "Your descriptive message"
git push

Recommended Commit History for This Version
git commit -m "Add /api/status health check route"
git commit -m "Add GET and POST routes for /api/items"
git commit -m "Add input validation to POST /api/items"
git commit -m "Add global error handlers for 404, 405, 500"
git commit -m "Add test_api.sh bash script for local testing"