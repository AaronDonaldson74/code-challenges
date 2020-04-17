# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

poppins = "supercalifragilisticexpialidocious"

# found_s = poppins.replace("s", "$")
# print(found_s)

# first_char = poppins[0]
# print(first_char)

#This was wrong, because it only kept the first letter because it was capitalized.

# for char in poppins:
#     if char == first_char:
#         print('fount it')

# new_word = ''
# for char in poppins:
#     if char == first_char:
#         new_word += '$'
#     else:
#         new_word += char
# print(new_word)

# poppins_minus_first_char = poppins[1:]
# print(poppins_minus_first_char)


#########Have to tackle this another day######### writeout a plan of steps.

string = "supercalifragilisticexpialidocious"
first_char = string[0]
replaced_word = string[1:].replace(first_char, "$")
print(first_char + replaced_word)
