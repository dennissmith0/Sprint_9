import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_weight():
    '''Test default product weight being 20.'''
    prod = Product('Test Product')
    assert prod.weight == 20


def test_default_product_flammability():
    '''Test default product flammability being 0.5.'''
    prod = Product('Test Product')
    assert prod.flammability == 0.5


def test_stealability_method():
    '''Test stealability method'''
    prod = Product('Test Product', price=10, weight=20)
    assert prod.stealability() == 'Kinda stealable.'


def test_explode_method():
    '''Test stealability method'''
    prod = Product('Test Product', weight=20, flammability=4)
    assert prod.exolode() == "...BABOOM!!"


def test_default_generate_products():
    '''Test default generate_products() function.'''
    products = generate_products()
    assert len(products) == 30

    for product in products:
        assert isinstance(product, Product)
        assert product.name.split(' ')[0] in ADJECTIVES
        assert product.name.split(' ')[1] in NOUNS
        assert 5 <= product.price <= 100
        assert 5 <= product.weight <= 100
        assert 0.0 <= product.flammability < 2.5
