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

name = "John Doe"
print(type(name))
num1 = 10
print(type(num1))
num2 = 10.5
print(type(num2))
num3 = 2j
print(type(num3))
ls = [1,2,3,4,5]
print(type(ls))
tp = (1,2,3,4,5)
print(type(tp))
dic = {"name":"John Doe", "age":26}
print(type(dic))
st = {"John Doe",26}
print(type(st))

frst = frozenset({"hello"})
print(type(frst))
bln = True
print(type(bln))

byt = b'hello'
print(type(byt))
bytearray = bytearray(b'hello')
print(type(bytearray))
none = None
print(type(none))










