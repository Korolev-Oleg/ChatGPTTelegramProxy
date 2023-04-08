from datetime import datetime
import peewee

db = peewee.SqliteDatabase("db.sqlite3")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField(max_length=256, unique=True)
    first_name = peewee.CharField(max_length=256)
    last_name = peewee.CharField(max_length=256)
    has_access = peewee.BooleanField(default=False)
    _raw_data_ = peewee.TextField()


class Message(BaseModel):
    created_at = peewee.DateTimeField(default=datetime.now)
    sender = User(backref="messages")
    text = peewee.TextField()
    gpt_response = peewee.TextField()


def create_all():
    try:
        db.connect()
        db.create_tables([User, Message])
        db.close()
    except peewee.ImproperlyConfigured:
        print("Database is already created")
