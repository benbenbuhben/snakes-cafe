from textwrap import dedent
import sys


MENU = [
  {'Appetizers': {'1': 'Wings','2': 'Cookies','3':'Spring Rolls'}},
  {'Entrees': {'4':'Salmon','5':'Steak','6':'Meat Tornado','7':'A Literal Garden'}},
  {'Desserts': {'8':'Ice Cream','9':'Cake','10':'Pie'}},
  {'Drinks': {'11':'Coffee','12':'Tea','13':'Blood of the Innocent'}},
]
AVAILABLE_ITEMS = {}

for category in MENU:
    for key,value in category.items():
      for key2,value2 in value.items():
        AVAILABLE_ITEMS[key2]=value2

ORDER = {}


def print_menu(menu):
  output='\n'
  for category in menu:
    for key,value in category.items():
      output += key + '\n'
      output += f'''{'-' * len(key)}\n'''
      for key2,value2 in value.items():
          output += key2 + '. ' + value2 + '\n'
    output += '\n'
  return output


def greeting():
  """Function which will greet user when the application executes for the first time.
  """
  ln_one = 'Welcome to the Snakes Cafe! '
  ln_two = 'Please see our menu below.'
  ln_three = '**'
  ln_four = 'To quit at any time, type "quit"'
  ln_four_2 = 'To see your full order, type "show"'
  ln_five = '**   What would you like to order?    **'
  ln_six = '** (Please enter number next to item) **'

  width = max(len(ln_one),len(ln_two),len(ln_three),len(ln_four),len(ln_four_2),len(ln_five)) + 8

  print(dedent(f'''\n
    {'*' * width}
    {'**' + (' ' * ((width - 4 - len(ln_one)) // 2)) + ln_one + (' ' * ((width - 4 - len(ln_one)) // 2)) + '**'}
    {'**' + (' ' * ((width - 4 - len(ln_two)) // 2)) + ln_two + (' ' * ((width - 4 - len(ln_two)) // 2)) + '**'}
    {'**' + (' ' * ((width - 4 - len(ln_three)) // 2)) + ln_three + (' ' * ((width - 4 - len(ln_three)) // 2)) + '**'}
    {'**' + (' ' * ((width - 4 - len(ln_four)) // 2)) + ln_four + (' ' * ((width - 4 - len(ln_four)) // 2)) + '**'}
    {'**' + (' ' * ((width - 4 - len(ln_four_2)) // 2)) + ln_four_2 + (' ' * ((width - 4 - len(ln_four_2)) // 2)) + '**'}
    {'*' * width}
    \n
    {print_menu(MENU)}
    {'*' * len(ln_six)}
    {ln_five}
    {ln_six}
    {'*' * len(ln_six)}
  '''))

def check_input(user_in):
  if user_in.lower() == 'quit':
    exit()
    return
  
  if user_in == 'show':
    return 'show'

  elif(user_in in AVAILABLE_ITEMS):
    if user_in in ORDER:
      ORDER[user_in] += 1
    else:
      ORDER[user_in] = 1
    return user_in

  else:
    return 'N/A'


def feedback(status):
  if status=='N/A':
    print(dedent('''
      Sorry, we don't have that item :(
    '''))

  if status=='show':
    if not ORDER:
      print(dedent('You haven\'t added any items to your order yet.'))
    else:
      print(dedent('Here\'s your current order:'+ '\n'))
      for item in ORDER:
        print(dedent(f'''ITEM: {AVAILABLE_ITEMS[item]}, QUANTITY: {ORDER[item]}      
          '''))
    print(dedent('Would you like to add anything to your order? (If so, enter the item number)'))

  else:
    if ORDER[status]>1:
      print(dedent(f'''
        ** {ORDER[status]} orders of {AVAILABLE_ITEMS[status]} are now in your meal. **

        Would you like anything else? (If so, enter the item number)       
        '''))
    else:
      print(dedent(f'''
        ** {ORDER[status]} order of {AVAILABLE_ITEMS[status]} has been added to your meal. **

        Would you like anything else? (If so, enter the item number)
        '''))
    
  user_input = input('< ')
  status = check_input(user_input)
  feedback(status)

def exit():
  print(dedent('''
    Thanks for coming in!
  '''))
  sys.exit()


def run():
    greeting()
    user_input = input('< ')
    status = check_input(user_input)
    feedback(status)
      

if __name__=='__main__':
  run()