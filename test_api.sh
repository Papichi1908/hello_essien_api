#!/bin/bash
# Test api.sh - tests the API endpoints using curl
# Base URL of the API
BASE_URL="http://localhost:5000"
# A helper function that prints a divider for better readability
# FUnctions in a bash work like small resusable scripts within a script.
print_selection() {
    echo ""
    echo "=============================="
    echo "$1" # $1 = The first argument passed to the function when called      
    echo "=============================="
}
#-Curl flags explained
# -s = Silent mode (hides download progress noise)
# -o /dev/null = Discards the response body (we only care about status codes here)
# -w "%{http_code}" = Outputs only the HTTP status code after the request completes
# -X Post = Specifies the HTTP method 
# -H      = Sets a header (Content-Type tells server the body is JSON )
# -d      = Sends the specified data

print_section "Test 1: Root Route -GET /"
echo "Sending : GET $BASE_URL/"
echo "Expected: 200 + 'Hello, Essien!'"
echo ""

#curl with no flags just prints the full response body
curl -s "$BASE_URL/"
echo "" # Add a newline for better readability

print_section "Test 2: Health Check - GET /api/status"
echo "Sending : GET $BASE_URL/api/status"
echo "Expected: 200 + JSON with status 'ok'"
echo ""
curl -s "$BASE_URL/api/status"
echo "" 

print_section "Test 3: Get All Items - GET /api/items"
echo "Sending : GET $BASE_URL/api/items"
echo "Expected: 200 + JSON List of 2 items"
echo ""
curl -s "$BASE_URL/api/items"
echo ""

print_section "Test 4: Add an Item - POST /api/items (valid)"
echo "Sending : POST $BASE_URL/api/items"
echo "Request Body: {\"name\": \"New Mouse\"}"
echo "Expected: 201 + the new item returned"
echo ""
curl -s -X POST "$BASE_URL/api/items" \
     -H "Content-Type: application/json" \
     -d '{"name": "New Mouse"}'
     # The backlash \ continues a long command on the next line for better readability -bash treates it as a single command.
echo ""

print_section "Test 5: Add an Item - POST /api/items (missing name)"
echo "Sending : POST with empty body - should fail validation"
echo "Expected: 400 error"


curl -s -X POST "$BASE_URL/api/items" \
     -H "Content-Type: application/json" \
     -d '{}'
echo ""

print_section "Test 6: Error Handling - GET /api/doesnotexist"
echo "Visiting a route that doesn't exist"
echo "Expected: 404 + JSON error (NOT an HTML page)"
echo ""
curl -s "$BASE_URL/api/doesnotexist"
echo ""

print_section "Test 7: Error Handling - Wrong Method"
echo "Sending DELETE to a GET-only route"
echo "Expected: 405 JSON error"
echo ""
curl -s -X DELETE "$BASE_URL/api/status"
echo ""

echo ""
echo "All tests complete"
echo "Compare the output above against the 'Expected' labels."
echo "If all are match, your API is working correctly!"
echo ""
