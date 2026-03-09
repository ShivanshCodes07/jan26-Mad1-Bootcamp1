from flask_sqlalchemy import SQLAlchemy # class


db = SQLAlchemy() #instance/object of the class


class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(100) , nullable = False)
    email = db.Column(db.String(100) , nullable = False , unique = True)
    password = db.Column(db.String(100) , nullable = False)

     
    #Roles
    isUser = db.Column(db.Boolean , default = True)
    isCreater = db.Column(db.Boolean , default = False)
    isAdmin = db.Column(db.Boolean , default = False)

    #Is User Blacklisted
    isBlacklisted = db.Column(db.Boolean , default = False)
