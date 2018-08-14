from textwrap import dedent
import sys

WIDTH = 96
BANK = [
  {
    'question': 'How old do you think I am?\n',
    'answer': '34',
    'hint': 'Digits add to 7.',
    'status': False,
  },
  {
    'question': 'What state was I born in?\n',
    'answer': 'Louisiana',
    'hint': 'Pelicans',
    'status': False,
  },
]


def greeting():
  """Function which will greet user when the application executes for the first time.
  """
  ln_one = 'Welcome to my Guessing Game!'
  ln_two = 'Answer the following questions for me'
  ln_three = 'To quit at any time, type "quit"'

  print(dedent(f'''
    {'*' * WIDTH}
    {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
    {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}
    {(' ' * ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}
    {'*' * WIDTH}
  '''))

def ask_question(question):
  return input(question)

def check_input(user_in, item):
  if user_in.lower() == 'quit':
    exit()
    return
  
  if user_in.lower() == item['answer'].lower():
    item['status'] = True
    return True

  return False


def feedback(status):
  if status is True:
    print(dedent('''
      Congrats! That's correct!\n
    '''))
    return

  print(dedent('''
    Sorry, you got that one wrong.\n
  '''))

def exit():
  print(dedent('''
    Thanks for playing!
  '''))
  sys.exit()


def run():
    greeting()
    for item in BANK:
      user_input = ask_question(item['question'])
      status = check_input(user_input, item)
      feedback(status)

if __name__=='__main__':
  print('Hello World Two')
  run()