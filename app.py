from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# inits flask
app = Flask(__name__)
# config for sql data base fopr app to locate db from sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# inits the sqlalchemy object with teh flask app
# To run db, open python shell --> fromapp, import app, db --> app.app_context().push() --> db.create_all()-->exit()
db = SQLAlchemy(app)

# sets schema for table in sql
# Id column --> numbers only  
# Content --> 200 char string cannot be null
# date created --> date created in UTC time
class Todo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # returns string --> %r replaced by self.id
    def __repr__(self):
        return '<Task %r>' % self.id
        



# index rout
# looks for the template
# app.route(url, methods)
# this allows for post and get to this route
@app.route('/', methods=['POST', 'GET'])
def index():
    # checking if the request is of type post
    if request.method == 'POST':
        # grabs the data from request form and sets it to a variable
        task_content = request.form['content']
        # assigns new task with the class inheritance of to do
        new_task = Todo(content=task_content)
        try:
            # adds it to the db and redirects the data
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            # error handling
            return 'There was an issue adding your task'
    else:
        # looks at db by order of date created and return all
        tasks = Todo.query.order_by(Todo.date_created).all()
        # renders all task
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return " There was a problem delete the task"


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating the task"
    else:
        return render_template('update.html', task=task)

# runs the code
if __name__ == "__main__":
   
    app.run(debug=True)