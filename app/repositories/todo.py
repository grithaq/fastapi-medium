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
        t.user = todo['user']
        self.todos.append(t)
        return self.todos


db_todo = TodoRepository()