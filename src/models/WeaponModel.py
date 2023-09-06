class WeaponModel:
    def __init__(self, 
                 id: str,
                 weaponId: str,
                 attack: int,
                 defense: int,
                 price: int,
                 name:str
                 ):
        self.id = id
        self.price = price
        self.weaponId = weaponId
        self.attack = attack
        self.defense = defense
        self.name = name
        
    