# from flask import Flask,render_template,request,redirect,url_for
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///codes.db"
# db=SQLAlchemy(app)
# def create_db():
#     with app.app_context():

#         db.create_all()
# class Users(db.Model):
#         __tablename__="Sellers"
#         id=db.Column(db.Integer,primary_key=True,autoincrement=True)
#         Email=db.Column(db.String)
#         name=db.Column(db.String)
#         number=db.Column(db.String,unique=True)
#         password=db.Column(db.String)
#         def __repr__(self):
#             return '<python_code %r>' % self.id

# # @app.route('/')
# # def hello():
# #     return render_template("hello.html")
# # # Route for handling the login page logic
# # @app.route('/home/<name>')
# # def home(name):
# #     return f'{name['username']}'
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         d=request.form
#         # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#         #     error = 'Invalid Credentials. Please try again.'
#         # else:
#         #     # return redirect(url_for('home',name=d))
#         return d
           
#     return render_template('login.html', error=error)

# if __name__=="__main__":
#     create_db()
#     app.run(debug=True)
from flask import Flask,request,render_template,redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///database.db'
db=SQLAlchemy(app)
app.secret_key='secret_key'

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String[100], nullable=False)
    email=db.Column(db.String[100],unique=True)
    password=db.Column(db.String[100])
    def __init__(self,email,password,name):
        self.name=name
        self.email=email
        salt = bcrypt.gensalt()
        self.password=bcrypt.hashpw(password.encode('utf-8'),salt)
        
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password)
        # Example usage
        

        
with app.app_context():
    db.create_all()
@app.route("/error01")
def error01():
    return "Error01"
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        new_user=User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return render_template("login.html")
        # return request.form
    return render_template("register.html")
    # return "registre"
@app.route("/login",methods=['GET','POST'])
def login():
     if request.method=='POST':
        # name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['name']=user.name
            session['email']=user.email
            return redirect('/dashboard')
            # return redirect("/")
     return render_template("login.html")
        # return redirect("/error01")
@app.route('/dashboard')
def dashboard():
    if session['name']:
        return render_template('dashboard.html')
    return render_template('/login')
