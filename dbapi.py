from flask import Flask, render_template, request, session, jsonify
import dbcon as db
import json
import datetime
# this application repressent web application
app = Flask(__name__)



# when user open site / or open slash the function below it executes
# decorater
# jsonify display in json format

@app.route("/")
def index():
    x = db.con()
    data=[]

    for rows in x :
        data.append([x for x in rows])
    return jsonify(data)

