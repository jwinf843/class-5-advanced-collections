from step_1 import transform_products_to_list
from data import products_string
from pprint import pprint

def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)
    results = {}
    
    for product in products_list:
        customer_id = product[-2]
        invoice_id = product[0]
        
        results.setdefault(customer_id, {})
        results[customer_id].setdefault(invoice_id, [])
        results[customer_id][invoice_id].append(product)
    
    return results
    
    
'''
results = {
    customer_id = {
        invoice_id = [
            products
        ]
    }
}

results = {customer_id: {invoice_id: []}}
'''

products = group_products_by_customer_and_invoice(products_string)
# # pprint(products)
# customer = products['17850']
# # pprint(customer)
# invoice = customer['536365']
# # pprint(invoice)
# transaction = invoice[0]
# # pprint(transaction)
# name = transaction[2]
# # pprint(name)
# our_list = name.split(' ')
# # pprint(our_list)
# heart = our_list[2]
# # pprint(heart)
# art = heart[2:]
# pprint(art)

print(products['17850']['536365'][0][2].split(' ')[2][2:])
transaction = products['17850']['536365'][0]
our_list = transaction[2].split(' ')
art = our_list[2][2:]
