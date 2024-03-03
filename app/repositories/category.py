from entity import Category


class CategoryRepository():
    categories = []

    def get(self):
        return self.categories
    
    def add(self,user_id, category):
        category_entity = Category()
        category_entity.id = category["id"]
        category_entity.name = category["name"]
        category_entity.user_id = user_id
        self.categories.append(category)
        return self.categories
    
    def update(self, id: str, category):
        category_entity = Category()
        category_entity.id = category["id"]
        category_entity.name = category["name"]
        for index, cat in enumerate(self.categories):
            if cat['id'] == int(id):
                self.categories[index] = category
                return self.get()
        return "Category not found"
    
    def delete(self, id: str):
        for index, category in enumerate(self.categories):
            if category['id'] == int(id):
                del self.categories[index]
                return self.get()
        return "Category not found"
    
    
db_categories = CategoryRepository()
