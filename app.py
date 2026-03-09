from flask import Flask, render_template, request , url_for , redirect
from models import db
import sqlite3
app = Flask(__name__)


#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# connect(db -- app) , Edit , create if not exists
db.init_app(app)
app.app_context().push()
db.create_all()   #create / update the database




def get_current_user():
    user = None
    return user


#--------------------------------------------------------------------------          
@app.route('/')
def home():
    user = get_current_user()
    return render_template('home.html' , user = user)

@app.route('/access' )
def access():
    return render_template('access.html')

#--------------------------------------------------------------------------
@app.route('/login' , methods = ['POST'])
def login():
    name = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    return redirect(url_for('home'))

@app.route('/register' , methods = ['POST'])
def register():
    name = request.form.get('username')
    email = request.form.get('email')   
    password = request.form.get('password')
    password2 = request.form.get('password2')
    return redirect(url_for('access'))
#--------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True )