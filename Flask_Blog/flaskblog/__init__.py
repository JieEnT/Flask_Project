# To signal that flaskblog is a package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# Secret key protect against forgery, xss attacks
# Secret key helps to encrypt cookies and send them to the browser
app.config['SECRET_KEY'] = '8c3fb25a345726fc6442e19a29967a71'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Bind SQLAlchemy to the specific Flask application
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# Where login is the funtion name of the route for login, need to tell login_required where the login component is
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# since routes uses app we need to import it later to prevent circular imports
from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

