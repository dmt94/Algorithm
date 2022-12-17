# recursive function is one that calls itself
import random

def print_chars(word, i):
  if i == len(word):
    print(f"Function has been called {i} times!")
    return # base case, == in this case, once index is out of base, fn stops calling itself
    # stopping boint = "base case"
  print(word[i])
  print_chars(word, i + 1)

class Player:
  def __init__(self, name):
    self.name = name
    self.tokens = None
    self.prize = None
    self.gifts = [
      "Golden H+K Winter Globe, for good luck in love and career throughout 2023!",
      "3 day Vacation Package to The Ritz-Carlton Maui for 2",
      "Disneyland Theme Park Tickets for 7",
      "Fully Furnished 3 bd 5ba home worth $8 million in Beverly Hills",
      "Fully Furnished 4 bd 5ba home worth $8 million in San Mateo",
      "2022 Sonic Gray Pearl Honda Accord Touring worth $40k",
      "$5,000 William Sonoma Giftcard",
      "$1.3 million 3bd 3ba Condo in Los Angeles",
      "$1,000 Target Giftcard",
      "Cozy Winter-themed Pajamas and a Hot Cocoa Giftset",
      "2023 Black Model 3 Tesla worth $53k",
      100000,
      "$5,000 Apple Giftcard",
      "Space-Gray 16-inch MacBook Pro with 10-Core CPU, 32-Core GPU, and 32GB Unified Memory worth $3.5k"
      "$200 Amazon Gift Card",
      "A Christmas Song"
    ]

  def give_tokens(self):
    max_rand_token = 100000
    token = random.randint(1, max_rand_token)
    setattr(self, 'tokens', token)
    print(f"Congratulations! You received ${token}.00!\n")

  def give_gift(self):
    gift = random.choices(self.gifts)[0]
    setattr(self, 'prize', gift)
    if gift == 100000:
      print(f"Wow! You received an extra ${gift}.00!\n")
      setattr(self, 'tokens', gift)
    if gift == "A Christmas Song":
      print(f"Wow! You received A Christmas Song!\n")  
    else:
      print(f"As an extra special gift, you also receive: {gift}!!\n")

  def get_prize(self):
    return self.prize

def ask_name():
  name = input(f"What is your name?\n==> ")
  print(f"Welcome, {name}! Merry Winter!")
  return name

def greeting():
  print("WELCOME!")
  print("Because it's the holidays, you'll receive some cash prizes and other wholesome gifts for using this program :)")

def special_song(user):
  prize = user.get_prize()
  return prize == "A Christmas Song"

def play_song(user):
  print(f"\n{user.name}, this song is for you:\n")
  song_path = "christmas.txt"
  with open(song_path) as song:
    print(song.read())

def ask_number(user):
  number = input(f"Pick a positive integer to find its factorial, {user.name}:\n==> ")
  if number.isdigit():
    number = int(number)
    if number < 0:
      print("Please input positive number")
      return ask_number(user)
    return number
  else:
    print("Input a digit")
    return ask_number(user)

def recursive_factorial(num):
  if num == 1 or num == 0:
    return 1
  else:
    return num * recursive_factorial(num - 1)

def print_factorial(factorial):
  print(f"The factorial is ==> {factorial}")

def input_another(user):
  again = input(f"Do you want to find the factorial of another number, {user.name}? [y/n]\n==> ")
  if again == "y" or again == "yes":
    return True
  elif again == "n" or again == "no":
    print("Thank you for using my program and have a Merry Holiday :)")
    print("Enjoy your gifts!")
    return False
  else:
    print("Please type 'y' or 'n'")
    return input_another(user)

def recursive_program(user):
  print_factorial(recursive_factorial(ask_number(user)))
  if input_another(user):
    return recursive_program(user)
  else:
    print("Bye~")

def program():
  greeting()
  user_name = ask_name()
  player = Player(user_name)
  player.give_tokens()
  player.give_gift()
  if special_song(player):
    play_song(player)
  recursive_program(player)

program()
  

# counts down, with int == 1 being the "base case"
# the formula is (current_int) * fn(current_int - 1)
# ----> keep counting down, multiplying (product accumulates) until int == 1
