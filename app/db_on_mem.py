from schema import ListProduct as ListProductSchema, Product as ProductSchema


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
    
    def add_product(self, product: Product):
        self.products.append(product.model_dump(exclude_unset=True))
        return self.get_products()
    

db_products = ListProduct()