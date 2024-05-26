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

@app.route("/license", methods=["GET"])
def get_drivers():
    cur = mysql.connection.cursor()
    query="""
    select * from license
    """
    cur.execute(query)
    data = cur.fetchall()
    cur.close()

    return make_response(jsonify(data), 200)
"""""@app.route("/license/<int:id>", method=["GET"])
def get_driver_by_name(name):
    cur = mysql.connection.cursor()
    query = """"select * from license""""
    cur.execute(query)
    data = cur.fetchall()
    cur.close()


"""

if __name__ == "__main__":
    app.run(debug=True)
