# STRING MANIPULATION


# 1. Create a new string made of first, middle, and last character

s = input("Enter a string: ")
mid_index = len(s)//2
new_s = s[0] + s[mid_index] + s[-1]
print("New string:", new_s)




# 2. Count occurrences of all characters in a string

s = input("Enter a string: ")
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print("Character frequencies:", freq)





# 3. Reverse a given string

s = input("Enter a string: ")
reversed_s = s[::-1]
print("Reversed string:", reversed_s)





# 4. Split a string on hyphens

s = input("Enter a string with hyphens: ")
split_s = s.split('-')
print("Split string:", split_s)






# 5. Remove special symbols / punctuation from a string

import string
s = input("Enter a string: ")
clean_s = ''.join([c for c in s if c.isalnum() or c.isspace()])
print("Cleaned string:", clean_s)





# LIST MANIPULATION


# 1. Reverse a list in Python

lst = [1,2,3,4,5]
reversed_lst = lst[::-1]
print("Reversed list:", reversed_lst)





# 2. Turn every item of a list into its square

lst = [1,2,3,4,5]
squared_lst = [x**2 for x in lst]
print("Squared list:", squared_lst)






# 3. Remove empty strings from a list of strings

lst = ["Python", "", "Java", "", "C++"]
clean_lst = [x for x in lst if x != ""]
print("List without empty strings:", clean_lst)





# 4. Add new item to list after a specified item

lst = ["a","b","c","d"]
item_to_add = "x"
after_item = "b"
index = lst.index(after_item)+1
lst.insert(index, item_to_add)
print("Updated list:", lst)




# 5. Replace list’s item with new value if found

lst = ["a","b","c","d"]
old_value = "c"
new_value = "z"
if old_value in lst:
    index = lst.index(old_value)
    lst[index] = new_value
print("Replaced list:", lst)






# DICTIONARY MANIPULATION


# 1. Check if a value exists in a dictionary

d = {'a':10,'b':20,'c':30}
value_to_check = 20
exists = value_to_check in d.values()
print("Value exists:", exists)







# 2. Get the key of minimum value from dictionary

d = {'a':10,'b':5,'c':30}
min_key = min(d, key=d.get)
print("Key of minimum value:", min_key)





# 3. Delete a list of keys from a dictionary

d = {'a':10,'b':20,'c':30,'d':40}
keys_to_delete = ['b','d']
for k in keys_to_delete:
    d.pop(k, None)
print("Dictionary after deletion:", d)






# TUPLE MANIPULATION


# 1. Reverse a tuple

t = (1,2,3,4,5)
reversed_t = t[::-1]
print("Reversed tuple:", reversed_t)





# 2. Access value 20 from the tuple

t = (10,20,30,40)
print("Accessed value:", t[1])





# 3. Swap two tuples

t1 = (1,2,3)
t2 = (4,5,6)
t1, t2 = t2, t1
print("Swapped tuples:", t1, t2)






# LOOP MANIPULATION


# 1. Print first 10 natural numbers using while

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()







# 2. Print even numbers till input number

n = int(input("Enter a number: "))
for i in range(2, n+1, 2):
    print(i, end=" ")
print()






# 3. Print odd numbers till input number

n = int(input("Enter a number: "))
for i in range(1, n+1, 2):
    print(i, end=" ")
print()





# 4. Print prime numbers till input number

n = int(input("Enter a number: "))
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()





# 5. Print multiplication table of a given number

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")