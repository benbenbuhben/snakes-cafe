from .order_class import Order
import pytest
import os


@pytest.fixture
def sample_order():
    return Order(available_items)


def test_this_file_works():
    pass


def test_order_module_exists():
    return Order


def test_sample_order_exists(sample_order):
    return sample_order


def test_default_properties(sample_order):
    assert sample_order.total == 0
    assert sample_order.text == ''
    assert sample_order.available_items == available_items


def test_add_item_successful(sample_order):
    pass


def test_remove_item_successful(sample_order):
    pass


def test_update_total_adds_to_total(sample_order):
    pass


def test_display_order_returns_formatted_order(sample_order):
    pass


def print_receipt_writes_new_file(sample_order):
    """Maybe need to use some kind of mock technique
    """
    pass


def test_length_returns_number_of_items_in_order(sample_order):
    pass


def test_print_prints_correct_format_to_std_out(sample_order):
    pass


available_items = {'1': {'item': 'Wings', 'cost': 7, 'quantity': 1000}, '2': {'item': 'Cookies', 'cost': 3, 'quantity': 1000}, '3': {'item': 'Spring Rolls', 'cost': 5, 'quantity': 1000}, '4': {'item': 'Rocky Mtn Oysters', 'cost': 8, 'quantity': 1000}, '5': {'item': 'Awesome Blossom Possom', 'cost': 10, 'quantity': 1000}, '6': {'item': 'Salmon', 'cost': 15, 'quantity': 1000}, '7': {'item': 'Steak', 'cost': 18, 'quantity': 1000}, '8': {'item': 'Meat Tornado', 'cost': 12, 'quantity': 1000}, '9': {'item': 'A Literal Garden', 'cost': 10, 'quantity': 1000}, '10': {'item': 'Vegan Mush', 'cost': 11, 'quantity': 1000}, '11': {'item': 'Chicken', 'cost': 11, 'quantity': 1000}, '12': {'item': 'Deep-Fried Filet Mignon', 'cost': 20, 'quantity': 1000}, '13': {'item': 'Fries', 'cost': 3, 'quantity': 1000}, '14': {'item': 'Tots', 'cost': 3, 'quantity': 1000}, '15': {'item': 'Cole Slaw', 'cost': 3, 'quantity': 1000}, '16': {'item': 'Cream Corn', 'cost': 3, 'quantity': 1000}, '17': {'item': 'Collard Greens', 'cost': 5, 'quantity': 1000}, '18': {'item': 'Corn Bread', 'cost': 4, 'quantity': 1000}, '19': {'item': 'Buttered Beans', 'cost': 6, 'quantity': 1000}, '20': {'item': 'Ice Cream', 'cost': 5, 'quantity': 1000}, '21': {'item': 'Cake', 'cost': 6, 'quantity': 1000}, '22': {'item': 'Pie', 'cost': 6, 'quantity': 1000}, '23': {'item': 'Salmon Cookie', 'cost': 4, 'quantity': 1000}, '24': {'item': 'Coffee', 'cost': 3, 'quantity': 1000}, '25': {'item': 'Tea', 'cost': 3, 'quantity': 1000}, '26': {'item': 'Blood of the Innocent', 'cost': 4, 'quantity': 1000}, '27': {'item': 'Beer', 'cost': 4, 'quantity': 1000}, '28': {'item': 'Irish Coffee', 'cost': 5, 'quantity': 1000}, '29': {'item': 'Purple Drank', 'cost': 3, 'quantity': 1000}}
