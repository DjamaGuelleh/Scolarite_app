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

def index():
    return render_template('InsertionForm.html')


@app.route("/add_note", methods=["POST"])
def add_user():
    """Function to create a user to the MySQL database"""
    filier =  int(request.form.get("id_filiere"))
    matiere = int(request.form.get("id_matiere"))
    cne = int(request.form["cne"])
    note = float(request.form["note"])
 
    if filier and matiere and cne and note and request.method == "POST":
        sql = "INSERT INTO note(id_matiere, id_filiere, cne,note) " \
              "VALUES(%s,%s, %s, %s)"
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