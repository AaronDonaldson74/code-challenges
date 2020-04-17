# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# Sample String : 'python'
# Expected Result : 'pyon'
# Sample String : 'py'
# Expected Result : 'pypy'

poppins = "Supercalifragilisticexpialidocious"

first_letters = (poppins[0:2])
last_letters = (poppins[-2:])

print(first_letters+last_letters)

mary = "Toppins"
first = (mary[0:2])
last = (mary[-2:])

if len(mary) > 2:
  print(first+last)
elif len(mary) == 2:
  print(mary+mary)
else:
  print('""') 
# Extra Credit: Check if the string length is less then 2. If the length is less then 2 print an empty string, else print the first 2 and the last 2 chars.

# Python conditions. https://www.w3schools.com/python/python_conditions.asp
# Sample String : 'f'
# Expected Result : ""