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
        return redirect('issues/404.html')
    elif request.method == 'GET':
        tasks = TODO.query.order_by(TODO.time_created).all()
        return render_template("index.html", tasks=tasks)
    else:
        return "Invalid method: " + request.method


@app.route('/addTask', methods=['POST'])
def addTask():
    if request.method == 'POST':
        content = request.form['content']
        task = TODO(content=content)

        # Add to database
        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/')
        except:
            return redirect('/issues/unable_to_add.html')


@app.route('/rmTask/<int:id>', methods=['GET'])
def rmTask():
    if request.method == 'GET':
        return redirect('/')


@app.route('/editTask', methods=['GET'])
def editTask():
    if request.method == 'GET':
        return redirect('/')


@app.route('/cmTask', methods=['GET'])
def cmTask():
    if request.method == 'GET':
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
