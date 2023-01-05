import os
from flask import jsonify, request, Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT"))
mysql.init_app(app)


@app.route("/")
def index():
    """Function to test the functionality of the API"""
    return "Hello, world!"


@app.route("/Inserstion", methods=["POST"])
def add_user():
    """Function to create a user to the MySQL database"""
    json = request.json
    filier = json["id_filiere"]
    matiere = json["id_matiere"]
    cne = json["cne"]
    note = json["note"]
    if filier and matiere and cne and note and request.method == "POST":
        sql = "INSERT INTO note(id_filiere, id_filiere, cne,note) " \
              "VALUES(%s, %s, %s)"
        data = (matiere, filier, cne,note)
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()
            resp = jsonify("Note ajouter !")
            resp.status_code = 200
            return resp
        except Exception as exception:
            return jsonify(str(exception))
    else:
        return jsonify("remplir les champs obligatoires !")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)