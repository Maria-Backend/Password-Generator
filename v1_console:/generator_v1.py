import random  # imports the random module for generating random characters
import string  # imports the string module which contains ready-made character sets

def generate_password(length=12): # function generates a password, def length is 12

  letters = string.ascii_letters  # all uppercase + lowercase English letters
  digits = string.digits          # numbers 0–9
  symbols = string.punctuation    # special characters like !@#$%^&*

  all_chars = letters + digits + symbols # combine all character sets into one string

  password = ''.join(random.choice(all_chars) for _ in range(length)) 
# random.choice() picks 1 random character each time
# the generator runs "length" times
# join() glues all chosen characters into one final password string

  return password  # return the final generated password

user_length = int(input("Password length: ")) # ask the user for the length and convert to integer
print("Your password:", generate_password(user_length))  # call the function with user input and print result