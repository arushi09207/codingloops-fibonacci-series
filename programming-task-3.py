# operations on data structures 


#1. ASSIGNING ELEMENTS FROM A LIST IN PYTHON

#Append method : adds element to the end of the list
lst = [] #empty list
lst.append(4)
print(lst)
lst1 = ['a','b',2,3] #existing list
lst1.append(4)
print(li)

#Insert method : inserts element to the specific position in the list
lst1 = ['a','b',2,6,4] #existing list
lst1.insert(5,3) #pos : 5 , ele : 3

#Extend method : extends our list by adding list or any combination of elements in lists,tuples,etc
lst2 = ['a','s','d','f']
lst3 = ['g','h','j','k','l']
lst2.extend(lst3)
print(lst2)


#2. ACCESSING ELEMENTS FROM A TUPLE IN PYTHON

# Indexing method : using the index of the element we can access elements of a tuple
tup = ('a',1,'2')
print(tup[0])

#Slicing method : we slice out various elements in the specific order from the tuple
print(tup[:1])
print(tup[:])

#3. DELETING DIFFERENT DICTIONARY ELEMENTS 

# Delete method : removes the key but raises an keyerror if key doesn't exists
dict1 = { 'a' : 1,
          'b' : 2,
          'c' : 3,
          'd' : 4}
del dict1['a']
print(dict1)

# Pop method : delete a key and doesn't raise a keyerror if assigned a value to key
dict1.pop('e','no')
print(dict1)
