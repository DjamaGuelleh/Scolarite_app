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
    return render_template('index.html')


@app.route("/connexion", methods=["POST"])
def connexion():
    """Function to create a user to the MySQL database"""
    user_id =  request.form.get("user_id")
    password = request.form.get("password")


    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM users where id= %s and mdp = %s"
        cursor.execute(sql, [user_id,password]) 
        notes = os.getenv("NOTES_SERVICE_HOST")       
        return redirect("http://localhost:5001")
    except Exception as exception:
        return jsonify(str(exception))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)