from flaskblog import app

# If we run the script directly from python then the name of the module is equivalent to __main__
# However if we import it from somewhere else then the name is the module itself
if __name__ == '__main__':
    app.run(debug=True)
