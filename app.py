import datetime
import os
import time
from firebase import firebase
from posts import Posts
from flask import Flask, render_template, request, jsonify
from user import User,Profile
# import flask_oauth
from flask import flash
from flask import redirect, url_for, session, Session
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import Form, IntegerField, StringField, PasswordField, validators
from wtforms.fields import SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from forms import IssueForm, CommentForm,UploadForm,graph_input,create_article_form,LoginForm,RegisterForm
import munch
app = Flask(__name__)
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}
ALLOWED_CATEGORY = {'ACM', 'IOI'}
import uuid
# import pyrebase
# config = {
#   "apiKey": "AIzaSyCp_8Wb0RB-0AhWpsvVahxez2nkQWa1RXc",
#   "authDomain": "fir-basic-9a5d7.firebaseapp.com",
#   "databaseURL": "https://fir-basic-9a5d7.firebaseio.com",
#   "storageBucket": "fir-basic-9a5d7.appspot.com",
#   "serviceAccount": "fir-basic-9a5d7-firebase-adminsdk-0jn0d-1d27894db7.json"
# }
#
# firebaseAuth = pyrebase.initialize_app(config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
firebase=firebase.FirebaseApplication('https://fir-basic-9a5d7.firebaseio.com/')
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
ckeditor = CKEditor(app)

app.secret_key = "super secret key"
sess = Session()


class user_form(Form):
    uid = StringField('username', [validators.DataRequired()])


@app.route('/')
def index():
    postlist = []
    result = firebase.get('/posts', None)
    for key,value in result.items():
        postlist.append(Posts(key,value).getShowable())
    print(postlist[0])


    error = 'You are not logged in'
    dumb = 'dumb'
    '''if 'username' not in session:
        return redirect(url_for('login',methods=['GET', 'POST']))'''
    return render_template('home.html', error=error, dumb=dumb, posts=postlist)


@app.route('/register')#, methods=['GET', 'POST'])
def register():
    """
    pass
    """
    return render_template('register_user.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/setUsername',methods=['GET', 'POST'])
def set_username():
    print("username set")
    #form = user_form(request.form)
    session['username'] = request.form['username']
    print(session['username'])
    response = {"data": "ok"}
    return jsonify(response)


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.clear()
    return redirect(url_for('index'))


@app.route('/profile/<id>',methods=['GET', 'POST'])
def profile(id):
    if id=="myself":
        if 'username' not in session:
            print("aaaaaa")
        print(session['username'])
        user = User(firebase.get('/users/' + session['username'], None))
        user.department=Utils.short([user.department])[0]
        return render_template('profile.html',user=user,edit=True)
    user=User(firebase.get('/users/'+id,None))
    postlist = []
    result = firebase.get('/posts', None)
    for key, value in result.items():
        postlist.append(Posts(key, value).getShowable())
    postlist=[post for post in postlist if post.authorId==id]
    return render_template('profile.html',user=user,edit=False,posts=postlist)
import Utils

@app.route('/getUUID',methods=['GET'])
def get_UUID():
    return uuid.uuid4().__str__()

@app.route('/editProfile',methods=['GET', 'POST'])
def edit_profile():
    user = User(firebase.get('/users/' +session['username'], None))
    halls = Utils.getHalls()
    departments=Utils.getFacultywiseDepartments()
    faculties = departments.keys()
    print(departments)
    userFaculty=Utils.getFacultyFromDepartment(user.department)
    user.department=Utils.resolve(user.department)
    print(userFaculty)
    if "faculty" in request.form:
        faculty=request.form['faculty']
        print(request.form)
        print(faculty)
        departments=departments[faculty]
        return jsonify(departments)
    try:
        departments=departments[userFaculty]
    except:
        departments=[]
    print(user.department)
    return render_template('edit_profile.html',user=user,halls=halls,faculties=faculties,departments=departments,userFaculty=userFaculty)

@app.route('/submitProfile',methods=['GET', 'POST'])
def submit_profile():
    print( session['username'],request.form)
    user = dict(firebase.get("/users/" + session['username'], None))
    for key,value in dict(request.form).items():
        if type(value)==list:
            print("list",value)
            value=value[0]
        if value is not None and len(value)>0:
            user[key] = value
    print(dict(request.form))
    print("pushed",user)
    firebase.put("/users/",session['username'],user)
    firebase.put("/profiles/",session['username'],Profile(user).__dict__)
    return jsonify("change","ok")




class PasswordForm(Form):
    password = StringField('Password')


@app.route('/post')
def post():
    return render_template('post.html')


if __name__ == '__main__':
    app.secret_key = 'SUPER SECRET KEY'
    app.config['SESSION_TYPE'] = 'filesystem'
    # sess.init_app(app) # uncomment this

    app.debug = True
    app.run()
