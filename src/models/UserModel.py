class UserModel:
    def __init__(self, 
                 id: int, 
                 name: str, 
                 level: int, 
                 attack : int, 
                 defense : int,
                 stamina : int,
                 money : int, 
                 health : int,
                 exp : int):
        self.id = id
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.stamina = stamina
        self.money = money
        self.health = health
        self.exp = exp
        
    