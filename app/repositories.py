class ListProduct():
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
    

class ListUsers():
    users = [
        {'id': 1, "name": "grithaq", "email": "grithaq@gmail.com"},
        {'id': 2, "name": "lutfi", "email": "lutfi@gmail.com"},
        {'id': 1, "name": "olan", "email": "olan@gmail.com"}
    ]

    def get_users(self):
        return self.users
    
    def add_user(self, user):
        self.users.append(user)
        return self.get_users()
    
    def update_user(self, id: str, user):
        for index, usr in enumerate(self.users):
            if usr['id'] == int(id):
                self.users[index] = user
                return self.get_users()
        return "User not found"
    
    def delete_user(self, id: str):
        pass
        # for index, user in enumerate(self.users):
        #     if user['id'] == int(id):
        #         del self.users[index]
        #         return self.get_users()
        # return "User not found"
    

class ListCategory():
    categories = []

    def get_all_categories(self):
        return self.categories
        # category_deserializer = ListCategoryResponse(
        #     categories=self.categories
        #     )
        # return category_deserializer.model_dump(mode='json')
    
    def add_category(self, category):
        self.categories.append(category)
        return self.categories
    
    def update_category(self, id: str, category):
        for index, cat in enumerate(self.categories):
            if cat['id'] == int(id):
                self.categories[index] = category
                return self.get_all_categories()
        return "Category not found"
    
    def delete_category(self, id: str):
        for index, category in enumerate(self.categories):
            if category['id'] == int(id):
                del self.categories[index]
                return self.get_all_categories()
        return "Category not found"


db_categories = ListCategory()
db_products = ListProduct()
db_users = ListUsers()