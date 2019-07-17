from step_1 import transform_products_to_list

def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)
    results = {}
    
    for product in products_list:
        customer_id = product[-2]
        invoice_id = product[0]
        price = float(product[-3])
        quantity = int(product[3])
        total = round(price * quantity, 3)
        
        results.setdefault(customer_id, {})
        results[customer_id].setdefault(invoice_id, 0)
        results[customer_id][invoice_id] += total
        
    return results