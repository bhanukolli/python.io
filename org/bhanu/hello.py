#!/usr/bin/env python

print ('Hello Bhanu....!')
i=0
if True:
    print("Hello Again")
elif False:
    print("Do Whatever you want")
else:
    print("Not again")

while i < 3:
    print("3 is greater")
    i += 1

my_names = ["bhanu" , "kolli" , "prakash"]

print(my_names[1]);

print(len(my_names));

my_names.append("ben"); # add element to array

"ben" in my_names == True # is present in array

del my_names[2] # delete from list

print(len(my_names)); # length of list

my_names[1:] # print except list

#loops

for name in my_names:
    print name
    print("My name is {0}".format(name))

#range function
me = 0
for index in range(10): # range (5, 10)
    me += 1
    print("Value {0}".format(me));

#break and continue

for name in my_names:
    if name == "ben":
        print "found"
        break
    print("Still searching")

#While loop

w = 0
while w < 10:
    print("count is {0}".format(w));
    w += 1

#Dictionaries

student = {
    "name": "mark",
    "id": 9898,
    "feedback": None
}


all_students =[
    { "name": "mark" , "id": 234},
    { "name": "ben", "id": 111}
]

print student["name"]

print student.get("name", "unkown")

student.keys()
student.values()
del student["name"]

# Exceptions
student["last_name"] = "kolli"
try:
    last_name = student["last_name"]
    print last_name
except KeyError:
    print("ERROR")
except TypeError as error:
    print("I can't add them ")
    print error
except Exception:
    print("Unknown")


print("Continue the program ")

#Other data types

# Complex , bytes , bytearray , tuple (immutable, cant change) , set (remove duplicates . order ) frozenset
