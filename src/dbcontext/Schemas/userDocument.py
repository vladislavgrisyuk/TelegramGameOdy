from mongoengine import connect, Document, StringField, IntField, ListField, ReferenceField, DateTimeField

class Weapon(Document):
    name = StringField()
    description = StringField()
    attack = IntField()
    defense = IntField()
    weaponId = StringField()
    price = IntField()
    
    
class UserDocument(Document):
    telegramId = IntField(unique = True)
    name = StringField()
    level = IntField()
    exp = IntField()
    attack = IntField()
    defense = IntField()
    stamina = IntField()
    money = IntField()
    health = IntField()
    mainWeapon = ReferenceField(Weapon)
    secondaryWeapon = ReferenceField(Weapon)
    items = ListField()