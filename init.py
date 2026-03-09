from app import app , db
from models import User

# Cretae 1 Admin

admin = User(
    username = 'admin',
    email = 'admin@admin.com',
    password = 'adminpass',
    isUser = True,
    isCreater = True,
    isAdmin = True
)
db.session.add(admin)
db.session.commit()


# create 3 users
for i in range(1,4):
    user = User(
        username = f'user{i}',
        email = f'user{i}@gmail.com',
        password = f'userpass{i}',
        isUser = True,  
        isCreater = False,
        isAdmin = False
    )
    db.session.add(user)
    db.session.commit()

# Create 3 Creators

for i in range(1,4):
    creater = User(
        username = f'creater{i}',
        email = f'creater{i}@gmail.com',
        password = f'createrpass{i}',
        isUser = False,
        isCreater = True,
        isAdmin = False
    )
    db.session.add(creater)
    db.session.commit()

