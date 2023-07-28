import datetime

def get_product_dict():
    product_dict = {}
    with open('../master_data/product_master.csv') as f:
        products = f.readlines()[1:]
        for product in products:
            product_dict[product.split(',')[0]] = product.split(',')[2]
        return product_dict


def validate_sales(order):
    product_dict = get_product_dict()
    if order['product_id'] in product_dict.keys():
        return int(product_dict[order['product_id']]) * int(order['quantity']) == int(order['sales'])


def validate_product_id(id, products):
    if id in products:
        return True
    return False


def validate_order_date(date):
    dt = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    today_date = datetime.date.today()
    delta = (today_date - dt).days
    if delta >= 0:
        return True
    return False


def validate_city(city):
    if city in ['Mumbai', 'Bangalore']:
        return True
    return False


def validate_emptiness(orders):
    empty_cols = []
    for k, v in orders.items():
        if not orders[k] or orders[k] == '':
            empty_cols.append(k)
    return empty_cols


def read_master_data():
    product_list = []
    with open('../master_data/product_master.csv') as f:
        products = f.readlines()[1:]
        for product in products:
            product_list.append(product.split(',')[0])
        return product_list
