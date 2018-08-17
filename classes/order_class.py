import uuid
from textwrap import dedent

class Order(object):

  def __init__(self,available_items):
    self.map = {}
    self.total = 0
    self.text = ''
    self.id = uuid.uuid4()
    self.available_items = available_items

  def add_item(self,item,quantity=1):
    if item not in self.map:
      self.map[item] = quantity
    else:
      self.map[item] += quantity

  def remove_item(self,item,item_cost):
    if item not in self.map:
      return False
    else:
      self.map[item] -= 1
      if self.map[item] == 0:
        del self.map[item]
      self.update_total(item_cost)
      return item

  def update_total(self,item_cost):
    self.total+=item_cost

  def display_order(self):
    ln_one='\rThe Snakes Cafe'
    ln_two='\r\"Eatability Counts\"'
    ln_three=f'''\rOrder #{self.id}'''
    ln_four='Type "print" to save your receipt as a .txt'

    order='\n'
    for key,value in self.map.items():
      current_item = self.available_items[key]['item']
      current_quantity = value
      item_total = current_quantity * self.available_items[key]['cost']
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
              \r{'Subtotal'+ (' ' * (len(ln_three)-len('Subtotal')-len('${:,.2f}'.format(self.total)))) + '${:,.2f}'.format(self.total)}
              \r{'Sales Tax' + (' ' * (len(ln_three)-len('Sales Tax')-len('${:,.2f}'.format(self.total*.101)))) + '${:,.2f}'.format((self.total*.101))}
              \r{'-'*len('Sales Tax')}
              \r{'Total Due' + (' ' * (len(ln_three)-len('Total Due')-len('${:,.2f}'.format(self.total*1.101)))) + '${:,.2f}'.format((self.total*1.101))}
              \r{'*' * len(ln_three)}
              \r{ln_four + (' ' * ( len(ln_three) - len(ln_four) ) )}
              \r{'*' * len(ln_three)}
          ''')
    self.text = output

    return output

  def clear_order(self):
    self.map = {}

  def print_receipt(self):
    filename = f'''order-{self.id}.txt'''
    text = self.display_order()
    with open(f'''./assets/receipts/{filename}''', "w") as f:
        f.write(text)

  def __repr__(self):
    num_items = 0
    for item,quantity in self.map.items():
      num_items += quantity
    return f'''<Order #{self.id} | Items: {num_items} | Total: {'${:,.2f}'.format(self.total*1.101)}>'''

  def __len__(self):
    num_items = 0
    for item,quantity in self.map.items():
      num_items += quantity
    return num_items

  def __str__(self):
    return self.display_order()
