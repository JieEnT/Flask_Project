from flask import Flask, render_template, url_for
app = Flask(__name__)

#A list of all the possible posts
posts = [
   {
       'author': 'Corey Schafer',
       'title': 'Blog post 1',
       'content': 'First post content',
       'date_posted': 'April 20, 2018'
   },
   {
       'author': 'Jane Doe',
       'title': 'Blog post 2',
       'content': 'Second post content',
       'date_posted': 'April 21, 2018'
   }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


# If we run the script directly from python then the name of the module is equivalent to __main__
# However if we import it from somewhere else then the name is the module itself
if __name__ == '__main__':
    app.run(debug=True)