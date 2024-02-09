import json
import os
from copy import deepcopy


def names_parser(file_name: str = None):
    '''Function that takes the JSON data as input and returns a list of names of all products.'''
    parsed_json = parse_json_file(file_name)
    products_list = []
    if parsed_json is not None:
        products = parsed_json["products"]
        for product in products:
            products_list.append(product.get("name"))
        return products_list


def price_threshold_parser(price_threshold=None, file_name: str = None):
    '''Function that takes the JSON data as input and a price threshold, and returns a list of products which price is greater than or equal to the threshold.'''
    parsed_json = parse_json_file(file_name)
    if not price_threshold:
        price_threshold = input("Enter price threshold (please, use format 123,456.908):")
    try:
        if isinstance(price_threshold, str):
            price_threshold.replace(",", "")
        price_threshold = float(price_threshold)
        if parsed_json is not None:
            products = parsed_json["products"]
            parsed_products = deepcopy(products)
            removed_products_count = 0
            for index, product in enumerate(products):
                product_price = product.get("price")
                if product_price < price_threshold:
                    parsed_products.pop(index - removed_products_count)
                    removed_products_count += 1
            if len(parsed_products) == 0:
                print("Price threshold is too high: empty list is returned")
            return parsed_products
    except ValueError:
        print("Entered price threshold is not a number.")


def parse_json_file(file_name: str = None):
    '''Function that takes the JSON data as input and returns suitable python variables.'''
    if not file_name:
        file_name = input("enter filename:")
    if file_name.split(".")[-1] != "json":
        file_name += ".json"
    project_name = os.getcwd()
    path_to_json = os.path.join(os.path.expanduser("~"), project_name, file_name)
    try:
        with open(path_to_json, "r") as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print("No such file in project's directory.")
