from textwrap import dedent
import sys
import uuid

#Simple data structure to add more items/prices
MENU = [
  {'Appetizers': [{'Wings':7},{'Cookies':3},{'Spring Rolls':5}]},
  {'Entrees': [{'Salmon':15},{'Steak':18},{'Meat Tornado':12},{'A Literal Garden':10}]},
  {'Sides': [{'Fries':3},{'Tots':3},{'Cole Slaw':3},{'Cream Corn':3}]},
  {'Desserts': [{'Ice Cream':5},{'Cake':6},{'Pie':6}]},
  {'Drinks': [{'Coffee':3},{'Tea':3},{'Blood of the Innocent':4}]},
]

#Formatted menu where each item is displayed along with a number
MENU_FORMATTED = []
counter = 1
for item in MENU:
  current_category = {}
  for key,value in item.items():
    current_category[key]={}
    for i in value:
      current_category[key][str(counter)] = i
      counter += 1
  MENU_FORMATTED.append(current_category)

CATEGORIES = set()
for i in MENU:
  for key,value in i.items():
    CATEGORIES.add(key.lower())

#Two dictionaries that list all available items
#AVAILABLE_ITEMS is in the format: {'1':'Wings', ...}
#BACKWARDS_MAP is in the format: {'Wings':'1', ...}
AVAILABLE_ITEMS = {}
BACKWARDS_MAP = {}
for category in MENU_FORMATTED:
    for key,value in category.items():
      for key2,value2 in value.items():
        for food,price in value2.items():
          AVAILABLE_ITEMS[key2]={'item':food,'cost':price}
          BACKWARDS_MAP[food.lower()]=key2

#Initializing ORDER, which will keep track of items and quantities
ORDER = {}

#Unique identifier for order
ORDER_NUMBER = uuid.uuid4()

#Function that prints menu in nice format. This will be called in the greeting() function below
def print_menu(menu,width):
  output='\n'
  for category in menu:
    for key,value in category.items():
      output += key + '\n'
      output += f'''{'-' * len(key)}\n'''
      for key2,value2 in value.items():
          for food, price in value2.items():
            output += key2 + '. ' + food + ('.'*(width-len(str(key2))-2-len(food)-len('${:,.2f}'.format(price)))) + '${:,.2f}'.format(price) + '\n'
    output += '\n'
  return output

def print_category(menu,selected_category,width):
  output='\n'
  for category in menu:
    for key,value in category.items():
      if key.lower()==selected_category:
        output += key + '\n'
        output += f'''{'-' * len(key)}\n'''
        for key2,value2 in value.items():
          for food, price in value2.items():
            output += key2 + '. ' + food + ('.'*(width-len(str(key2))-2-len(food)-len('${:,.2f}'.format(price)))) + '${:,.2f}'.format(price) + '\n'
      output += '\n'
  return output

#Welcomes the user, displays menu, and gives basic instructions
def greeting():
  """Function which will greet user when the application executes for the first time.
  """
  ln_one = 'Welcome to the Snakes Cafe! '
  ln_two = 'Please see our menu below.'
  ln_three = '**'
  ln_four = 'To quit at any time, type "quit"'
  ln_four_2 = 'To see your full order, type "order"'
  ln_five = 'What would you like to order? '
  ln_six = '(Please enter item name, or number next to item)'

  width = max(len(ln_one),len(ln_two),len(ln_three),len(ln_four),len(ln_four_2),len(ln_five),len(ln_six)) + 8

  print(dedent(f'''\n
    \r{'*' * width}
    \r{'**' + (' ' * ((width - 4 - len(ln_one)) // 2)) + ln_one + (' ' * ((width - 4 - len(ln_one)) // 2)) + '**'}
    \r{'**' + (' ' * ((width - 4 - len(ln_two)) // 2)) + ln_two + (' ' * ((width - 4 - len(ln_two)) // 2)) + '**'}
    \r{'**' + (' ' * ((width - 4 - len(ln_three)) // 2)) + ln_three + (' ' * ((width - 4 - len(ln_three)) // 2)) + '**'}
    \r{'**' + (' ' * ((width - 4 - len(ln_four)) // 2)) + ln_four + (' ' * ((width - 4 - len(ln_four)) // 2)) + '**'}
    \r{'**' + (' ' * ((width - 4 - len(ln_four_2)) // 2)) + ln_four_2 + (' ' * ((width - 4 - len(ln_four_2)) // 2)) + '**'}
    \r{'*' * width}
    \n
    {print_menu(MENU_FORMATTED,width)}
    \r{'*' * width}
    \r{'**' + (' ' * ((width - 4 - len(ln_five)) // 2)) + ln_five + (' ' * ((width - 4 - len(ln_five)) // 2)) + '**'}
    \r{'**' + (' ' * ((width - 4 - len(ln_six)) // 2)) + ln_six + (' ' * ((width - 4 - len(ln_six)) // 2)) + '**'}
    \r{'*' * width}
  '''))

#This function handles user input. Options are quit, order, remove <item>, or simply an item number or name (which adds that item to the order object above)
def check_input(user_in):
  if user_in.lower() == 'quit':
    exit()
    return
  
  if user_in.lower() == 'order':
    return 'order'

  if user_in.lower() == 'menu':
    return 'menu'

  if user_in.lower() in CATEGORIES:
    return 'category ' + user_in.lower()

  elif user_in.split(' ')[0].lower() == 'remove' and user_in.split(' ')[1].lower() in (BACKWARDS_MAP or AVAILABLE_ITEMS):
    item = user_in.split(' ')[1].lower()
    if item.isnumeric():
      if ORDER[item] != 0:
        ORDER[item] -= 1
        item_cost = AVAILABLE_ITEMS[item]['cost']*-1
        update_total_cost(item_cost)
        return f'''removed {item}'''
    elif item in BACKWARDS_MAP:
      string_item = BACKWARDS_MAP[item].lower()
      if ORDER[string_item] != 0:
        ORDER[string_item] -= 1
        item_cost = AVAILABLE_ITEMS[string_item]['cost']*-1
        update_total_cost(item_cost)
        return f'''removed {item}'''
    else:
      print('That item is not in your order!')

  elif(user_in.lower() in AVAILABLE_ITEMS or user_in.lower() in BACKWARDS_MAP):
    if user_in.lower() in BACKWARDS_MAP:
      user_in = BACKWARDS_MAP[user_in.lower()]
    if user_in in ORDER:
      ORDER[user_in] += 1
    else:
      ORDER[user_in] = 1
    # print(AVAILABLE_ITEMS[user_in])
    item_cost = AVAILABLE_ITEMS[user_in]['cost']
    update_total_cost(item_cost)
    return user_in

  else:
    return 'N/A'

#Function that calculates total cost. This is called in the feedback() function below
TOTAL_COST = 0
def update_total_cost(item_cost):
  global TOTAL_COST
  TOTAL_COST += item_cost
  return TOTAL_COST

#Function that provides user feedback based on their input and subsequent processing
def feedback(status):
  if status=='' or status=='N/A':
    print(dedent('''
      Sorry, I didn't understand. :(
    '''))

  elif status=='order':
    if not ORDER:
      print(dedent('You haven\'t added any items to your order yet.'))
    else:
      print(dedent('Here\'s your current order:'+ '\n'))
      print(format_order())
  
  elif status=='menu':
    print(print_menu(MENU_FORMATTED,54))
  
  elif status.split(' ')[0]=='category':
    print(print_category(MENU_FORMATTED,status.split(' ')[1],54))

  elif status.split(' ')[0]=='removed':
    print(f'''1 order of {status.split(' ')[1]} removed from your meal.''')

  elif status!='N/A':
    if ORDER[status]>1:
      print(dedent(f'''
        ** {ORDER[status]} orders of {AVAILABLE_ITEMS[status]['item']} are now in your meal. The total cost of your order is ${round(TOTAL_COST,2)} (before tax) **'''))
    else:
      print(dedent(f'''
        ** {ORDER[status]} order of {AVAILABLE_ITEMS[status]['item']} has been added to your meal. The total cost of your order is ${round(TOTAL_COST,2)} (before tax) **'''))

  print(dedent(f'''\nWould you like to add anything to your order? If so, enter the item number.\n(To remove an item, type 'remove' followed by the item number or name.)\n(To see your complete order, type 'order'.)\n'''))
        
  user_input = input('< ')
  status = check_input(user_input)
  feedback(status)

#Function that formats the order nicely when the command 'order' is typed.
def format_order():
  ln_one='\rThe Snakes Cafe'
  ln_two='\r\"Eatability Counts\"'
  ln_three=f'''\rOrder #{ORDER_NUMBER}'''

  order='\n'
  for key,value in ORDER.items():
    current_item = AVAILABLE_ITEMS[key]['item']
    current_quantity = value
    item_total = current_quantity * AVAILABLE_ITEMS[key]['cost']
    if current_quantity>0:
      order += f'''{current_item} x{current_quantity} {' '*(len(ln_three)-len(current_item)-len(str(current_quantity))-len(str(item_total))-8)} {'${:,.2f}'.format(item_total)}\n'''

  output = dedent(f'''
            \r{'*' * len(ln_three)}
            {ln_one}
            {ln_two}
            {''}
            {ln_three}
            \r{'=' * len(ln_three)}
            {order}
            \r{'-' * len(ln_three)}
            \r{'Subtotal'+ (' ' * (len(ln_three)-len('Subtotal')-len('${:,.2f}'.format(TOTAL_COST)))) + '${:,.2f}'.format(TOTAL_COST)}
            \r{'Sales Tax' + (' ' * (len(ln_three)-len('Sales Tax')-len('${:,.2f}'.format(TOTAL_COST*.101)))) + '${:,.2f}'.format((TOTAL_COST*.101))}
            \r{'-'*len('Sales Tax')}
            \r{'Total Due' + (' ' * (len(ln_three)-len('Total Due')-len('${:,.2f}'.format(TOTAL_COST*1.101)))) + '${:,.2f}'.format((TOTAL_COST*1.101))}
            \r{'*' * len(ln_three)}
        ''')

  return output

#Function that escapes from the program  
def exit():
  print(dedent('''
    Thanks for coming in!
  '''))
  sys.exit()

#Function that initializes the script
def run():
    greeting()
    user_input = input('< ')
    status = check_input(user_input)
    feedback(status)
      
if __name__=='__main__':
  run()