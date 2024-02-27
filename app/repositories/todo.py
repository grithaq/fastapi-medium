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
        print(id)
        print(self.todos)
        print
        print(todo)


db_todo = TodoRepository()