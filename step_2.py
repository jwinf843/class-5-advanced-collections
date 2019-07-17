from step_1 import transform_products_to_list
# from step_1 import products_list

def group_products_by_customer(products_string):
    products_list = transform_products_to_list(products_string)
    results = {}
    
    for product in products_list:
        customer_id = product[-2]
        
        results.setdefault(customer_id, [])
        results[customer_id].append(product)
    
    return results
        
        
'''
results = {
    customer_id: []
}

results[customer_id]
'''