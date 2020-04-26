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
            return render_template('issues/unable_to.html', issue="add the task")


@DeprecationWarning
# @app.route('/rmTask/<int:id>', methods=['GET'])
def rmTask(): pass
#     if request.method == 'GET':
#         return redirect('/')


@app.route('/editTask/<int:tid>', methods=['POST', 'GET'])
def editTask(tid):
    task = TODO.query.get_or_404(tid)

    if request.method == 'POST':
        # Accessing through form in edit
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return render_template('issues/unable_to.html', issue="edit task")
    else:
        return render_template('edit.html', task=task)


@app.route('/cmTask/<int:tid>', methods=['GET'])
def cmTask(tid):
    if request.method == 'GET':
        return redirect('/')
    task = TODO.query.get_or_404(tid)

    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return render_template('issues/unable_to.html', issue='complete the task')


if __name__ == '__main__':
    app.run(debug=True)
