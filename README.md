#Instructions and how the project works:

Clone this repository using Git or download the ZIP file.
Open a terminal and navigate to the project directory.
Install the required dependency:
pip install flask

Running the API:
Start the Flask development server:
python app.py
This will start the API server on http://127.0.0.1:5000/ by default.

Testing the API:
The project includes unit tests using the unittest module.
Run the tests using:
python test_app.py
This will execute the tests and report the results.

Using the API:
The API provides a single endpoint:
/orders (POST): This endpoint accepts a JSON payload containing a list of component codes under the key components. It returns a JSON response with details about the order.

Example Request (using Postman):
Open Postman and create a new POST request.
Set the URL to http://127.0.0.1:5000/orders.
In the Body tab, select "raw" and choose JSON (application/json) as the content type.
Paste the following JSON payload:
JSON
{
  "components": ["I", "A", "D", "F", "K"]
}
Send the request.
Example Response:
{
  "order_id": "b80a...",  // This will be a unique ID generated for the order.
  "total": 156.56,
  "parts": [
    "Android OS",
    "LED Screen",
    "Wide-Angle Camera",
    "USB-C Port",
    "Metallic Body"
  ]
}

