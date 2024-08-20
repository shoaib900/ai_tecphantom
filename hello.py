# 01 single and multiple lines compiled into one line

# print("hello world")

"""
print("hello world")
hello world
"""

# 02 legal variable name: 

# myname = "John Doe"
# name = "Jane Doe"
# _name1= "Jane Doe" # snake case writing style
# nameFirst = "Jane" # camel case writing style
# NameFirst = "Jane" # pascal case writing style
# name1st = "Jane"
# name-name = "Jane" # hyphenated writing style

# 03 variable for string and number concatenation:

# name = "John Doe"
# age= "26"
# print("Hello, my name is " + name + " "+ age)

# name1 = "John Doe"
# name1 = "Jane mark"
# print(name1)

# age1 = 26
# age2 = 27
# print(age1 , age2)

# 04 familiar and unfamiliar operators:

# a = 10
# a = 10 + 10
# a = a + 10
# a -= 10
# print(a)

# 05 math ambiguity: 

# a =  (2 + 3) * 5
# print(a)

# 06 if condition:
# x = 11

# if x == 10:
#     print("x is 10")
# else:
#     print("x is not 10",x)

# if x == 10:
#     print("x is 10")
# elif x == 20:
#     print("x is 20")
# else:
#     print("x is neither 10 nor 20",x)

# marks = 80

# if marks >= 90:
#     print("Excellent! Grade A")
# elif marks > 80:
#     print("Good! Grade B")
# else:
#     print("Fail! Grade F")

# hp = 10

# if hp != 10:
#     print("Healthy")
# else:
#     print("Unhealthy")

# 07 input 

# name = input("Enter your name: ")

# print("Hello, ", name)

# 08 input if condition:

# num = input("Enter your number: ")
# num = int(num)
# print(type(num))

# if( num >= 90):
#     print("Grade A")
# elif num >= 80:
#     print("Grade B")
# elif num != 75:
#     print("Grade C")
# else:
#     print("Grade D")

# 09 if test of conditions 

# marks = 79

# if (marks >= 90 and marks <= 100):
#     print("Excellent! Grade A")
# elif (marks >= 80 and marks < 90):
#     print("Good! Grade B")
# elif (marks >= 70 and marks < 80):
#     print("Average! Grade C")
# else:
#     print("Invalid grade")

# num1 = 10
# num2 =110

# if (num1 > 10 or num2 < 90):
#     print("num1 is greater than 10 ")

# 10 nested if statement 

# num1 =11
# num2 = 11

# if num1 == 10:
#     if (num2 == 11):
#         print("Both numbers are true")
#     else:
#         print("num1 is true but num2 is false")
# else:
#     print("num1 is false")

#  11  lists

# names = [89]
# names =  ["data"] + names + ["John Doe"]
# names.append("Shoaib")
# names.insert(1,34)
# print(type(names), names)

# ls1 = [1,2,3,4,5]
# ls2 = [6,7,8,9,10]
# ls1.extend(ls2)
# print(ls1)

# ls = [ "a",1,2,3,4,5]
# del ls[0]
# del ls[0]
# ls.remove("a")
# print(ls)
# ls2 = ls[0::4]
# print(ls2)

# ls= [3,2,1,5,7,6]
# ls.sort()
# print(ls)
# ls.sort(reverse=True)
# print(ls)
# ls.pop(-5)
# print(ls)
# le = len(ls) -1
# print(le)

# 12 data types 

# name = "John Doe"
# print(type(name))
# num1 = 10
# print(type(num1))
# num2 = 10.5
# print(type(num2))
# num3 = 2j
# print(type(num3))
# ls = [1,2,3,4,5]
# print(type(ls))
# tp = (1,2,3,4,5)
# print(type(tp))
# dic = {"name":"John Doe", "age":26}
# print(type(dic))
# st = {"John Doe",26}
# print(type(st))

# frst = frozenset({"hello"})
# print(type(frst))
# bln = True
# print(type(bln))

# byt = b'hello'
# print(type(byt))
# bytearray = bytearray(b'hello')
# print(type(bytearray))
# none = None
# print(type(none))


# 13 tuples

# tup = ("hello","world")
# print(tup)
# print(type(tup))
# tup1 = ("hello world",)
# print(type(tup1))

# tup = (1,2,3,4)
# tup2 = (True,False,True,False)
# tup3= ("q","a","b","c")
# tup4 = (True,"h",3)
# print(tup,tup2,tup3,tup4)

# tup = tuple((1,2,3,4))
# print(tup)

# tup = ("hello ",1,2,3,4)
# print(len(tup))
# print(tup[0])
# y = list(tup)
# print(y)
# y.append("world")
# print(y)
# tup = tuple(y)
# print(tup)
# print(type(tup))

# tup1 = ("hello","world")
# tup2 = ("!",)
# tup1 += tup2
# print(tup1)
# tup = ("!",)
# print(type(tup))

# tup = (1,"2",3,4)
# y = list(tup)
# y.pop(0)
# print(y)
# y.remove("2")
# del y[1]
# del y[1]
# print(y)
# y.insert(0,"hello")
# print(y)
# tup = tuple(y)
# print(tup)



# 14 dictionaries
# thisdict = {"name":"John Doe", "age":26, "city":"New York","list":["hello","world","!"]}

# thisdict["first name"] = "Ashutosh"
# print(thisdict["name"])

# x = thisdict.get("name")
# print(x)
# # thisdict.update({"last name":"hello mira"})
# print( thisdict.values())
# print(thisdict.keys())
# print(thisdict)

# prnt = {
#     "child1":{
#         "name":"ashutosh",
#         "age":24,
#     },
#     "child2":{
#         "name":"Aslam",
#         "age":30,
#     },
#     "child":{
#         "name":"afaq",
#         "age":12
#     }
# }

# prnt["child1"] = "Ashutosh Khan"
# prnt2 = prnt.copy()
# print(prnt)
# print(prnt2)

# dic1 = {"name":"John Doe", "age":26, "city":"New York"}
# dic2 = dic1.copy()
# dic1["name"] = "Ashutosh"
# print(dic1)
# print(dic2)


# print(prnt)
# print(prnt2)
# print(prnt)
# print(prnt2)

# print(prnt)
# print(prnt["child1"]["name"])
# prnt["child1"]["name"] = "Ashutosh Khan"
# print(prnt)

# 15 sets

# set1 = {1,2,3,4,5}
# set2 = {"hello","world","!"}
# set3 = {True,False,0,1}
# print(set1, type(set1))

# set1 = set({1,2,3,4,5})
# print(set1, type(set1))

# set1 = {1,2,3,4,5}
# set2 = {"hello","world","!",9}


# set1.update(set2)
# set1.add(6)
# print(set1)
# print(len(set1)-1)

# set1 = {1,2,3,4,5}
# set2 = {5,6,7,8,9,10}
# set3 = {11,12,13,14,15}
# set1.remove(2)
# set1.discard(9)
# set3 = set1.union(set2)
# set4 =set1|set2|set3
# set4 = set1.intersection(set2,set3)
# set4 = set1 & set2
# set4 = set1 | set2 & set3 
# set4 = set1.difference(set2)
# set4 = set1 - set2
# print(set4)

# set1 = {1,2,3,4,5}
# print( 1 in set1)


# 16 Break continue and pass statements

# for i in range(5):
#     print(i)
#     if i == 2:
#         pass


# 17 conditional ternary operator
# x = 10
# print("pass") if x == 10 else print("x is not 10")

# 18 while loop, for loop
# li = [1,2,3,4,5]

# for x in li:
#     print(x)

# i=0
# while i<5:
#     print(i)
#     i+=1


# 19 nested loops

# name1 = ["John","Ashutosh","John Doe"]
# name2 = ["John","Ashutosh","John Doe"]
# for i in name1:
#     for j in name2:
#         print(i,j)


# 20 list comprehension

# ls1 =[ "apple", "banana", "cherry"]
# ls2 =[]
# for i in ls1:
#     if "a" in i:
#         ls2.append(i)
# print(ls2)
# ls3 =[i for i in ls1 if "a" in i]
# print(ls3)


# 21 iterators and iterables




