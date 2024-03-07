from app.repositories.category import db_categories


def test_add_category():
    data = {
        "id": 1,
        "name": "Learning",
    }
    categories = db_categories.add(1, data)
    print(categories)
    assert categories[0].user_id == 1
    assert categories[0].__dict__ == {"id": 1, "name": "Learning", "user_id": 1}


def test_get_categories():
    categories = db_categories.get(1)
    assert categories
    assert categories[0].user_id == 1
    assert categories[0].__dict__ == {"id": 1, "name": "Learning", "user_id": 1}


def test_update_category():
    data_updated = {"id": 1, "name": "New learning", "user_id": 1}
    categories = db_categories.update(1, 1, data_updated)
    assert categories[0].__dict__ == data_updated


def test_delete_category():
    categories = db_categories.delete("1", 1)
    assert categories == []
