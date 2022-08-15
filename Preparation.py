
# data = 'Hello World'     # store value in a data variable
# print(data)


# print('Hello World')   #first python program


# print multi pieces of data separately
# print(50)
# print('Hello World')
# print(3.14)
# print multiple data 
# print(10,3.14444,'Hello World')


""" complex number left number is real part and the second number is imaginary part 
 complex is used to create complex numbers """

# complex_Num = complex(2,4) 
# print(complex_Num)
# print(complex(45,30))     #complex is used to create complex number


# print(True)
# p_false = False
# print(p_false)


# print(True & False)   #if atleast one false then all the value is False
# print(True or False)   #if atleast one true then all the value is True


# str1 = "Hello World str1"     # these are all string type different quotes
# print(str1)
# str2 = 'Hello World str2'     #IDE bydefault provide double quotes but we change it in single quotes 
# print(str2)                 # and triple quotes is used for more then one line string
# str3 = '''hello
# world
# how
# are
# you str3'''
# print(str3)


# str_len = 'Hello World'    #len is used to fine the length of string
# print(len(str_len))
# print(str_len[0])        #[0] used to find the zero index position element 
# print(str_len.count(" "))    # count is used to count the spaces between string 
  

# str = 'Hello'    #id is used to find the id of string
# print(id(str))
# str = 'world'
# print(id(str))


# val = None
# print(val)               # type is used to find the type datatype
# print(type(val))


# str = 'Hello World'
# print(str)
# print(type(str))


# str = '0123456789'
# print(str[0:5])    #it start from 0 and never add the fifth position character
# print(str[:5])    #it also start from 0 and never add the fifth position character
# print(str[1:])    #it start from 1 and never stop until the string will not ended
# print(str[2:3])
# print(str[8:len(str)])
# print(str[:8:3])


# str = 'hello world'
# print(str[::-1])          #Reverse String


# str = 'Hello world %s'%'How are You'
# temp = 'django'                       #inserting string
# str = 'I like %s and %s' % ('python',temp)
# print(str)          


# str = "%i + %i = %i" % (2,4,5)
# print(str) #inserting integer with in a string 


# str = '%f' % (1.111)
# print(str)
# str = '%.2f' % (1.1111)
# print(str)                  #%f is used to substitute floats


# num1 = 10
# num2 = 20               #bitwise operator
# print(num1 & num2)
# print(num1 | num2)
# print(num1 ^ num2)
# print(num1 << num2)
# print(num1 >> num2)
# print(~num2)


# house = 5
# new_house = 5
# print(house  <= new_house)
# print(house  >= new_house)
# print(house  == new_house)
# print(house  > new_house)
# print(house  < new_house)


# str = 'hello world how ar you'
# print('how' in str)
# print('it' in str)


# G = 6.67e-11
# M = 6e+24           # Gravitational Force     
# m = 7.34e+22        # Fg = GMm/r(square)
# r = 384000000.0
# GMm = 2.937468e+37
# r = 1.47456e+17
# Fg = GMm/r
# print(Fg)


# a = 10
# b = 20            #conditions 
# c = 30
# if a < b:
#     print('a is less than b')
# elif( a > b):
#     print('a is greater than b')
# elif( a+b == c):
#     print('a plus b is equal to c')


# num = 20
# num1 = 40
# num3 = 35           
# if num%2==0 and num3%2==0:
#     print('20 is multiple of 2')       # "and" "or" operators use in conditions
# else:
#     print('this is odd number')

# if num%2==0 or num3%2==0:
#     print('20 is multiple of 2')
# else:
#     print('this is odd number')


# nested conditions
# num = 100
# if num > 0 and num <= 100:
#     if num >=10 and num<=200:
#         if num >=100 and num < 1000:
#             print('That is nested loop')


# num = 10
# num2 = 20
# if num < num2:
#     print(num)   #find the minimum number


# array = [7,3,2,6,5,4,9,8]
# print(min(array))           # min max by built in function
# print(max(array))

# array = [7,3,2,6,5,4,9,8]
# array2 = array[0]
# for num in array:              # find the minimum number
#    if num < array2:
#       array2 = num
# print(array2)



# def index():                # use of functions
#     print('Hello world')
# index()


# def index2(x):  #define a parameter in a function
#     print(x+5)
# index2(5)


# def index(first_num,second_num):
#     if first_num > second_num:
#         print('first No is greater')
#     else:
#         print('second No is greater')
# num = 10
# num1 = 20
# result = index(num,num1)
# print(result)


# def index(first_num,second_num):
#     if first_num > second_num:
#         return first_num
#     else:
#         return second_num
# num = 10
# num2 = 20
# result = index(num,num2)
# print(result)


# list = [10,20,30,40,50]           #function scope 
# def multiply_by(my_list):
#     my_list[0] *= 10
#     my_list[1] *= 10
#     my_list[2] *= 10
#     my_list[3] *= 10
#     my_list[4] *= 10
# multiply_by(list)
# print(list)


# str = "Hello world"   # find the substring
# print(str.find("o"))


# str = 'Hello this is educative'  #replace is used to replace the string with other
# str_replace = str.replace('Hello this is','Hello')
# print(str_replace)

# str = 'hello world'
# str1 = str.upper()
# print(str1)


# str = 'HELLO WORLD'   #lower is used to change the upper case to lower case string
# print(str.lower())


# list = ['a','b','c']
# print('+'.join(list))


# list = ['a','b','c']
# print(','.join(list))


# formate_str = 'Hello world {a}'.format(a = 'How are you')
# print(formate_str)  #string formating



# a = int("5")
# b = int("5")     # (a + b) = c condition
# c = 10
# if a + b == c:
#     print(c)
# else:
#     print(False)



# str_ord = "1"       # "ord" is used to get unicode value of string type character
# print(ord(str_ord))


# num = 2   # float is used to convert the int to floating point number
# print(float(num))


# str_con =  'Hello ' + str(5)
# print(str_con)


# input_str = input('What is your Name? ')
# print('Hello '+ input_str)


# def add(num1,num2):
#     return num1+num2
# def sub(num1,num2):
#     return num1-num2
# def mul(num1,num2):
#     return num1*num2
# def div(num1,num2):
#     return num1/num2
# def calculator(operation,num1,num2):
#     return operation(num1,num2)
# result = calculator(mul,10,10)
# print(result)
# result = calculator(sub,10,10)
# print(result)


# def calculator(operation,n1,n2):   # lambda operator is used to asign values to n1 and n2
#     return operation(n1,n2)
# result = calculator(lambda n1,n2:n1*n2,10,20)
# print(result)
# result = calculator(lambda n1,n2:n1+n2,10,20)
# print(result)

 
# num_list = [1,2,3,4,5]
# list1 = map(lambda n: n * 2, num_list)
# print(list(list1))


# num = [10,20,30,40,50]
# list_1 = list(filter(lambda n:n>20,num))
# print(list_1)


# def rec_cat(x,y):
#     con_x = str(x)*10
#     con_y = str(y)*5
#     print(con_x+con_y)
# rec_cat(3,4)


# For loop to find even and odd values b/w 1,10 with 2 steps
# for n in range(1,10,2):
#     if n % 2 == 0:
#         print(n, 'is even')
#     else:
#         print(n, 'is odd')



# float_list = [2,3,4,5,6,7,8]
# print(float_list)         # double the 2nd list using loop
# for n in range(0,len(float_list)):
#     float_list[n] = float_list[n]*2
# print(float_list)


# num = 40
# array = [10,20,30,40,50]
# for n1 in array:          #find number that sum is equal to third using loop and condition on array and number 
#     for n2 in array:
#         if n1 + n2 == num:
#             print(n1,n2)


# n = 50
# array = [20,30,40,50,60]
# found = False
# for n1 in array:
#     for n2 in array:
#         if n1 + n2 == n:
#             found = True
#             break
#     if found:
#         print(n1,n2)
#         break


# def check_balance(brackets):
#     check = 0
#     for bracket in brackets:
#         if bracket == '[':
#             check += 1
#         elif bracket == ']':
#             check -= 1
#         if check < 0:
#             break
#     return check == 0
# bracket_string = '[[[]]]'
# print(check_balance(bracket_string))


# def check_sum(list):
#     for first in range(len(list)):
#         for second in range(first , len(list)):
#             if list[first] + list[second] == 0:
#                 return True
#     return False
# list = [10,-20,5,-5,-20]
# print(check_sum(list))



# Data Sturcture Chapter

# list1 = range(0,10)
# print(list(list1))

# list2  = range(3,30,5)
# print(list(list2))


# product = [['milk',20],['vegetable',30],['oil',40]]
# print(product[0])           #sequential indexing
# print(product[1][0])
# print(product[2][0])


# a = [1,2,3,4]
# b = [1,2,3,4]
# c = a + b
# print(c)

# a = [1,2,3,4]
# b = [5,6,7,8]
# a.extend(b)
# print(a) 


# a = [1,2,3]
# a.append(4)
# a.append(5)
# a.append(6)
# print(a)

# a = [1,2,3]
# a.insert(2,4)
# print(a)

# list = ['abc','def','hij']
# print(list)
# list2 = list.pop()
# print(list2)

# list = ['abc','def','hij']
# list.remove('abc')
# print(list)


# list = ['abc','def','hij']      # find index of an element 
# print(list.index('abc'))


# list = ['abc','def','hij']
# print('abc' in list)
# print('abc' not in list)


# list = [7,6,5,3,1,2]
# list.sort()
# print(list)


# list = [2,3,4,6]
# list1 = [n*2 for n in list]
# print(list1)


# list = [10,20,30,40]
# list1 = []
# for n in list:
#     list1.append(n*2)
# print(list)
# print(list1)


# list = [1,2,3,4,5]
# list1 = [n*2 for n in list]
# print(list)
# print(list1)


# list  = [1,2,3,4,5,6]
# list2 =  [n*2 for n in list if n%2==0]
# print(list)
# print(list2)
  

# str = 'this is my cat'
# str_sort = ''.join(sorted(str))
# print(str_sort)




# pakistan = [5,4,3,6,8]
# new_pakistan = []
# while pakistan:             #sorting of an array
#     recover = pakistan[0]
#     for suba in pakistan:
#         if suba < recover:
#             recover = suba
#     pakistan.remove(recover)
#     new_pakistan.append(recover)
# print(new_pakistan)


# dic_reco = {
#     'name':'Rashid',
#     'age':24,
#     'phone': 30475528384
# }
# print(dic_reco['name'])


# list = dict(name = 'Rashid', age = 24, phone = 7552384)
# list['roll'] = 30         # insert new element in an array
# print(list)


# my_list = [44, 82, "Rashid", 77, "Ali"]
# tuple = (my_list[0],my_list[len(my_list)-3], len(my_list))
# print(tuple)


# list2 = [40,35,82,14,22,66,53]
# list1 = []
# while list2:
#     temp = list2[0]
#     for x in list2:
#         if x > temp:            # kth_max = 66
#             temp = x            # kth_min = 22
#     list2.remove(temp)
#     list1.append(temp)
# kth_max = list1[-2]
# kth_min = list1[-6]
# print([kth_max,kth_min])



# list = [40,35,82,14,22,66,53]
# k = -2
# list.sort()
# print(list[k])


import datetime
from datetime import date
import datetime as dt
import math
import heapq
from os import dup
import random
import time
import calendar




# factorial_of_5 = math.factorial(8)
# print(factorial_of_5)

# gcd_math = math.gcd(300,200)
# print(gcd_math)

# log_math = math.log(10,20)
# print(lcm_math)


# import heapq
# heap = []
# heapq.heappush(heap,5)
# heapq.heappush(heap,10)
# heapq.heappush(heap,15)
# heapq.heappush(heap,20)
# result = heapq.heappop(heap)
# print(result)




# num = random.random()
# print(num)


# range = random.uniform(30,50)
# print(range)


# list = [3,6,8,0,8,6,5,4,3,2]
# random.shuffle(list)
# print(list)



# def find_max(lis):
#     sum1 = sum(list[0])
#     sum2 = sum(list[1])
#     sum3 = sum(list[2])
#     list2 = [sum1,sum2,sum3]
#     print(list2)
# list = [[1, 2, 3], [2, 3, 3], [1, 3, 3]]
# find_max(list)




# list = [9, 8, 7]
# new_list =  [[x for x in[list]] for x in range(3)]
# print(new_list)


     
# list = [a for a in range(20) if a%2!=0]   # even and odd number in single loop
# print(list)
# new_list = [a for a in range(20) if a%2==0]
# print(new_list)



# my_list = ['Hello', 'World', 'Python']
# temp = [a[0].upper() for a in my_list]
# print(temp)




# list = [1,2,3,4,5]
# print(list.pop(-1))
# print(list.remove(list[-2]))



# dictionary = {
#     'Rashid':1,
#     'Apple':2,
#     'Amazon':3
# }
# for (key,value) in dictionary.items():
#     print(key,value)


#
# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# list = []
# list2 = []
# while duplicate:
#     temp = duplicate[0]
#     for x in duplicate:
#         if x < temp:       #sorting
#             temp = x
#     duplicate.remove(temp)
#     list.append(temp)
# print(list)
# for x in list:       #remove duplication
#     if x not in list2:
#         list2.append(x)
# print




# list_a = [3,2,1,5,6,5,4,3,2,1]
# list = []
# for x in list_a:
#    if x not in list:
#       list.append(x)
# list1 = []
# while list:
#    temp = list[0]
#    for x in list:
#       if x < temp:
#          temp = x
#    list.remove(temp)
#    list1.append(temp)
# print(list1)




# import time
# localtime = time.asctime(time.localtime(time.time()))
# print ("Local current time :", localtime)


# import calendar
# cal = calendar.month(2022,8)
# print ("Today Calendar:")
# print (cal)
#!/usr/bin/python



# class Teacher:
#    stuCount = 0
#    def __init__(self,name,roll):
#       self.studentName = name
#       self.studentRoll = roll           #function to find the student name and roll using Teacher Class
#       Teacher.stuCount += 1
#    def DisplayeStudentDetail(self):
#       print('Student Name : ' ,self.studentName, ' Student Roll :',self.studentRoll)
#
# stu1 = Teacher('Rashid',12)
# stu2 = Teacher('Umar',13)
# stu1.DisplayeStudentDetail()
# stu2.DisplayeStudentDetail()
# print('Total Student : ',Teacher.stuCount)