
#break a string into list items.
#set the first letter to be a key dictionary item with a value 1.
#loop the function setting letters to be key and value 1.
#if conditional should add x += 1 to value if key == key.


#need a string
#add character to dictionary with a value of one
#if the character already exhists in the dic incrememnr the value by one
#return dictionary when loop is finished

string = "mississippi"
dic = {}
for char in string:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1
    
print(dic)

