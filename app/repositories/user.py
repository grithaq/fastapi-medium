from entity import User


class UserRepository:
    users = []

    def get(self):
        return self.users
    
    def get_user_by_id(self, user_id: str):
        for u in self.users:
            if u.id == user_id:
                return u
    
    def add(self, user):
        user_model = User()
        user_model.id = user["id"]
        user_model.username = user["username"]
        user_model.email = user["email"]
        user_model.password = user["password"]
        user_model.disabled = False
        self.users.append(user_model)
        return user_model
    
    def update(self, id: str, user):
        for index, usr in enumerate(self.users):
            if usr['id'] == int(id):
                self.users[index] = user
                return self.get()
        return "User not found"
    
    def delete(self, id: str):
        for index, user in enumerate(self.users):
            if user['id'] == int(id):
                del self.users[index]
                return self.get()
        return "User not found"
    

db_users = UserRepository()