from schema import ListProduct as ListProductSchema


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
    

db_products = ListProduct()