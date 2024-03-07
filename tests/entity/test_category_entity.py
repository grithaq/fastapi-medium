from app.entity.category import Category


def test_category_entity():
    category = Category()
    category.id = 1
    category.name = "Learning"
    category.user_id = 1
    assert category
    assert category.id == 1
    assert category.name == "Learning"
