from flask import Flask, make_response, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Akamatsu"
app.config["MYSQL_DB"] = "driver"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

@app.route("/licenses", methods=["GET"])
def get_licenses():
    data = data_fetch("""select * from license""")
    return make_response(jsonify(data), 200)

@app.route("/licenses/<int:id>", methods=["GET"])
def get_license_by_id(id):
    data = data_fetch("""select * from license where id = {}""".format(id))
    return make_response(jsonify(data), 200)

@app.route("/licenses/<int:id>/violation_description", methods=["GET"])
def get_violation_description_by_license(id):
    data = data_fetch("""
        SELECT license.name, violations.violation_description, violations.penalty, vehicle.vehicle_color
        FROM license
        JOIN violations ON license.id = violations.license_id
        JOIN vehicle ON license.id = vehicle.license_id
        WHERE license.id = 5;
    """.format(id))
    return make_response(jsonify({"license_id" : id, "count": len(data), "violation_description": data}),201)
if __name__ == "__main__":
    app.run(debug=True)
