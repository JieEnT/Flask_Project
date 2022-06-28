# To signal that flaskblog is a package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Secret key protect against forgery, xss attacks
# Secret key helps to encrypt cookies and send them to the browser
app.config['SECRET_KEY'] = '8c3fb25a345726fc6442e19a29967a71'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# since routes uses app we need to import it later to prevent circular imports
from flaskblog import routes