from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI']
# index rout
# looks for the template
@app.route('/')
def index():
    # render_templates renders html templates as a key word argument
    return render_template('index.html')

# runs the code
if __name__ == "__main__":
    app.run(debug=True)