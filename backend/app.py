from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)

def connect_database():

    while True:
        try:

            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="appdb"
            )

            return conn

        except:
            print("Waiting for MySQL database...")
            time.sleep(5)


@app.route("/api")

def home():

    conn = connect_database()

    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))"
    )

    cursor.execute("INSERT INTO users (name) VALUES ('Mohan')")
    conn.commit()

    cursor.execute("SELECT * FROM users")

    result = cursor.fetchall()

    return jsonify({
        "message": "Backend connected successfully",
        "data": result
    })


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
