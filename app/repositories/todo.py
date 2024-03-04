from entity import Todo


class TodoRepository():
    todos = []

    def get(self):
        return self.todos
    
    def add(self, user_id, todo):
        t = Todo()
        t.id = todo['id']
        t.title = todo['title']
        t.description = todo['description']
        t.categories = todo['categories']
        t.user_id = user_id
        self.todos.append(t)
        return self.todos
    
    def update(self, id, user_id, todo):
        for index, td in enumerate(self.todos):
            if td.id == int(id):
                t = Todo()
                t.id = todo['id']
                t.title = todo['title']
                t.description = todo['description']
                t.categories = todo['categories']
                t.user_id = user_id
                self.todos[index] = t
                return td
    
    def delete(self, id):
        for td in self.todos:
            if td.id == int(id):
                self.todos.remove(td)
                return td


db_todo = TodoRepository()