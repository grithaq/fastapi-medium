from entity import Todo


class TodoRepository():
    todos = []

    def get(self):
        return self.todos
    
    def add(self, todo):
        t = Todo()
        t.id = todo['id']
        t.title = todo['title']
        t.description = todo['description']
        t.categories = todo['categories']
        t.user_id = todo['user_id']
        self.todos.append(t)
        return self.todos
    
    def update(self, id, todo):
        for index, td in enumerate(self.todos):
            if td.id == int(id):
                t = Todo()
                t.id = todo['id']
                t.title = todo['title']
                t.description = todo['description']
                t.categories = todo['categories']
                t.user_id = todo['user_id']
                self.todos[index] = t
                return self.get()
        return self.todos
    
    def delete(self, id):
        for index, td in enumerate(self.todos):
            if td.id == int(id):
                del self.todos[index]
                return self.get()
            return "Todo not found"


db_todo = TodoRepository()