from models.product import Product

def product_schema(product):
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'stock': product.stock
    }

def product_schema_list(products):
    product_list = []
    for pk in products:
        product = Product.get(pk)
        product_list.append(product_schema(product))
    return product_list