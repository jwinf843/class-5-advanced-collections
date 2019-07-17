from data import products_string

def transform_products_to_list(products_string):
    products_splot = products_string.split('\n')
    results = []
    
    for product in products_splot:
        if product:
            clean_product = product.split(',')
            results.append(clean_product)
    
    return results

products_list = transform_products_to_list(products_string)