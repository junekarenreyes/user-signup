from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route("/", methods=['POST'])
def validate_signup():

    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verifypassword_error = ''
    email_error = ''

    if username == '':
        username_error = 'Please enter username'
        username = ''
    else:
        username = str(username)
        if len(username) < 3 or len(username) > 31:
            username_error = 'Invalid username, should be between 3-20 characters'
            username = ''
        else:
            username = request.form['username']

    if password == '':
        password_error = 'Please enter password'
        password = ''
    else:
        password = str(password)
        if len(password) < 3 or len(password) > 31:
            password_error = 'Invalid password, should be between 3-20 characters'
            password = ''
        else:
            password = request.form['password']

    if verifypassword == "" :
        verifypassword_error = 'Please enter password.'
        verifypassword = ''
    
    if not password == verifypassword:
        verifypassword_error = verifypassword_error + 'Passwords do not match.'
        verifypassword = ''
        password = ''

    if len(str(email)) > 0:
        email = str(email)
        if len(email) < 3 or len(email) > 31:
            email_error = 'Invalid email, should be between 3-20 characters.'
            email = ''
        elif "." not in email:
            email_error = 'Invalid email. Please enter again.'
            email = ''
        elif "@" not in email:
            email_error = 'Invalid email. Please enter again.'
            email = ''


    if not username_error and not password_error and not verifypassword_error and not email_error:
        template = jinja_env.get_template('welcome.html')
        return template.render(username=username)

    else:
        template = jinja_env.get_template('index.html')
        return template.render(username_error=username_error,
            password_error=password_error,
            verifypassword_error=verifypassword_error,
            email_error=email_error, username=username, email=email)

    template = jinja_env.get_template('todos.html')
    return template.render(title="TODOs", tasks=tasks)

app.run()
