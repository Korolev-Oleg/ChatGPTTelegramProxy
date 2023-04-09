from datetime import datetime

import peewee

db = peewee.SqliteDatabase("db.sqlite3")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    username = peewee.CharField(max_length=256, unique=True)
    first_name = peewee.CharField(max_length=256, null=True)
    last_name = peewee.CharField(max_length=256, null=True)
    has_access = peewee.BooleanField(default=False)
    _raw_data_ = peewee.TextField()

    def get_messages(self, limit=None):
        return Message.select().where(Message.sender == self).order_by(
            Message.created_at.desc()
        ).limit(limit)

    def get_messages_count(self):
        return Message.select().where(Message.sender == self).count()

    def create_message(self, question, answer):
        return Message.create(
            sender=self,
            question=question,
            answer=answer,
        )


class Message(BaseModel):
    created_at = peewee.DateTimeField(default=datetime.now)
    sender = peewee.ForeignKeyField(User, backref="messages")
    question = peewee.TextField()
    answer = peewee.TextField()

    @staticmethod
    def get_count(user):
        return Message.select().where(Message.sender == user).count()


def create_all():
    try:
        db.connect()
        db.create_tables([User, Message])
        db.close()
    except peewee.ImproperlyConfigured:
        print("Database is already created")
