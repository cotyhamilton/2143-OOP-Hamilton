"""
Name: Coty Hamilton
Email: cotyhamilton@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 31 Jan @ 11:00 p.m.
"""


# ---
#   A: What would Python print?
# ---


a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1, 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 3]


# ---
#   B: Write a function that removes all instances of an element from a list.
# ---


x = [3, 1, 2, 1, 5, 1, 1, 7]

def remove_all(el, lst):
    # remove() removes the first occurence in a list
    while (el in lst):
        lst.remove(el)
    return lst

print (remove_all(1, x))
# Prints: [3, 2, 5, 7]


# ---
#   C: Write a function that takes in two values, x and y, and a list, and adds as many y's to the end of the list as there are x's. Do not use the built-in function count.
# ---


lst = [1, 2, 4, 2, 1]

def add_this_many(x, y, lst):
    for i in lst:
        if i == x:
            lst.append(y)
    return lst

print (add_this_many(1, 5, lst))
# Prints: [1, 2, 4, 2, 1, 5, 5]


# ---
#   D: What would Python print?
# ---


a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: [5, 3, 3, 1] (Wrong)
    # Correct Answer: []
    # Doesn't do the wrap around, lol

print(a[1:-2])
# Prints: [1, 3, 3, 5, 2] (Wrong)
    # Correct Answer: [1, 4, 2]
    # finds -2 index, moves forward as normal

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]


# ---
#   E:  Let's reverse Python lists in place, meaning mutate the passed in list itself, instead of returning a new list. We didn't discuss this in class directly, so feel free to use google. Why is the "in place" solution preferred?
# ---


x = [3, 2, 4, 5, 1]

def reverse(lst):
    for i in range(0, len(lst)-1):
         lst.insert(len(lst)-1-i,lst.pop(0))
    return lst

print (reverse(x))
# Prints: [1, 5, 4, 2, 3]


# ---
#   F: Write a function that rotates the elements of a list to the right by k. Elements should not "fall off"; they should wrap around the beginning of the list. rotate should return a new list. To make a list of n 0's,you can do this: [0] * n
# ---


x = [1, 2, 3, 4, 5]

def rotate(lst, k):
    rList = [0] * len(lst)

    for i in lst:
        rList[((lst.index(i) + k) % len(lst))] = i
    return rList

print (rotate(x, 3))
# Prints: [3, 4, 5, 1, 2]


# ---
#   H: Continuing from above, what would Python print? (something about sportsball)
# ---


superbowls = {
    'peyton manning': 1,
    'tom brady': 3,
    'joe flacco': 1,
    'joe montana': 4}

print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {('eli manning', 'giants'): 2, 'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {3: 'cat', ('eli manning', 'giants'): 2, 'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {3: 'cat', ('eli manning', 'giants'): 5, 'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

# superbowls[['steelers', '49ers']] = 11
# can't use list (or any mutable objects) as key in dict
# print(superbowls)
# Prints: {['steelers', '49ers']: 11, 3: 'cat', ('eli manning', 'giants'): 5, 'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4} (wrong)
    # Correct Answer: error


# ---
#   I: Given a dictionary replace all occurrences of x as the value with y.
# ---


d = {1: {2:3, 3:4},
    2:{4:4, 5:3}}

def replace_all(d, x, y):
    for k,v in d.items():
        if type(v) is dict:
            replace_all(v,x,y)
        else:
            if v == x:
                d[k] = y
    return d

print(replace_all(d, 3, 1))
# Prints: {1: {2: 1, 3: 4} 2: {4: 4, 5: 1}}

# ---
#   J: Given a (non-nested) dictionary delete all occurences of a value. You cannot delete items in a dictionary as you are iterating through it (google :) ).
# ---


d = {1:2, 2:3, 3:2, 4:3}

def rm(d, x):
    rmKey = []
    # list to populate with keys that need to be removed from d
    for k,v in d.items():
        if v == x:
            rmKey.append(k)
    for j in rmKey:
        del d[j]
    return d

print (rm(d,2))
# Prints: {2: 3, 4: 3}