from mongoengine import connect, Document, StringField, IntField
from .Schemas import UserDocument
from models import UserModel

class MongoContext:
    def connect(self):
        connect(db='testdb', host='127.0.0.1', port=27017)
        
    def getUserByTelegramId(self, id:int) -> UserModel:
        return UserDocument.objects.get(name='Vladik')