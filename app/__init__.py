from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///codes.db"
db=SQLAlchemy(app)
def create_db():
    with app.app_context():

        db.create_all()
class Users(db.Model):
        __tablename__="Sellers"
        id=db.Column(db.Integer,primary_key=True,autoincrement=True)
        Email=db.Column(db.String)
        name=db.Column(db.String)
        number=db.Column(db.String,unique=True)
        password=db.Column(db.String)
        def __repr__(self):
            return '<python_code %r>' % self.id

# @app.route('/')
# def hello():
#     return render_template("hello.html")
# # Route for handling the login page logic
# @app.route('/home/<name>')
# def home(name):
#     return f'{name['username']}'
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        d=request.form
        # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        #     error = 'Invalid Credentials. Please try again.'
        # else:
        #     # return redirect(url_for('home',name=d))
        return d
           
    return render_template('login.html', error=error)

if __name__=="__main__":
    create_db()
    app.run(debug=True)