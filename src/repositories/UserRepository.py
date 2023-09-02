from models import UserModel

__users__ = []
__users__.append(UserModel(380472185, 'enmu', 23))
__users__.append(UserModel(2, 'jezus', 4))
__users__.append(UserModel(3, 'marley', 1))


class UserRepository:
    def __init__(self):
        pass
    
    def getUserById(self, id: int) -> UserModel:
        #return [e for e in __users__ if e.id == id]
        return next(filter(lambda x: x.id == id, __users__))
    
    