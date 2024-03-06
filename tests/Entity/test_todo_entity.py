from app.entity.todo import Todo


def test_todo_entity():
    todo = Todo()
    todo.id = 1
    todo.title = "Todo ke 1"
    todo.description = "Todo 1 desc"
    todo.user_id = 1
    assert todo
    assert todo.id == 1
    assert todo.title == "Todo ke 1"
    assert todo.description == "Todo 1 desc"
    assert todo.user_id == 1
