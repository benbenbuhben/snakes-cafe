import snakes_cafe
import pytest
import io
import sys
from contextlib import contextmanager


@pytest.fixture
def menu():
    return [{'Appetizers': [{'Wings': 7}, {'Cookies': 3}, {'Spring Rolls': 5}, {'Rocky Mtn Oysters': 8}, {'Awesome Blossom Possom': 10}]}, {'Entrees': [{'Salmon': 15}, {'Steak': 18}, {'Meat Tornado': 12}, {'A Literal Garden': 10}, {'Vegan Mush': 11}, {'Chicken': 11}, {'Deep-Fried Filet Mignon': 20}]}, {'Sides': [{'Fries': 3}, {'Tots': 3}, {'Cole Slaw': 3}, {'Cream Corn': 3}, {'Collard Greens': 5}, {'Corn Bread': 4}, {'Buttered Beans': 6}]}, {'Desserts': [{'Ice Cream': 5}, {'Cake': 6}, {'Pie': 6}, {'Salmon Cookie': 4}]}, {'Drinks': [{'Coffee': 3}, {'Tea': 3}, {'Blood of the Innocent': 4}, {'Beer': 4}, {'Irish Coffee': 5}, {'Purple Drank': 3}]}]


@pytest.fixture
def more_arguments():
    return [{'sides', 'entrees', 'desserts', 'drinks', 'appetizers'}, {'1': {'item': 'Wings', 'cost': 7, 'quantity': 997}, '2': {'item': 'Cookies', 'cost': 3, 'quantity': 998}, '3': {'item': 'Spring Rolls', 'cost': 5, 'quantity': 998}, '4': {'item': 'Rocky Mtn Oysters', 'cost': 8, 'quantity': 1000}, '5': {'item': 'Awesome Blossom Possom', 'cost': 10, 'quantity': 1000}, '6': {'item': 'Salmon', 'cost': 15, 'quantity': 1000}, '7': {'item': 'Steak', 'cost': 18, 'quantity': 1000}, '8': {'item': 'Meat Tornado', 'cost': 12, 'quantity': 1000}, '9': {'item': 'A Literal Garden', 'cost': 10, 'quantity': 1000}, '10': {'item': 'Vegan Mush', 'cost': 11, 'quantity': 1000}, '11': {'item': 'Chicken', 'cost': 11, 'quantity': 1000}, '12': {'item': 'Deep-Fried Filet Mignon', 'cost': 20, 'quantity': 1000}, '13': {'item': 'Fries', 'cost': 3, 'quantity': 1000}, '14': {'item': 'Tots', 'cost': 3, 'quantity': 1000}, '15': {'item': 'Cole Slaw', 'cost': 3, 'quantity': 1000}, '16': {'item': 'Cream Corn', 'cost': 3, 'quantity': 1000}, '17': {'item': 'Collard Greens', 'cost': 5, 'quantity': 1000}, '18': {'item': 'Corn Bread', 'cost': 4, 'quantity': 1000}, '19': {'item': 'Buttered Beans', 'cost': 6, 'quantity': 1000}, '20': {'item': 'Ice Cream', 'cost': 5, 'quantity': 1000}, '21': {'item': 'Cake', 'cost': 6, 'quantity': 1000}, '22': {'item': 'Pie', 'cost': 6, 'quantity': 1000}, '23': {'item': 'Salmon Cookie', 'cost': 4, 'quantity': 1000}, '24': {'item': 'Coffee', 'cost': 3, 'quantity': 1000}, '25': {'item': 'Tea', 'cost': 3, 'quantity': 1000}, '26': {'item': 'Blood of the Innocent', 'cost': 4, 'quantity': 1000}, '27': {'item': 'Beer', 'cost': 4, 'quantity': 1000}, '28': {'item': 'Irish Coffee', 'cost': 5, 'quantity': 1000}, '29': {'item': 'Purple Drank', 'cost': 3, 'quantity': 1000}}, {'wings': '1', 'cookies': '2', 'spring rolls': '3', 'rocky mtn oysters': '4', 'awesome blossom possom': '5', 'salmon': '6', 'steak': '7', 'meat tornado': '8', 'a literal garden': '9', 'vegan mush': '10', 'chicken': '11', 'deep-fried filet mignon': '12', 'fries': '13', 'tots': '14', 'cole slaw': '15', 'cream corn': '16', 'collard greens': '17', 'corn bread': '18', 'buttered beans': '19', 'ice cream': '20', 'cake': '21', 'pie': '22', 'salmon cookie': '23', 'coffee': '24', 'tea': '25', 'blood of the innocent': '26', 'beer': '27', 'irish coffee': '28', 'purple drank': '29'}]


def test_this_file_works():
    pass


@contextmanager
def captured_output():
    '''Helper function for testing stdout'''
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def test_format_menu_fcn_exists():
    return snakes_cafe.format_menu


def test_format_menu_formats_menu(menu):
    """This function tests that the format menu function adds a numeric index to each menu item
    """
    actual = snakes_cafe.format_menu(menu)
    expected = [{'Appetizers': {'1': {'Wings': 7}, '2': {'Cookies': 3}, '3': {'Spring Rolls': 5}, '4': {'Rocky Mtn Oysters': 8}, '5': {'Awesome Blossom Possom': 10}}}, {'Entrees': {'6': {'Salmon': 15}, '7': {'Steak': 18}, '8': {'Meat Tornado': 12}, '9': {'A Literal Garden': 10}, '10': {'Vegan Mush': 11}, '11': {'Chicken': 11}, '12': {'Deep-Fried Filet Mignon': 20}}}, {'Sides': {'13': {'Fries': 3}, '14': {'Tots': 3}, '15': {'Cole Slaw': 3}, '16': {'Cream Corn': 3}, '17': {'Collard Greens': 5}, '18': {'Corn Bread': 4}, '19': {'Buttered Beans': 6}}}, {'Desserts': {'20': {'Ice Cream': 5}, '21': {'Cake': 6}, '22': {'Pie': 6}, '23': {'Salmon Cookie': 4}}}, {'Drinks': {'24': {'Coffee': 3}, '25': {'Tea': 3}, '26': {'Blood of the Innocent': 4}, '27': {'Beer': 4}, '28': {'Irish Coffee': 5}, '29': {'Purple Drank': 3}}}]
    assert actual == expected


def test_load_categories_creates_unique_set_of_categories(menu):
    print('hellooooo')
    actual = snakes_cafe.load_categories(menu)
    expected = {'sides', 'entrees', 'drinks', 'appetizers', 'desserts'}
    assert actual == expected


def test_create_lookup_returns_array_of_2_lookup_tables(menu):
    fcn_input = snakes_cafe.format_menu(menu)
    actual = snakes_cafe.create_lookup(fcn_input)
    expected1 = {'1': {'item': 'Wings', 'cost': 7, 'quantity': 1000}, '2': {'item': 'Cookies', 'cost': 3, 'quantity': 1000}, '3': {'item': 'Spring Rolls', 'cost': 5, 'quantity': 1000}, '4': {'item': 'Rocky Mtn Oysters', 'cost': 8, 'quantity': 1000}, '5': {'item': 'Awesome Blossom Possom', 'cost': 10, 'quantity': 1000}, '6': {'item': 'Salmon', 'cost': 15, 'quantity': 1000}, '7': {'item': 'Steak', 'cost': 18, 'quantity': 1000}, '8': {'item': 'Meat Tornado', 'cost': 12, 'quantity': 1000}, '9': {'item': 'A Literal Garden', 'cost': 10, 'quantity': 1000}, '10': {'item': 'Vegan Mush', 'cost': 11, 'quantity': 1000}, '11': {'item': 'Chicken', 'cost': 11, 'quantity': 1000}, '12': {'item': 'Deep-Fried Filet Mignon', 'cost': 20, 'quantity': 1000}, '13': {'item': 'Fries', 'cost': 3, 'quantity': 1000}, '14': {'item': 'Tots', 'cost': 3, 'quantity': 1000}, '15': {'item': 'Cole Slaw', 'cost': 3, 'quantity': 1000}, '16': {'item': 'Cream Corn', 'cost': 3, 'quantity': 1000}, '17': {'item': 'Collard Greens', 'cost': 5, 'quantity': 1000}, '18': {'item': 'Corn Bread', 'cost': 4, 'quantity': 1000}, '19': {'item': 'Buttered Beans', 'cost': 6, 'quantity': 1000}, '20': {'item': 'Ice Cream', 'cost': 5, 'quantity': 1000}, '21': {'item': 'Cake', 'cost': 6, 'quantity': 1000}, '22': {'item': 'Pie', 'cost': 6, 'quantity': 1000}, '23': {'item': 'Salmon Cookie', 'cost': 4, 'quantity': 1000}, '24': {'item': 'Coffee', 'cost': 3, 'quantity': 1000}, '25': {'item': 'Tea', 'cost': 3, 'quantity': 1000}, '26': {'item': 'Blood of the Innocent', 'cost': 4, 'quantity': 1000}, '27': {'item': 'Beer', 'cost': 4, 'quantity': 1000}, '28': {'item': 'Irish Coffee', 'cost': 5, 'quantity': 1000}, '29': {'item': 'Purple Drank', 'cost': 3, 'quantity': 1000}}
    expected2 = {'wings': '1', 'cookies': '2', 'spring rolls': '3', 'rocky mtn oysters': '4', 'awesome blossom possom': '5', 'salmon': '6', 'steak': '7', 'meat tornado': '8', 'a literal garden': '9', 'vegan mush': '10', 'chicken': '11', 'deep-fried filet mignon': '12', 'fries': '13', 'tots': '14', 'cole slaw': '15', 'cream corn': '16', 'collard greens': '17', 'corn bread': '18', 'buttered beans': '19', 'ice cream': '20', 'cake': '21', 'pie': '22', 'salmon cookie': '23', 'coffee': '24', 'tea': '25', 'blood of the innocent': '26', 'beer': '27', 'irish coffee': '28', 'purple drank': '29'}
    assert actual[0] == expected1
    assert actual[1] == expected2


def test_menu_from_csv_converts_csv_file_to_menu_format():
    fcn_input = '''name,category,price,quantity
Chicken Fingers,Appetizers,5,13
Loaded Potato,Appetizers,5,15
Mozz Sticks,Appetizers,5,26
Fish & Chips,Entrees,14,34
A Big Fucking Steak,Entrees,11,24
Turducken,Entrees,12,16
Unicorn Meat,Entrees,13,9
Yellow Cake,Desserts,3,33
Freedom Pie,Desserts,4,21
I Scream,Desserts,5,22'''
    actual = snakes_cafe.menu_from_csv(fcn_input)
    expected = [{'Appetizers': [{'Chicken Fingers': 5}, {'Loaded Potato': 5}, {'Mozz Sticks': 5}]}, {'Entrees': [{'Fish & Chips': 14}, {'A Big Fucking Steak': 11}, {'Turducken': 12}, {'Unicorn Meat': 13}]}, {'Desserts': [{'Yellow Cake': 3}, {'Freedom Pie': 4}]}]
    assert actual == expected


def test_print_menu_formats_menu_for_printing(menu):
    fcn_input = snakes_cafe.format_menu(menu)
    sample_width = 56
    actual = snakes_cafe.print_menu(fcn_input, sample_width)
    expected = '\nAppetizers\n----------\n1. Wings...........................................$7.00\n2. Cookies.........................................$3.00\n3. Spring Rolls....................................$5.00\n4. Rocky Mtn Oysters...............................$8.00\n5. Awesome Blossom Possom.........................$10.00\n\nEntrees\n-------\n6. Salmon.........................................$15.00\n7. Steak..........................................$18.00\n8. Meat Tornado...................................$12.00\n9. A Literal Garden...............................$10.00\n10. Vegan Mush....................................$11.00\n11. Chicken.......................................$11.00\n12. Deep-Fried Filet Mignon.......................$20.00\n\nSides\n-----\n13. Fries..........................................$3.00\n14. Tots...........................................$3.00\n15. Cole Slaw......................................$3.00\n16. Cream Corn.....................................$3.00\n17. Collard Greens.................................$5.00\n18. Corn Bread.....................................$4.00\n19. Buttered Beans.................................$6.00\n\nDesserts\n--------\n20. Ice Cream......................................$5.00\n21. Cake...........................................$6.00\n22. Pie............................................$6.00\n23. Salmon Cookie..................................$4.00\n\nDrinks\n------\n24. Coffee.........................................$3.00\n25. Tea............................................$3.00\n26. Blood of the Innocent..........................$4.00\n27. Beer...........................................$4.00\n28. Irish Coffee...................................$5.00\n29. Purple Drank...................................$3.00\n\n'
    assert actual == expected


def test_print_category_formats_for_printing(menu):
    fcn_input = snakes_cafe.format_menu(menu)
    sample_width = 54
    sample_category = 'desserts'
    actual = snakes_cafe.print_category(fcn_input, sample_category, sample_width)
    expected = '\nDesserts\n--------\n20. Ice Cream....................................$5.00\n21. Cake.........................................$6.00\n22. Pie..........................................$6.00\n23. Salmon Cookie................................$4.00\n\n'
    assert actual == expected


def test_greeting_prints_properly_to_std_out(menu):
    fcn_input = snakes_cafe.format_menu(menu)
    with captured_output() as (out, err):
        snakes_cafe.greeting(fcn_input)
    output = out.getvalue()
    print(output.encode('utf-8'))
    expected = '''\n\n        \r********************************************************\n        \r**            Welcome to the Snakes Cafe!             **\n        \r**             Please see our menu below.             **\n        \r**                         **                         **\n        \r**          To quit at any time, type "quit"          **\n        \r**        To see your full order, type "order"        **\n        \r********************************************************\n\n\n\nAppetizers\n----------\n1. Wings...........................................$7.00\n2. Cookies.........................................$3.00\n3. Spring Rolls....................................$5.00\n4. Rocky Mtn Oysters...............................$8.00\n5. Awesome Blossom Possom.........................$10.00\n\nEntrees\n-------\n6. Salmon.........................................$15.00\n7. Steak..........................................$18.00\n8. Meat Tornado...................................$12.00\n9. A Literal Garden...............................$10.00\n10. Vegan Mush....................................$11.00\n11. Chicken.......................................$11.00\n12. Deep-Fried Filet Mignon.......................$20.00\n\nSides\n-----\n13. Fries..........................................$3.00\n14. Tots...........................................$3.00\n15. Cole Slaw......................................$3.00\n16. Cream Corn.....................................$3.00\n17. Collard Greens.................................$5.00\n18. Corn Bread.....................................$4.00\n19. Buttered Beans.................................$6.00\n\nDesserts\n--------\n20. Ice Cream......................................$5.00\n21. Cake...........................................$6.00\n22. Pie............................................$6.00\n23. Salmon Cookie..................................$4.00\n\nDrinks\n------\n24. Coffee.........................................$3.00\n25. Tea............................................$3.00\n26. Blood of the Innocent..........................$4.00\n27. Beer...........................................$4.00\n28. Irish Coffee...................................$5.00\n29. Purple Drank...................................$3.00\n\n\n        \r********************************************************\n        \r**           What would you like to order?            **\n        \r**  (Please enter item name, or number next to item)  **\n        \r********************************************************\n\n'''
    assert output == expected


def test_check_input_returns_valid_single_word_commands(more_arguments):

    actual1 = snakes_cafe.check_input('order', more_arguments)
    actual2 = snakes_cafe.check_input('menu', more_arguments)
    actual3 = snakes_cafe.check_input('print', more_arguments)
    assert actual1 == 'order'
    assert actual2 == 'menu'
    assert actual3 == 'print'


def test_check_input_handles_remove_command(more_arguments):
    """I could use some help on this one. The check input function is dependent on the globally defined variable ORDER. I haven't been able to easily figure out how to make this variable available to the function during testing, without modifying the function.
    """
    # global ORDER
    # ORDER = snakes_cafe.Order(more_arguments[1])
    # actual = snakes_cafe.check_input('remove spring rolls', more_arguments)
    # expected = 'removed Spring Rolls'
    # assert actual == expected
    pass


def test_check_input_handles_invalid_input(more_arguments):
    actual = snakes_cafe.check_input('ljawhbfjahdsbv', more_arguments)
    expected = 'N/A'
    assert actual == expected


def test_feedback_gives_reponse_for_invalid_input(menu, more_arguments):
    """Also need some help here. My feedback function prompts for input, which is causing an error in the pytest module:
    OSError: reading from stdin while output is captured
    """
    # menu_formatted = snakes_cafe.format_menu(menu)
    # with captured_output() as (out, err):
    #     snakes_cafe.feedback('N/A', menu_formatted, more_arguments)
    # output = out.getvalue()
    # print(output.encode('utf-8'))
    pass

