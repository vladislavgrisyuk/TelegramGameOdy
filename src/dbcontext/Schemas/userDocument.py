from mongoengine import connect, Document, StringField, IntField


class UserDocument(Document):
    telegramId = IntField(unique = True)
    name = StringField()