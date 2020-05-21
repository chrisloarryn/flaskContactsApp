from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '0.0.0.0' #'remotemysql.com'
app.config['MYSQL_USER'] = 'root' #'oNcACxFstL'
app.config['MYSQL_PASSWORD'] = 'root' #'Hct8mjydD2'
app.config['MYSQL_DB'] = 'testapp' #'oNcACxFstL'
# app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/addContact', methods=["POST"])
def addContact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        # 'cur' allow us to exec mysql queries
        cur = mysql.connect.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', 
        (fullname, phone, email))
        mysql.connection.commit()

        return jsonify({"msg": "received"})

@app.route('/edit')
def editContact():
    return jsonify({"msg": 'editContact'})

@app.route('/delete')
def deleteContact():
    return jsonify({"msg": 'deleteContact'})

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
