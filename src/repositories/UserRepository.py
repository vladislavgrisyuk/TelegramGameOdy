from models import UserModel
from dbcontext import MongoContext
from models import UserModel
from dbcontext.Schemas import UserDocument
from bson import ObjectId
db = MongoContext()


class UserRepository:
    def __init__(self):
        pass
    
    def getUserByTelegramId(self, telegramId:int) -> UserModel:
        usDoc:UserDocument = UserDocument.objects(telegramId=telegramId).first()
        usModel:UserModel = UserModel(
            usDoc.id,
            'name',
            usDoc.level,
            usDoc.attack,
            usDoc.defense,
            usDoc.stamina,
            usDoc.money,
            usDoc.health,
            usDoc.exp,
        )
        
        return usModel
    
    def AddItem(self, userId:int, objectId:str):
        user:UserDocument = UserDocument.objects(telegramId=userId).first()
        if(user):
            user.items.append(ObjectId(objectId))
            user.save()
            
        
            
    
    
    