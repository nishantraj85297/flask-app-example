from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Database connection
connection = pymysql.connect(
    host="webapp-mysql.choqskyq0cdy.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="abcnis123",
    database="webapp"
)

@app.route("/")
def home():
    return "WebApp Backend Running"

@app.route("/houses", methods=["GET"])
def get_houses():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM houses")
    result = cursor.fetchall()

    houses = []
    for row in result:
        houses.append({
            "id": row[0],
            "city": row[1],
            "price": row[2],
            "type": row[3]
        })

    return jsonify(houses)

@app.route("/houses", methods=["POST"])
def add_house():
    data = request.json
    cursor = connection.cursor()

    query = "INSERT INTO houses(city,price,type) VALUES(%s,%s,%s)"
    cursor.execute(query,(data["city"],data["price"],data["type"]))
    connection.commit()

    return {"message":"House added"}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
