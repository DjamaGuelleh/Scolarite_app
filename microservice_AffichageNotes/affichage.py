import os
from flask import jsonify, request, Flask, render_template, redirect, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "kaou"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "projet_devops"
app.config["MYSQL_DATABASE_HOST"] = "mysql"
mysql.init_app(app)

@app.route("/")
def index():
    return redirect(url_for('notes'))


@app.route("/notes")
def notes(): 
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT cne,nom,note FROM note,matiere where note.id_matiere= matiere.id_matiere"
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template('affichage.html', results=results) 
    except Exception as exception:
        return jsonify(str(exception))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)