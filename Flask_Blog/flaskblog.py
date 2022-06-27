from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#Secret key protect against forgery, xss attacks
#Secret key helps to encrypt cookies and send them to the browser
app.config['SECRET_KEY'] = '8c3fb25a345726fc6442e19a29967a71'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #f string is a literal string
        flash(f'Account created for {form.username.data}!', 'success')
        #We will redirct to the home page after submission of form
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# If we run the script directly from python then the name of the module is equivalent to __main__
# However if we import it from somewhere else then the name is the module itself
if __name__ == '__main__':
    app.run(debug=True)
