from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
db = SQLAlchemy(app)


class TODO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    time_created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "hello38"
    elif request.method == 'GET':
        return render_template("index.html")
    else:
        return "Invalid method: " + request.method


@app.route('/addTask', methods=['POST'])
def addTask():
    if request.method == 'POST':
        return redirect('/')


@app.route('/rmTask', methods=['POST'])
def rmTask():
    if request.method == 'POST':
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
