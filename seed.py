from app import app
from models import db, User, Feedback


db.drop_all()
db.create_all()


from app import app
from models import db, User, Feedback


db.drop_all()
db.create_all()

u1 = User(
    username="Marcus83",
    password="Rogeram25",
    email="marcusclemmons1@gmail.com",
    first_name="Marcus",
    last_name="Clemmons"
)

u2 = User(
    username="Andre83",
    password="Mildredk29",
    email="mackingmark1@gmail.com",
    first_name="Andre",
    last_name="Clemmons"
)

db.session.add_all([u1, u2])
db.session.commit()



f1 = Feedback(
    title="What happen",
    content="What is wrong with the world",
    username="Marcus83"

)

f2 = Feedback(
    title="Its right here",
    content="Going to take over the world",
    username="Andre83"

)