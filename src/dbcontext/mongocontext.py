from mongoengine import connect, Document, StringField, IntField
from .Schemas import UserDocument, Weapon
from models import UserModel, WeaponModel

class MongoContext:
    def connect(self):
        connect(db='testdb', host='127.0.0.1', port=27017)
        
    def getUserByTelegramId(self, telegramId:int) -> UserDocument:
        return UserDocument.objects.get(telegramId=telegramId)
    
    def getWeapons(self, weaponId = ''):
        if weaponId == '':
            return Weapon.objects()
        
        return Weapon.objects(weaponId=weaponId).first()
    
    def getWeaponModel(self, weaponId) -> WeaponModel:
        wp:Weapon = Weapon.objects(weaponId=weaponId).first()
        if(wp):
            weaponModel = WeaponModel(wp.id, wp.weaponId, wp.attack, wp.defense, wp.price, wp.name)
            return weaponModel
    