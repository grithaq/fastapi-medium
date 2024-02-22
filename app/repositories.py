from entity import User, Category, Todo


class ProductRepository:
    products = []

    def get_products(self):
        pass
    
    def add_product(self, product):
        pass
    
    def update_product(self, prod_id: str, product):
        pass
        # product = product.model_dump(exclude_unset=True)
        # for index, prd in enumerate(self.products):
        #     if prd['id'] == int(prod_id):
        #         self.products[index] = product
        #         return "Data was updated"
        # return "Product not found"
    
    def delete_product(self, id: str):
        # for index, product in enumerate(self.products):
        #     if product['id'] == int(id):
        #         del self.products[index]
        #         return "Data was deleted"
        # return "Product not found"
        pass
    

class UserRepository:
    users = []

    def get(self):
        return self.users
    
    def add(self, user):
        user_model = User()
        user_model.id = user.id
        user_model.name = user.name
        self.users.append(user)
        return self.users
    
    def update(self, id: str, user):
        for index, usr in enumerate(self.users):
            if usr['id'] == int(id):
                self.users[index] = user
                return self.get_users()
        return "User not found"
    
    def delete(self, id: str):
        pass
        # for index, user in enumerate(self.users):
        #     if user['id'] == int(id):
        #         del self.users[index]
        #         return self.get_users()
        # return "User not found"
    

class CategoryRepository(): #crud
    categories = []

    def get(self):
        return self.categories
    
    def add(self, category):
        self.categories.append(category)
        return self.categories
    
    def update(self, id: str, category):
        for index, cat in enumerate(self.categories):
            if cat['id'] == int(id):
                self.categories[index] = category
                return self.get_all_categories()
        return "Category not found"
    
    def delete(self, id: str):
        for index, category in enumerate(self.categories):
            if category['id'] == int(id):
                del self.categories[index]
                return self.get_all_categories()
        return "Category not found"


db_categories = CategoryRepository()
db_products = ProductRepository()
db_users = UserRepository()