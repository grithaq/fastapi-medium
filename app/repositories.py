from schema import (
    ListProduct as ListProductSchema,
    ListUserSchema, UserSchema,
    ListCategorySchema, CategorySchema
    )


class Product():

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ListProduct():
    products = []

    def get_products(self):
        list_product_schema = ListProductSchema(products=self.products)
        return list_product_schema.model_dump(mode='json')
    
    def add_product(self, product: Product):
        self.products.append(product.model_dump(exclude_unset=True))
        return self.get_products()
    
    def update_product(self, prod_id: str, product: Product):
        product = product.model_dump(exclude_unset=True)
        for index, prd in enumerate(self.products):
            if prd['id'] == int(prod_id):
                self.products[index] = product
                return "Data was updated"
        return "Product not found"
    
    def delete_product(self, id: str):
        for index, product in enumerate(self.products):
            if product['id'] == int(id):
                del self.products[index]
                return "Data was deleted"
        return "Product not found"
    

class ListUsers():
    users = []

    def get_users(self):
        user_schema_serializer = ListUserSchema(users=self.users)
        return user_schema_serializer.model_dump(mode='json')
    
    def add_user(self, user: UserSchema):
        self.users.append(user.model_dump(exclude_unset=True))
        return self.get_users()
    
    def update_user(self, id: str, user: UserSchema):
        user = user.model_dump(exclude_unset=True)
        for index, usr in enumerate(self.users):
            if usr['id'] == int(id):
                self.users[index] = user
                return self.get_users()
        return "User not found"
    
    def delete_user(self, id: str):
        for index, user in enumerate(self.users):
            if user['id'] == int(id):
                del self.users[index]
                return self.get_users()
        return "User not found"
    

class ListCategory():
    categories = []

    def get_all_categories(self):
        category_deserializer = ListCategorySchema(categories=self.categories)
        return category_deserializer.model_dump(mode='json')
    
    def add_category(self, category: CategorySchema):
        self.categories.append(category.model_dump(exclude_unset=True))
        return self.get_all_categories()
    
    def update_category(self, id: str, category: CategorySchema):
        category = category.model_dump(exclude_unset=True)
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