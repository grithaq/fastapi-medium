from entity import Category


class CategoryRepository:
    categories = []

    def get(self, user_id):
        return [c for c in self.categories if c.user_id == user_id]

    def add(self, user_id, category):
        category_entity = Category()
        category_entity.id = category["id"]
        category_entity.name = category["name"]
        category_entity.user_id = user_id
        self.categories.append(category_entity)
        return self.categories

    def update(self, user_id: int, id: str, category):
        category_entity = Category()
        category_entity.id = category["id"]
        category_entity.name = category["name"]
        category_entity.user_id = user_id
        for index, cat in enumerate(self.categories):
            if cat.id == int(id):
                self.categories[index] = category_entity
                return self.get(user_id)
        return "Category not found"

    def delete(self, id: str, user_id: int):
        for index, category in enumerate(self.categories):
            if category.id == int(id):
                del self.categories[index]
                return self.get(user_id)
        return "Category not found"


db_categories = CategoryRepository()
