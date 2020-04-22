"""
remove_first_and_last(list_to_clean)

html = ['<h1>', 'Some content', '</h1>']

return a list, not a string.

1.Need a function that returns a list.
2.Need the function to remove the first element of the list.
3.Need the function to remove the last element of the list.
"""
"""{This one converts a string into a list then removes the first and last}
def term_one(to_list_one):
    li = list(to_list_one.split(" "))
    return li
    

str1 = "When in the course of human events"
# print(term_one(str1)[1:(len(term_one(str1))-1)])
given_list = term_one(str1)
print(given_list[1:(len(term_one(str1)))-1])
"""


"""This worked, but solution was different
second_list = ["item 1", "item 2", "item 3", "item 4"]

def chopper(*argchopped):
    for item in argchopped:
        return item

print(chopper(second_list)[1:(len(chopper(second_list)))-1])
"""


###Jordan's Solution###
def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean))