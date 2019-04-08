import datetime
import os
import time
from firebase import firebase
from posts import Posts
from flask import Flask, render_template, request
from user import User
from flask import flash
from flask import redirect, url_for, session, Session
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import Form, IntegerField, StringField, PasswordField, validators
from wtforms.fields import SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from forms import IssueForm, CommentForm,UploadForm,graph_input,create_article_form,LoginForm,RegisterForm
app = Flask(__name__)
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}
ALLOWED_CATEGORY = {'ACM', 'IOI'}
import uuid

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
firebase=firebase.FirebaseApplication('https://fir-basic-9a5d7.firebaseio.com/')
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
ckeditor = CKEditor(app)

app.secret_key = "super secret key"
sess = Session()

@app.route('/')
def index():
    postlist = []
    result = firebase.get('/posts', None)
    for key,value in result.items():
        postlist.append(Posts(key,value).getShowable())
    print(postlist[0].comments[0])

    error = 'You are not logged in'
    dumb = 'dumb'
    # if 'username' in session:
    #     msg = 'You are Logged in as ' + session['username']
    #     return render_template('home.html', msg=msg, posts=list)
    return render_template('home.html', error=error, dumb=dumb, posts=postlist)


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
   pass
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.clear()
    return redirect(url_for('index'))

@app.route('/profile/<id>',methods=['GET', 'POST'])
def profile(id):
    user=User(firebase.get('/users/'+id,None))
    print(user)
    return render_template('profile.html',user=user)
#
#
# @app.route('/posts/<id>')
# def posts(id):
#     if not ('username' in session):
#         return redirect(url_for('login'))
#
#     from profile import profilePostCall
#     post_array,user=profilePostCall(id)
#     return render_template('user_post.html', post_array=post_array,user=user)
#
#



@app.route('/user/<userName>',methods=['GET', 'POST'])
def userProfile(userName):
    class User:
        def __init__(self, name, username, mail):
            self.name = name
            self.username = username
            self.mail = mail
    users = ''
    existing_user = users.find_one({'USERNAME': userName})
    print("exist",existing_user,userName)
    user = User(existing_user['NAMES'], existing_user['USERNAME'], existing_user['MAIL'])
    return render_template('profile.html', user=user)

class PasswordForm(Form):
    password = StringField('Password')


if __name__ == '__main__':
    app.secret_key = 'SUPER SECRET KEY'
    app.config['SESSION_TYPE'] = 'filesystem'
    # sess.init_app(app) # uncomment this

    app.debug = True
    app.run()
