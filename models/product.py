#!/usr/bin/python3
""" Product Module for HBNB project """
from models.base_model import BaseModel


class Product(BaseModel):
    """ A product to stay """
    product_id = ""
    user_id = ""
    name = ""
    description = ""
    number_pieces = 0
    price = 0
