import bcrypt
class User():
    def __init__(self,pwd) :
         self.pwd=pwd
         print(self,pwd)
    def make_password_hash(self):
            self.hash = bcrypt.hashpw(password=self.pwd.encode('utf-8'), salt=bcrypt.gensalt())
            # hash=password
            # return hash.decode('utf-8')
            # return self.hash

    def is_password_valid(self,newpwd):
        return bcrypt.checkpw(newpwd.encode('utf-8'), self.hash)

user=User("password1")
user.make_password_hash()
print(user.is_password_valid("password1"))