from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
# Remember, everytime you make changes to the colum (such as adding one col or removing one col, change the value),
# you have to do the following: open terminal from pycharm, python3.7, from app import db, db.create_all() and exit.
db = SQLAlchemy(app)


# TODO send email warning if the due time is so soon and still incomplete,

class TODO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)

    time_created_str = datetime.now().strftime("%B %d %Y %H:%M:%S")

    time_created = db.Column(db.String, default=time_created_str)
    time_due = db.Column(db.String(500), nullable=False)

    # By default, the email warning is enabled
    email_warning = db.Column(db.Integer, default=1)

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.__repr__()

    def getTimeColor(self):
        # time_dif = self.get_time_difference()
        return 'red'

    def get_time_difference(self):
        # year_dif = int(self.time_due[7:11]) - int(self.time_created_str[7:11])
        # month_dif = int(self.time_due[])
        # self.time_due[]
        return ""


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('issues/404.html')
    elif request.method == 'GET':
        tasks = TODO.query.order_by(TODO.time_created).all()
        time_now = datetime.now().strftime("%b %d %Y %H:%M:%S")
        return render_template("index.html", tasks=tasks, mintime=time_now,
                               # Basically it's 100 years later.
                               maxtime=time_now[0:7] + str(int(time_now[7:11]) + 100) + time_now[11:])
    else:
        return "Invalid method: " + request.method


@app.route('/addTask/<content>/<date>', methods=['POST'])
def addTask(content, date):
    if request.method == 'POST':
        # content = request.form['content']
        task = TODO(content=content, time_due=date)

        # Add to database
        try:
            db.session.add(task)
            db.session.commit()
            return redirect('/')
        except:
            return render_template('issues/unable_to.html', issue="add the task")
    else:
        return render_template('issues/unable_to.html', issue="method not applicable")


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
        task.time_due = request.form['date']

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
        task = TODO.query.get_or_404(tid)

        try:
            db.session.delete(task)
            db.session.commit()
            return redirect('/')
        except:
            return render_template('issues/unable_to.html', issue='complete the task')
    else:
        return render_template('issues/unable_to.html', issue="method not applicable")


if __name__ == '__main__':
    app.run(debug=True)
