from schema import ListProduct as ListProductSchema


class Product():

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ListProduct():
    products = [
        {
            "id": 1,
            "name": "Bakwan",
            "price": 1000
        }
    ]

    def get_products(self):
        list_product_schema = ListProductSchema(products=self.products)
        return list_product_schema.model_dump(mode='json')
    
    def add_product(self, product: Product):
        self.products.append(product.model_dump(exclude_unset=True))
        return self.get_products()
    
    def update_product(self, prod_id: str, product: Product):
        product = product.model_dump(exclude_unset=True)
        for index, prd in enumerate(self.products):
            if prd['id'] == int(prod_id):
                self.products[index] = product
                return "Data was updated"
        return "Product not found"
    

db_products = ListProduct()