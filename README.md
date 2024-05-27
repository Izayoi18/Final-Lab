Flask MySQL API
Overview
This project is a simple RESTful API built with Flask, MySQL, and HTTP Basic Authentication. It allows for CRUD operations on a license table and includes endpoints to fetch violation descriptions associated with licenses. The project also includes unit tests to verify the functionality of the API endpoints.

Requirements
Python 3.x
Flask
Flask-MySQLdb
Flask-HTTPAuth
Werkzeug
MySQL server
unittest (for testing)
Installation
Clone the repository:

git clone https://github.com/your-repo/flask-mysql-api.git
cd flask-mysql-api
Create a virtual environment and activate it:


python3 -m venv venv
source venv/bin/activate
Install the required Python packages:


pip install Flask Flask-MySQLdb Flask-HTTPAuth Werkzeug
Set up the MySQL database:

Make sure your MySQL server is running.
Create a database named driver and a table named license with the appropriate schema.
Update the database configuration in app.py with your MySQL credentials.
Configuration
Update the app.py file with your MySQL database credentials:

in python

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Akamatsu"
app.config["MYSQL_DB"] = "driver"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
Running the Application
Start the Flask application:

python Api.py
The API will be available at http://127.0.0.1:5000/.

API Endpoints
GET /: Returns a simple "Hello, World!" message.
GET /licenses: Returns all licenses.
GET /licenses/<int:id>: Returns the license with the specified ID.
GET /licenses/<int:id>/violation_description: Returns the violation descriptions associated with the specified license ID.
POST /licenses: Adds a new license. Expects a JSON body with name and license_number.
PUT /licenses/<int:id>: Updates the license with the specified ID. Expects a JSON body with name and license_number.
DELETE /licenses/<int:id>: Deletes the license with the specified ID.
GET /licenses/format: Returns query parameters id and aaaa as a JSON response.
Authentication
The API uses HTTP Basic Authentication. The default user is:

Username: Joshua
Password: Akamatsu
Running the Tests
Make sure the Flask application is running.
Run the unit tests:

python -m unittest discover
Unit Tests
The unit tests are located in the tests directory. They verify the following functionalities:

The index page returns a 200 status and the correct content.
The GET /licenses endpoint returns a 200 status and includes a specific license.
The GET /licenses/<int:id> endpoint returns a 200 status and includes a specific license.
