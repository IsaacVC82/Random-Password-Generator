import random as  random 
import secrets as secrets 
import string
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

print ("Welcome to your password generator: ")
number = input("How many passwords you want to generate? : ")
number= int(number)

pwd_length= 12

pwd = ""

print("\nhere are your password: ")
for pwd in range(number):
  passwords= ""
  for c in range(pwd_length):
     passwords += random.choice(alphabet)
  
   
  print(passwords)
      



