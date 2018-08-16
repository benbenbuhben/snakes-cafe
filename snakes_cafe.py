from textwrap import dedent
import sys
from uuid import uuid4

#TESTS
#For each function... valid case, invalid case, edge case

def determine_menu(menu_type):
  if menu_type == 'default':
    MENU = [
      {'Appetizers': [{'Wings':7},{'Cookies':3},{'Spring Rolls':5},{'Rocky Mtn Oysters':8},{'Awesome Blossom Possom':10}]},
      {'Entrees': [{'Salmon':15},{'Steak':18},{'Meat Tornado':12},{'A Literal Garden':10},{'Vegan Mush':11},{'Chicken':11},{'Deep-Fried Filet Mignon':20}]},
      {'Sides': [{'Fries':3},{'Tots':3},{'Cole Slaw':3},{'Cream Corn':3},{'Collard Greens':5},{'Corn Bread':4},{'Buttered Beans':6}]},
      {'Desserts': [{'Ice Cream':5},{'Cake':6},{'Pie':6},{'Salmon Cookie':4}]},
      {'Drinks': [{'Coffee':3},{'Tea':3},{'Blood of the Innocent':4},{'Beer':4},{'Irish Coffee':5},{'Purple Drank':3}]},
    ]
  else:
    MENU = menu_type
  return MENU

def format_menu(menu):
  """Formatted menu where each item is displayed along with a number"""
  MENU_FORMATTED = []
  counter = 1
  for item in menu:
    current_category = {}
    for key,value in item.items():
      current_category[key]={}
      for i in value:
        current_category[key][str(counter)] = i
        counter += 1
    MENU_FORMATTED.append(current_category)
  return MENU_FORMATTED

def load_categories(menu):
  """Unique set to hold each category for print_category() function below"""
  CATEGORIES = set()
  for i in menu:
    for key,value in i.items():
      CATEGORIES.add(key.lower())
  return CATEGORIES

QUANTITIES = [] 
def create_lookup(menu_formatted):
  """Two dictionaries that list all available items for ease of access.
  AVAILABLE_ITEMS is in the format: {'1':'Wings', ...}
  BACKWARDS_MAP is in the format: {'Wings':'1', ...}"""
  AVAILABLE_ITEMS = {}
  BACKWARDS_MAP = {}
  for category in menu_formatted:
    for key,value in category.items():
      for key2,value2 in value.items():
        for food,price in value2.items():
          if len(QUANTITIES)>0:
            AVAILABLE_ITEMS[key2]={'item':food,'cost':price,'quantity':int(QUANTITIES[int(key2)-1])}
          else:
            AVAILABLE_ITEMS[key2]={'item':food,'cost':price,'quantity':1000}
          BACKWARDS_MAP[food.lower()]=key2
  return [AVAILABLE_ITEMS,BACKWARDS_MAP]

#Initializing ORDER, which will keep track of items and quantities
ORDER = {}

#Unique identifier for order
ORDER_NUMBER = uuid4()

def menu_from_csv(custom_menu):
  arr = custom_menu.split('\n')[1:]
  newArr = []
  
  #Create 2-D array of rows/columns
  for i in arr:
    row = i.split(',')
    newArr.append(row)

  finalObj = {}
  #Iterate through each row and create object of unique categories
  newArr = newArr[:len(newArr)-1]
  for i in newArr:
    category = i[1]
    if category not in finalObj:
      finalObj[category] = []

  #Iterate again and append each item to its corresponding category
  for i in newArr:
    item = {i[0]:int(i[2])}
    QUANTITIES.append(i[3])
    finalObj[i[1]].append(item)

  #Convert the object to an array in the appropriate format
  finalArr = []
  for key,value in finalObj.items():
    current_item = {key:value}
    finalArr.append(current_item)

  return finalArr

def print_menu(menu,width):
  """Function that prints menu in nice format. This will be called in the greeting() function below"""
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

def greeting(menu_formatted):
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
    {print_menu(menu_formatted,width)}
    \r{'*' * width}
    \r{'**' + (' ' * ((width - 4 - len(ln_five)) // 2)) + ln_five + (' ' * ((width - 4 - len(ln_five)) // 2)) + '**'}
    \r{'**' + (' ' * ((width - 4 - len(ln_six)) // 2)) + ln_six + (' ' * ((width - 4 - len(ln_six)) // 2)) + '**'}
    \r{'*' * width}
  '''))

def check_input(user_in,more_arguments):
  """This function handles user input. Options are quit, order, remove <item>, or simply an item number or name (which adds that item to the order object above)"""
  CATEGORIES = more_arguments[0]
  AVAILABLE_ITEMS = more_arguments[1]
  BACKWARDS_MAP = more_arguments[2]
  input1 = user_in.split(' ')[0].lower()
  increment = 1
  if(len(user_in.split(' '))>1):
    input2 = user_in.split(' ')[1].lower()
    if not input2.isnumeric() or (input2.isnumeric() and int(input2)<1):
      print('Invalid quantity!')
      return 'N/A'
    else:
      increment = int(input2)
  if user_in.lower() == 'quit':
    exit()
    return
  
  elif user_in.lower() == 'order':
    return 'order'

  elif user_in.lower() == 'menu':
    return 'menu'

  elif user_in.lower() in CATEGORIES:
    return 'category ' + user_in.lower()

  elif input1 == 'remove' and input2 in (BACKWARDS_MAP or AVAILABLE_ITEMS):
    item = input2
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

  elif(input1 in AVAILABLE_ITEMS or input1 in BACKWARDS_MAP):
    if input1 in BACKWARDS_MAP:
      input1 = BACKWARDS_MAP[input1]
    if (AVAILABLE_ITEMS[input1]['quantity']-increment)<=0:
      print(dedent(f'''Sorry, we only have {AVAILABLE_ITEMS[input1]['quantity']} {AVAILABLE_ITEMS[input1]['item']} left.'''))
      return 'N/A'
    else:
      if input1 in ORDER:
        ORDER[input1] += increment
        AVAILABLE_ITEMS[input1]['quantity'] -= increment
      else:
        ORDER[input1] = increment
        AVAILABLE_ITEMS[input1]['quantity'] -= increment
      item_cost = AVAILABLE_ITEMS[input1]['cost']
      update_total_cost(item_cost)
      return input1

  else:
    return 'N/A'


TOTAL_COST = 0
def update_total_cost(item_cost):
  """Function that calculates total cost. This is called in the feedback() function below"""
  global TOTAL_COST
  TOTAL_COST += item_cost
  return TOTAL_COST

def feedback(status,menu_formatted,more_arguments):
  """Function that provides user feedback based on their input and subsequent processing"""
  AVAILABLE_ITEMS = more_arguments[1]

  if status=='' or status=='N/A':
    print(dedent('''
      Sorry, I didn't understand. :(
    '''))

  elif status=='order':
    if not ORDER:
      print(dedent('You haven\'t added any items to your order yet.'))
    else:
      print(dedent('Here\'s your current order:'+ '\n'))
      print(format_order(AVAILABLE_ITEMS))
  
  elif status=='menu':
    print(print_menu(menu_formatted,54))
  
  elif status.split(' ')[0]=='category':
    print(print_category(menu_formatted,status.split(' ')[1],54))

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
  status = check_input(user_input,more_arguments)
  feedback(status,menu_formatted,more_arguments)

def format_order(available_items):
  """Function that formats the order nicely when the command 'order' is typed."""
  ln_one='\rThe Snakes Cafe'
  ln_two='\r\"Eatability Counts\"'
  ln_three=f'''\rOrder #{ORDER_NUMBER}'''

  order='\n'
  for key,value in ORDER.items():
    current_item = available_items[key]['item']
    current_quantity = value
    item_total = current_quantity * available_items[key]['cost']
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
 
def exit():
  """Function that escapes from the program """
  print(dedent('''
    Thanks for coming in!
  '''))
  sys.exit()

def load_menu():
  print('Please type the filepath to your menu (e.g., ./assets/custom_menu.csv)')
  menu_path = input('< ')
  file_structure = menu_path.split('/')
  file = file_structure[len(file_structure)-1].split('.')
  extension = file[len(file)-1]
  if extension != 'csv':
    print('THAT WASN\'T A CSV FILE!!!!!11!!1!')
    return load_menu()

  else:
    try:
      with open(menu_path) as file:
        custom_menu = file.read()
        menu = menu_from_csv(custom_menu)
        return menu
    except FileNotFoundError:
      print('BAD FILE PATH!!!!!11!!1!')
      return load_menu()
    

def run():
  """Function that initializes the script"""
  print(dedent(f'''
  {'Welcome to the Snake Cafe Menu Loader Thingie!'}
  {'Would you like to use our default menu, or load a custom menu (in .csv format)?'}
  {'1: Default'}
  {'2: Custom'}'''))
  initial_input = input('< ')
  if initial_input == '2':
    custom_menu = load_menu()
    MENU = determine_menu(custom_menu)
  else:
    MENU = determine_menu('default')

  MENU_FORMATTED = format_menu(MENU)
  CATEGORIES = load_categories(MENU)
  AVAILABLE_ITEMS = create_lookup(MENU_FORMATTED)[0]
  BACKWARDS_MAP = create_lookup(MENU_FORMATTED)[1]
  argument_package = [CATEGORIES,AVAILABLE_ITEMS,BACKWARDS_MAP]
  greeting(MENU_FORMATTED)
  user_input = input('< ')
  status = check_input(user_input,argument_package)
  feedback(status,MENU_FORMATTED,argument_package)
    
if __name__=='__main__':
  try:
    run()
  except(KeyboardInterrupt):
    exit()