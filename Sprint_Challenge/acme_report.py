import random
from acme import Product

# Useful to use with random.sample or random.choice to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        price = random.randint(5,100)
        weight = random.randint(5,100)
        flammability = random.uniform(0.0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products

def inventory_report(products):
    unique_product_names = len(set([product.name for product in products]))
    average_price = sum([product.price for product in products]) / len(products)
    average_weight = sum([product.weight for product in products]) / len(products)
    average_flammability = sum([product.flammability for product in products]) / len(products)

    return (unique_product_names, average_price, average_weight, average_flammability)

if __name__ == '__main__':
    print(inventory_report(generate_products()))