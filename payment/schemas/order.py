from models.order import Order

def order_schema(order):
    return {
        'id': order.pk,
        'product_id': order.product_id,
        'price': order.price,
        'fee': order.fee,
        'total': order.total,
        'quantity': order.quantity,
        'status': order.status
    }

def order_schema_list(orders):
    order_list = []
    for pk in orders:
        order = Order.get(pk)
        order_list.append(order_schema(order))
    return order_list