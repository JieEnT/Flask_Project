from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    # Initial request will be where page=1 (first page)
    # The command is read as taking a number of type int from after page= in url with default as 1
    # Note that page will simply be a number
    page = request.args.get('page', 1, type=int)
    # Instead of using dummy post data we will query the post data from the database
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

