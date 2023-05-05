from flask import Flask, render_template
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
@app.route('/', method=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        pass
    # render_templates renders html templates as a key word argument
    return render_template('index.html')

# runs the code
if __name__ == "__main__":
   
    app.run(debug=True)