from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb+srv://kathjooubaid_db_user:EoklyKHbXj9HA1vZ@cluster0.rubip9g.mongodb.net/?appName=Cluster0")

db = client["student_db"]
collection = db["students"]

# Requirement 1 - API Route
@app.route('/api')
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)

    return jsonify(data)

# Home Page with Form
@app.route('/')
def home():
    return render_template('index.html')

# Form Submission
@app.route('/submit', methods=['POST'])
def submit():

    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('index.html', error=str(e))

# Success Page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)