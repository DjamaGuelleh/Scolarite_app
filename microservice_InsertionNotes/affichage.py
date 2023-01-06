
import os
from flask import jsonify, request, Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "oooo"
app.config["MYSQL_DATABASE_DB"] = "projet_devops"
app.config["MYSQL_DATABASE_HOST"] = "127.0.0.1"
mysql.init_app(app)


@app.route("/")
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id_etudiant , id_matiere , note FROM notes")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        resp = jsonify(rows)
        resp.status_code = 200
        render_template('affichage.html', results = resp ) 
    except Exception as exception:
        return jsonify(str(exception))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)