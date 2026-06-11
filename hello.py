# print('Hello world')

# if (1>2):
#     print('Yes')
# else:
#     print("No")
    
# a = 5
# y = 2

# print(a + y)

# print("Hello World!", end=" ")
# print("I will print on the same line.")

# print("I am", 35 , "years old")

# a = 'String'
# print(a)
# a = int(8)
# print(type(a))
# a = c = 'Kenneth'
# print(c)

# fruits = ['Oranges', 'Apples', 'Melon']
# x,y,z = fruits
# print(z+ " "+ x+ " "+ y)
# s = 5
# t = 'John'
# print(s, t)
# print('Hello','Hello')

# def myFunc():
#     print('Python in '+ t)
    
# myFunc()
# import random;
# print(random.randrange(1, 100))

# x = int(4.66)
# print(x)
# print(type(x))

# for x in "bananas":
#     print(x)

# a = 'Bananas'
# print(len(a))

# txt = "kennethmuriuki"
# if ("banaas" not in txt):
#     print("bananas")
# else:
#     print("Big Noooo")
# print("free" not in txt)
# print(txt[-5:].upper())
# d = '    I have a big whitespace, infront and also at back     '
# print(d)
# print(d.strip())
# print(d.replace('h', 'Q'))
# print(d.split(","))
# a = 'Hello'
# b= 'World'
# c = 35
# print(a + " " + b, c)
# number = 35
# txt = f'Hello World ', number
# print(txt)
# price = 60
# txt = f'The price for unga is {price:.2f} dollars'
# print(txt)
# txt = 'Hello\rNyumba!'
# print(txt)
# txt = 'hello world'
# print(txt.startswith('r'))
# thislist = ['apples', 'Oranges', 'Bananas', 'cherries']
# print(thislist)
# thislist[2:4] = ['Watermelon']
# print(thislist)
# thislist.insert(2, 'Sugar')
# print(thislist)
# thislist.append('Sugar')
# print(thislist)
# thislist2 = {'Mangos', 'Pineapples'}
# thislist.extend(thislist2)
# print(thislist)
# thislist.remove('Watermelon')
# print(thislist)
# thislist.pop()
# print(thislist)
# thislist.copy()
# print(thislist)
# for x in range(len(thislist)):
#     print(thislist[x])
    
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1
    
# [print(x) for x in thislist]

# newList = []
# for x in thislist:
#     if 'a' in x:
#         newList.append(x)
# print(newList)

# newList = [x if x != 'Bananas' else 'Oranges' for x in thislist]
# print(newList)
# thislist.sort()
# print(thislist)

# numberlist = [100, 50, 65, 82, 23]
# numberlist.sort(reverse=True)
# print(numberlist)

# def myFunc(n):
#     return abs(n - 50)

# newNumberlist = [100, 50, 65, 82, 23]
# newNumberlist.sort(key=myFunc)
# print(newNumberlist)

# thislistagain = ["banana", "Orange", "Kiwi", "cherry"]
# thislistagain.reverse()
# print(thislistagain)
# for x in thislistagain:
#     thislist.append(x)
# print(thislist)

# thislist.extend(thislistagain)
# print(thislist)


# thistuple = ('Apples', 'Mangos', 'Pineapples', 'Mangos')
# print(thistuple)
# y = list(thistuple)
# y.append('Kiwi') 
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)

# thistuple = ("apple", "banana", "cherry", 'apple')
# for i in range(len(thistuple)):
#     print(thistuple[i])


# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = 1 + i

# mytuple = thistuple * 2
# print(mytuple)

# counttuple = thistuple.index('apple')
# print(counttuple)

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# for i in thisset:
#     print(i)
# if ('chacoals' not in thisset):
#     print('YEEEEES')
# else:
#     print('NOOOOOO')
    
# thisset.add('Melon')
# print(thisset)
# thisset2 = ['Pineapple', 'Berry']
# thisset.update(thisset2)
# print(thisset)
# thisset.discard('Melon') 
# print(thisset)
# thisset.pop()
# print(thisset)
# thisset.clear()
# print(thisset)
# del thisset

# thisset = {"apple", "banana", "cherry"}
# x = frozenset({"apple", "banana", "cherry"})
# print(type(x))

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict['year'])
# x = thisdict.get('brand')
# print(x)
# x = thisdict.keys()
# print(x)
# thisdict['year'] = 2000
# print(thisdict)
# v = thisdict.values()
# print(v)
# thisdict['color'] = 'red'
# print(thisdict)
# z = thisdict.items()
# print(z)
# thisdict.update({"location": 'Nairobi'})
# print(thisdict)
# thisdict.pop('model')
# print(thisdict)
# thisdict.popitem()
# print(thisdict)
# # del thisdict['color']
# # print(thisdict)
# # # thisdict.clear()
# # # print(thisdict)
# # # del thisdict
# for x in thisdict:
#     print(thisdict[x])

# for x in thisdict.items():
#     print(x, y)
    
# thisdict2 = dict(thisdict)
# print(thisdict2)

# myfamily = {
#     "child1" : {
#         "name": 'Emil',
#         "year": 2004
#     },
#     "child2" : {
#         "name": 'Tobias',
#         "year": 2000
#     },
#     "child3" : {
#         "name": 'Linus',
#         "year": 2011
#     },
# }

# print(myfamily["child1"]["name"])

# for x, obj in myfamily.items():
#     print(x)
    
#     for y in obj:
#         print(y +':', obj[y])

# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# temperature = 22

# if temperature > 30:
#   print("It's hot outside!")
# elif temperature > 20:
#   print("It's warm outside")
# elif temperature > 10:
#   print("It's cool outside")
# else:
#   print("It's cold outside!")

# username = ""

# if len(username) > 0:
#   print(f"Welcome, {username}!")
# else:
#   print("Error: Username cannot be empty")

# a = 2
# b = 330
# # print("YEEs") if a > b else print("Noo")
# print("A") if a > b else print("=") if a == b else print("B")

# x = 15
# y = 20
# max_value = x if x > y else y
# print("Maximum value:", max_value)

# username = ""
# display_name = username if username else 'Guest'
# print("Welcome,", display_name)

# age = 25
# has_license = True

# if age >= 18:
#   if has_license:
#     print("You can drive")
#   else:
#     print("You need a license")
# else:
#   print("You are too young to drive")
  

# score = 85

# if score > 90:
#   pass 
# print("Score processed")

# value = 50

# if value < 0:
#   print("Negative value")
# elif value == 0:
#   pass # Zero case - no action needed
# else:
#   print("Positive value")

# day = 8
# match day:
#   case 1:
#     print('Monday')
#   case 2:
#     print('Tuesday')
#   case 3:
#     print('Wednesday')
#   case 4:
#     print('Thursday')
#   case 5:
#     print('Fridayy')
#   case 6:
#     print('Saturday')
#   case 7:
#     print('sunday')
#   case _:
#     print('Looking forward')

# month = 5
# day = 4
# match day:
#   case 1 | 2 | 3 | 4 | 5 if month == 4 :
#     print('A weekday in April')
#   case 1 | 2 | 3 | 4 | 5 if month == 5 :
#     print('A weekday in May')
#   case _:
#     print('No match')
    
    
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
# else:
#   print('i is no longer less than 6')

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == 'banana':
#     continue
#   print(x)

# for x in range(5):
#   if x == 2:
#     continue
#   print(x)
# else:
#   print('Finally finished!')

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# for x in [0, 1, 2]:
#   pass

# def my_function():
#   print("Hello from a function")

# my_function()

# def greeting():
#   return "Hello from a function"

# print(greeting())

# def my_function(fname):
#   print(fname + " Refsnes")
  
# my_function('Kenneth')

# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(name = "Buddy", animal = "dog")

# def my_function(fruits):
#   for fruit in fruits:
#     print(fruit)
# my_fruits = ['Apples', 'Melon', 'Mangos', 'Cherries']
# my_function(my_fruits)  

# def my_function(person):
#   print('Name:', person['name']) 
#   print('Age:', person['age'])
# my_person = {'name': 'Kenneth', 'age': 30}
# my_function(my_person)

# def my_function(x, y):
#   return x + y

 
# result = my_function(3, 8)
# print(result)

# def my_function(*name):
#   print("Hello", name)

# my_function("Emil", 'Kenneth')

# def my_function(*numbers):
#   if len(numbers) == 0:
#     return None
#   max_num = numbers[0]
#   for num in numbers:
#     if num > max_num:
#       max_num = num
#   return max_num
# print(my_function(2, 7, 1, 9, 0))


# def my_function(username, **kwagrs):
#   print("Username:", username)
#   print('Additional details:')
#   for key, value in kwagrs.items():
#     print(key, ":", value)
  
# my_function("murio", age=30, city="Nai")

# def my_function(a, b, c):
#   return a + b + c

# numbers = [1, 2, 3]
# result = my_function(*numbers)
# print(result)

# def my_function(fname, lname):
#   print("Hello", fname, lname)

# person = {'fname': 'Ken', 'lname': 'murio'}
# my_function(**person)

# def changecase(func):
#   def myinner(*args, **kwargs):
#     return func(*args, **kwargs).upper()
#   return myinner

# @changecase
# def myfunction(nam):
#   return 'Hello '+ nam
# print(myfunction('Kenneth'))

# def changecase(n):
#   def changecase(func):
#     def myinner():
#       if n == 1:
#         a = func().lower()
#       else:
#         a = func().upper()
#       return a
#     return myinner
#   return changecase

# @changecase(7)
# def myfunction():
#   return 'Hello Ken'

# print(myfunction())

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# def addgreetings(func):
#   def myinner():
#     return 'Hello ' + func() + " Have a good day!"
#   return myinner

# @changecase
# @addgreetings
# def myfunction():
#   return "Ken"

# print(myfunction())

# @changecase
# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)

# import functools

# def changecase(func):
#   @functools.wraps(func)
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return 'Have a great day!'

# print(myfunction.__name__)

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# def myfunction(n):
#   return lambda a : a * n

# myboudler = myfunction(2)
# mytrippler = myfunction(3)

# print(myboudler(11))
# print(mytrippler(11))

# numbers = [1, 2, 3, 4, 5, 6]
# double = list(map(lambda x: x * 2, numbers))
# print(double)

# odd_numbers = list(filter(lambda x: x  % 2 != 0, numbers))
# print(odd_numbers)

# students = [('Emil', 25), ('Tobias', 20), ('Linus', 15)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

# words = ["apple", "pie", "banana", "cherry"]
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)

# def countdown(n):
#   # Base case
#   if n <= 0:
#     print("Done!")
#     # Recursive case
#   else:
#     print(n)
#     countdown(n-1)
# countdown(5)

# def fibonacci(n):
#   if n <= 1:
#     return n
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)
  
# print(fibonacci(7))

# def sum_list(numbers):
#   if len(numbers) == 0:
#     return 0
#   else:
#     return numbers[0] + sum_list(numbers[1:])
  
# my_list = [1, 2, 3, 4, 5]
# print(sum_list(my_list))

# def find_max(numbers):
#   if len(numbers) == 1:
#     return numbers[0]
#   else:
#     max_of_rest = find_max(numbers[1:])
#     return numbers[0] if numbers[0] > max_of_rest else max_of_rest
  
# my_list = [1, 2, 3, 4, 5]
# print(find_max(my_list))



# def my_generator():
#   yield 1
#   yield 2
#   yield 3
  
# for value in my_generator():
#     print(value)
    
# def count_up_to(n):
#   count = 1
#   while count <= n:
#     yield count
#     count += 1
    
# for n in count_up_to(5):
#   print(n)
  
# def large_sequence(n):
#   for i in range(n):
#     yield i

# # This doesn't create a million numbers in memory
# gen = large_sequence(1000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def simple_gen():
#   yield "Emil"
#   yield "Tobias"
#   yield "Linus"
  
# gen = simple_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def echo_generator():
#   while True:
#     received = yield
#     print("Recieved:", received)
# gen = echo_generator()
# next(gen)
# gen.send('Hello')
# gen.send('world')

# def my_gen():
#   try:
#     yield 1
#     yield 2
#     yield 3
#   finally:
#     print('Generator closed')
    
# gen = my_gen()
# print(next(gen))
# gen.close()
# x = range(3, 15, 2)
# print(x)
# print(list(x))

# for i in range(40, 60, 5):
#   print(i)

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# for i in mytuple:
#   print(i)

# class mynumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
  
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
  
# myclass = mynumbers()
# myit = iter(myclass)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# from mymodule import greeting
# from mymodule import person1

# greeting('Kenneth')

# a = person1['age']
# print(a)
# y = dir(person1)
# print(y)

# import platform

# x = platform.system()
# print(x)
# x = dir(platform)
# print(x)

# import datetime

# x = datetime.datetime.now()
# print(x.day)
# print(x.strftime("%A"))

# x = min(5, 10, 25)
# y = max(5, 10, 25)

# print(x)
# print(y)

# x = abs(-7.76)
# print(x)

# x = pow(4, 3)
# print(x)

# import math

# x = math.sqrt(125)
# print(x)

# x = math.ceil(1.4)
# y = math.floor(1.4)

# print(x)
# print(y)

# y = math.pi
# print(y)

# import json

# x = '{"name": "Kenneth", "age": 35, "location": "Nairobi"}'
# y = json.loads(x)
# print(y["age"])

# x = {
#   "name": "kenneth",
#   "age": 35,
#   "location": "nairobi"
# }

# y = json.dumps(x)

# print(y)

# x = {
#   "name": "kenneth",
#   "age": 35,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann", "Billy"),
#   "pet": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "ford edgar", "mpg": 24.1}
#   ]
# }

# y = json.dumps(x, indent=4, separators=(". ", " = ",), sort_keys=True)
# print(y)

# try:
#   print(x)
# except NameError:
#   print("Variable is nto defined")
# except:
#   print("something went wrong")
  
# # y = True
# # while y == True:
# #   x = input("Enter a number")
# #   try:
# #     x = float(x);
# #     y = False
# #   except:
# #     print("Wrong input, please try again")
# # print("Thank you")

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age
    
  def greet(self):
    return "Hello, "+ self.name, self.age
  
  def welcome(self):
    message = self.greet()
    print(message, "! Welcome to our website")

p1 = Person("Emil")
p1.age = 36
p1.name = "Tobias"
p1.city = "Nairobi"

p1.welcome()
print(p1.city)

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.year = year
  
  def welcome(self):
    print("Welcome ", self.firstname, self.lastname, "to the class of ", self.year)

s1 = Student("Mike", "leo", 2019)
s1.printname()
print(s1.year)
s1.welcome()

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property
    
  def get_age(self):
    return self.__age
  
  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Emil", 25)
print(p1.name)
print(p1.get_age())
p1.set_age(26)
print(p1.get_age())

class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

class Car:
  def __init__(self, name, brand):
    self.name = name
    self.brand = brand
    self.engine = self.Engine()
  class Engine:
    def __init__(self):
      self.status = "Off"
      
    def start(self):
      self.status = "Running"
      print("Engine started")
    
    def stop(self):
      self.status = "Off"
      print("Engine stopped")
  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.name} {self.brand}")
    else:
      print("Start the engine first")
      
c1 = Car("Cazoo", "Toyota")
c1.drive()
c1.engine.start()
c1.drive()
    
class Computer:
  def  __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()
  class CPU:
    def processing(self):
      print("Processing data....")
  class RAM:
    def store(self):
      print("Storing data....")
      
computer = Computer()
computer.cpu.processing()
computer.ram.store()

myarray = [7, 4, 28, 56, 1, 4]
minvalue = myarray[0]

for i in myarray:
  if i < minvalue:
    minvalue = i
print(f"lowest value for {myarray} is :", minvalue)


# stack with python list
class Stack:
  def __init__(self):
    self.stack = []
  def push(self, element):
    self.stack.append(element)
  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()
  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]
  def isEmpty(self):
    return len(self.stack) == 0
  def size(self):
    return len(self.stack)
  
mystack = Stack()
mystack.push("A")
mystack.push("B")
mystack.push("C")

print("stack:", mystack.stack)
print("Pop:", mystack.pop())
print("stack after pop:", mystack.stack)
print("Peek:", mystack.peek())
print("Is Empty:", mystack.isEmpty())
print("size:", mystack.size())


# stack with linked lists(node)
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
class Stack:
  def __init__(self):
    self.head = None
    self.size = 0
  def push(self, value):
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1
  def pop(self):
    if self.isEmpty():
      return "stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value
  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.value
  def isEmpty(self):
    return self.size == 0
  def stacksize(self):
    return self.size
  def traverseandprint(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.value, end=" -> ")
      currentNode = currentNode.next
    print()

mystack = Stack()
mystack.push("A")
mystack.push("B")
mystack.push("C")

print("LinkedList:", end="")
mystack.traverseandprint()
print("Peek:", mystack.peek())
print("Pop:", mystack.pop())
print("LinkedList after Pop:", end="")
mystack.traverseandprint()
print("isEmpty:", mystack.isEmpty())
print("Size:", mystack.stacksize())

# Queues using python list
queue = []

queue.append("A")
queue.append("B")
queue.append("C")
print("Queue: ", queue)

frontElement = queue[0]
print("Peek :", frontElement)

poppedElement = queue.pop(0)
print("Dequeue :", poppedElement)

print("Queue after Dequeue: ", queue)

isEmpty = not bool(queue)
print("Is empty: ", isEmpty)

print("Size: ", len(queue))

class Queue:
  def __init__ (self):
    self.queue = []
  def enqueue(self, element):
    self.queue.append(element)
  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]
  def isEmpty(self):
    return len(self.queue) == 0
  def size(self):
    return len(self.queue)
myQueue = Queue()
myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("queue after Dequeue:", myQueue.queue)
print("Is empty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())

# Queue using python linked lists
class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None
class Queue:
  def __init__ (self):
    self.front = None
    self.reer = None
    self.length = 0
  def enqueue(self, element):
    new_node = Node(element)
    if self.reer is None:
      self.front = self.rear = new_node
      self.length += 1
      return
    self.rear.next = new_node
    self.rear = new_node
    self.length += 1
  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.length -= 1
    if self.front is None:
      self.rear = None
    return temp.data
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    self.front.data
  def isEmpty(self):
    return self.length == 0
  def size(self):
    return self.length
  def printqueue(self):
    temp = self.front
    while temp:
      print(temp.data, end=" -> ")
      temp = temp.next
    print()
    
myqueue2 = Queue()
myqueue2.enqueue("A")
myqueue2.enqueue("B")
myqueue2.enqueue("C")

print("queue: ", end="")
myqueue2.printqueue()
print("Peek: ", myqueue2.peek())
print("Dequeue: ", myqueue2.dequeue())
print("Queue after dequeue: ", end="")
print("Is empty: ", myqueue2.isEmpty())
print("size: ", myqueue2.size())

class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None
def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")
  

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)

class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None

def findMinValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findMinValue(node1))

class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None
def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")
def deleteSpacificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next
  
  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next
  if currentNode.next is None:
    return head
  
  currentNode.next = currentNode.next.next
  
  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpacificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)

class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None
def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")
def insertNodeAtPosition(head, newNode, Position):
  if Position == 1:
    newNode.next = head
    return newNode
  
  currentNode = head
  for _ in range(Position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next
  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)

my_list = [None, None, None, None, None, None, None, None, None, None]
my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)
  return sum_of_chars % 10

def add(name):
  index = hash_function(name)
  my_list[index].append(name)

def contains(name):
  index = hash_function(name)
  return my_list[index] == name
  
add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list)
print("'Pete' is in the index:", contains("Pete"))

# A pre-order traversal Binary Trees
# class TreeNode:
#   def __init__ (self, data):
#     self.data = data
#     self.left = None
#     self.right = None

# def preOrderTranversal(node):
#   if node is None:
#     return
#   print(node.data, end=", ")
#   preOrderTranversal(node.left)
#   preOrderTranversal(node.right)

# root = TreeNode("R")
# nodeA = TreeNode("A")
# nodeB = TreeNode("B")
# nodeC = TreeNode("C")
# nodeD = TreeNode("D")
# nodeE = TreeNode("E")
# nodeF = TreeNode("F")
# nodeG = TreeNode("G")

# root.left = nodeA
# root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

# nodeB.left = nodeE
# nodeB.right = nodeF

# nodeF.left = nodeG

# preOrderTranversal(root)


# # An In-order Traversa Binary Trees
# class TreeNode:
#   def __init__ (self, data):
#     self.data = data
#     self.left = None
#     self.right = None

# def inOrderTranversal(node):
#   if node is None:
#     return
#   inOrderTranversal(node.left)
#   print(node.data, end=", ")
#   inOrderTranversal(node.right)

# root = TreeNode("R")
# nodeA = TreeNode("A")
# nodeB = TreeNode("B")
# nodeC = TreeNode("C")
# nodeD = TreeNode("D")
# nodeE = TreeNode("E")
# nodeF = TreeNode("F")
# nodeG = TreeNode("G")

# root.left = nodeA
# root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

# nodeB.left = nodeE
# nodeB.right = nodeF

# nodeF.left = nodeG

# inOrderTranversal(root)


# An Post-order Traversa Binary Trees
# class TreeNode:
#   def __init__ (self, data):
#     self.data = data
#     self.left = None
#     self.right = None

# def inOrderTranversal(node):
#   if node is None:
#     return
#   inOrderTranversal(node.left)
#   inOrderTranversal(node.right)
#   print(node.data, end=", ")
  

# root = TreeNode("R")
# nodeA = TreeNode("A")
# nodeB = TreeNode("B")
# nodeC = TreeNode("C")
# nodeD = TreeNode("D")
# nodeE = TreeNode("E")
# nodeF = TreeNode("F")
# nodeG = TreeNode("G")

# root.left = nodeA
# root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

# nodeB.left = nodeE
# nodeB.right = nodeF

# nodeF.left = nodeG

# inOrderTranversal(root)
# class TreeNode:
#   def __init__ (self, data):
#     self.data = data
#     self.left = None
#     self.right = None
# def inOrderTraversal(node):
#     if node is None:
#       return
#     inOrderTraversal(node.left)
#     print(node.data, end=",")
#     inOrderTraversal(node.right)
    
# root = TreeNode(13)
# node7 = TreeNode(7)
# node15 = TreeNode(15)
# node3 = TreeNode(3)
# node8 = TreeNode(8)
# node14 = TreeNode(14)
# node19 = TreeNode(19)
# node18 = TreeNode(18)

# root.left = node7
# root.right = node15

# node7.left = node3
# node7.right = node8

# node15.left = node14
# node15.right = node19

# node19.left = node18

# inOrderTraversal(root)


# Search the Tree for the value "13" BST
# class TreeNode:
#   def __init__ (self, data):
#     self.data = data
#     self.left = None
#     self.right = None
# def inOrderTraversal(node):
#     if node is None:
#       return
#     inOrderTraversal(node.left)
#     print(node.data, end=",")
#     inOrderTraversal(node.right)
# def search(node, target):
#   if node is None:
#     return None
#   elif node.data == target:
#     return node
#   elif target < node.data:
#     return search(node.left, target)
#   else:
#     return search(node.right, target)
  
# root = TreeNode(13)
# node7 = TreeNode(7)
# node15 = TreeNode(15)
# node3 = TreeNode(3)
# node8 = TreeNode(8)
# node14 = TreeNode(14)
# node19 = TreeNode(19)
# node18 = TreeNode(18)

# root.left = node7
# root.right = node15

# node7.left = node3
# node7.right = node8

# node15.left = node14
# node15.right = node19

# node19.left = node18

# result = search(root, 1)
# if result:
#   print(f"Found the node with the value: {result.data}")
# else:
#   print("Value not found in the BTS")
  
# Inserting a node in a BST:
class TreeNode:
  def __init__ (self, data):
    self.data = data
    self.left = None
    self.right = None

def insert(node, data):
  if node is None:
    return TreeNode(data)
  else:
    if data < node.data:
      node.left = insert(node.left, data)
    elif data > node.data:
      node.right = insert(node.right, data)
  return node
def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=",")
  inOrderTraversal(node.right)
  
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

result = insert(root, 10)
inOrderTraversal(root)

# Find the lowest value in a BST subtree
class TreeNode:
  def __init__ (self, data):
    self.data = data
    self.left = None
    self.right = None

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=",")
  inOrderTraversal(node.right)

def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

inOrderTraversal(root)
print("\nLowest value:", minValueNode(root).data)

# Delete a Node in a BST
class TreeNode:
  def __init__ (self, data):
    self.data = data
    self.left = None
    self.right = None

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=",")
  inOrderTraversal(node.right)

def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def delete(node, data):
  if not node:
    return None
  
  if data < node.data:
    node.left = delete(node.left, data)
  elif data > node.data:
    node.right = delete(node.right, data)
  else:
    # Node with only one child or no child
    if not node.left:
      temp = node.right
      node = None
      return temp
    elif not node.right:
      temp = node.left
      node = None
      return temp
    
    # Node with two children, get the in-order successor
    node.data = minValueNode(node.right).data
    node.right = delete(node.right, node.data)
  return node
    

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Traverse
inOrderTraversal(root)

# Delete node 15
delete(root, 15)

# Traverse
print()
inOrderTraversal(root)

# # Implement AVL Tree in Python:
# class TreeNode:
#   def __init__ (self, data):
#     self.data = data
#     self.left = None
#     self.right = None
#     self.height = 1
# def getHeight(node):
#   if not node:
#     return 0
#   return node.height
# def getBalance(node):
#   if not node:
#     return 0
#   return getHeight(node.left) - getHeight(node.right)
# def rightRotate(y):
#   print("Rotate right on node", y.data)
#   x = y.left
#   T2 = x.right
#   x.right = y
#   y.left = T2
#   y.height = 1 + max(getHeight(y.left), getHeight(y.right))
#   x.height = 1 + max(getHeight(x.left), getHeight(x.right))
#   return x

# def leftRotate(x):
#   print("Rotate left on node", x.data)
#   y = x.right
#   T2 = y.left
#   y.height = x
#   x.right = T2
#   x.height = 1 + max(getHeight(x.left), getHeight(x.right))
#   y.height = 1 + max(getHeight(y.left), getHeight(y.right))
#   return y
# def insert(node, data):
#   if not node:
#     return TreeNode(data)
  
#   if data < node.data:
#     node.left = insert(node.left, data)
#   elif data > node.data:
#     node.right = insert(node.right, data)
    
# # Update the balance factor and balance the tree
#   node.height = 1 + max(getHeight(node.left), getHeight(node.right))
#   balance = getBalance(node)
  
#   # Balancing the tree
#   # Left Left
#   if balance > 1 and getBalance(node.left) >= 0:
#     return rightRotate(node)
  
#   # Left Right
#   if balance > 1 and getBalance(node.left) <= 0:
#     node.left = leftRotate(node.left)
#     return rightRotate(node)
  
#   # Right Right
#   if balance < -1 and getBalance(node.right) <= 0:
#     return leftRotate(node)
  
#   # Right Left
#   if balance < -1 and getBalance(node.right) > 0:
#     node.right = rightRotate(node.right)
#     return leftRotate(node)
  
#   return node

# def inOrderTraversal(node):
#   if not node:
#     return
#   inOrderTraversal(node.left)
#   print(node.data, end=", ")
#   inOrderTraversal(node.right)
  
# Inserting the letters
root = None
letters = ["C", "B", "E", "A", "D", "H", "G", "F"]
for letter in letters:
  root = insert(root, letter)
inOrderTraversal(root)
  
# AVL Trees Delete Node:
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.height = 1

def getHeight(node):
  if not node:
    return 0
  return node.height

def getBalance(node):
  if not node:
    return 0
  return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
  x = y.left
  T2 = x.right
  x.right = y
  y.left = T2
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  return x

def leftRotate(x):
  y = x.right
  T2 = y.left
  y.left = x
  x.right = T2
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  return y

def insert(node, data):
  if not node:
    return TreeNode(data)

  if data < node.data:
    node.left = insert(node.left, data)
  elif data > node.data:
    node.right = insert(node.right, data)

  # Update the balance factor and balance the tree
  node.height = 1 + max(getHeight(node.left), getHeight(node.right))
  balance = getBalance(node)

  # Balancing the tree
  # Left Left
  if balance > 1 and getBalance(node.left) >= 0:
    return rightRotate(node)

  # Left Right
  if balance > 1 and getBalance(node.left) < 0:
    node.left = leftRotate(node.left)
    return rightRotate(node)

  # Right Right
  if balance < -1 and getBalance(node.right) <= 0:
    return leftRotate(node)

  # Right Left
  if balance < -1 and getBalance(node.right) > 0:
    node.right = rightRotate(node.right)
    return leftRotate(node)

  return node

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)
    
def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def delete(node, data):
  if not node:
    return node

  if data < node.data:
    node.left = delete(node.left, data)
  elif data > node.data:
    node.right = delete(node.right, data)
  else:
    if node.left is None:
      temp = node.right
      node = None
      return temp
    elif node.right is None:
      temp = node.left
      node = None
      return temp

    temp = minValueNode(node.right)
    node.data = temp.data
    node.right = delete(node.right, temp.data)

  if node is None:
    return node

  # Update the balance factor and balance the tree
  node.height = 1 + max(getHeight(node.left), getHeight(node.right))
  balance = getBalance(node)

  # Balancing the tree
  # Left Left
  if balance > 1 and getBalance(node.left) >= 0:
    return rightRotate(node)

  # Left Right
  if balance > 1 and getBalance(node.left) < 0:
    node.left = leftRotate(node.left)
    return rightRotate(node)

  # Right Right
  if balance < -1 and getBalance(node.right) <= 0:
    return leftRotate(node)

  # Right Left
  if balance < -1 and getBalance(node.right) > 0:
    node.right = rightRotate(node.right)
    return leftRotate(node)

  return node

# Inserting the letters
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
  root = insert(root, letter)

inOrderTraversal(root)
print('\nDeleting A')
root = delete(root,'A')
inOrderTraversal(root)

mylist = [3, 8 ,7 ,1, 2, 9]

if 3 in mylist:
  print("\nFound!")
else:
  print("\nNot found!")

def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -i

mylist = [9, 5, 3, 1, 7, 2, 1, 4, 6]
x = 5

result = linearSearch(mylist, x)
if result != -i:
  print("Found at index", result)
else:
  print("Not found")

def binarySearch(arr, targetVal):
  left = 0 
  right = len(arr) - 1
  
  while left <= right:
    mid = (left + right) // 2
    
    print("Checking index:", mid, "value:", arr[mid])
    
    if arr[mid] == targetVal:
      return mid
    
    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid -1
  return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 88]
x = 11

result = binarySearch(mylist, x)

if result != -1:
  print("\nFound at index", result)
else:
  print("\nnot found")

# Bubble sort
mylist = [64, 70, 46, 12, 4, 6, 22, 100]
n = len(mylist)
for i in range(n-1):
  swapped = False
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
      swapped = True
  if not swapped:
    break
  
print(mylist)

# Selection sort
mylist = [67, 89, 32, 5, 65, 12, 8, 43]

n = len(mylist)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
    if mylist[j] < mylist[min_index]:
      min_index = j
  mylist[i], mylist[min_index] = mylist[min_index], mylist[i] 
print(mylist)

# Insertion sort
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1, n):
  insert_index = i
  current_value = mylist[i]
  for j in range(i-1, -1, -1):
    if mylist[j] > current_value:
      mylist[j+1] = mylist[j]
      insert_index = j
    else:
      break
  mylist[insert_index] = current_value
print(mylist)

# Quick Sort
def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  
  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
      
  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1
    
  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)
mylist = [64, 34, 25, 5, 22, 3000, 11, 90, 12]
quicksort(mylist)
print(mylist)

# Counting Sort algorithm
def countingSort(arr):
  max_val = max(arr)
  count = [0] * (max_val + 1)
  
  while len(arr) > 0:
    num = arr.pop(0)
    count[num] += 1
    
  for i in range(len(count)):
    while count[i] > 0:
      arr.append(i)
      count[i] -= 1
  return arr
mylist = [4, 2, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
mysortedlist = countingSort(mylist)
print(mysortedlist)

# Radix Sort algorithm
mylist = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", mylist)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(mylist)
exp = 1

while maxVal // exp > 0:
  while len(mylist) > 0:
    val = mylist.pop()
    radixIndex = (val // exp) % 10
    radixArray[radixIndex].append(val)
  for bucket in radixArray:
    while len(bucket) > 0:
      val = bucket.pop()
      mylist.append(val)
  exp *= 10
print(mylist)


# Radix Sort algorithm that uses Bubble Sort
def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i -1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
def radixsortwithBubbleSort(arr):
  max_val = max(arr)
  exp = 1
  
  while max_val // exp > 0:
    radixList = [[], [], [], [], [], [], [], [], [], []]
    
    for num in arr:
      radixIndex = (num // exp) % 10
      radixList[radixIndex].append(num)
      
    for bucket in radixList:
      bubbleSort(bucket)
      
    i = 0
    for bucket in radixList:
      for num in bucket:
        arr[i] = num
        i += 1
    exp *= 10
mylist = [170, 45, 75, 90, 802, 24, 2, 66]
radixsortwithBubbleSort(mylist)
print(mylist)

# Merge Sort algorithm with recursion
def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]
  
  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)
  
  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result.extend(left[i:])
  result.extend(right[j:])
  
  return result
mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)

# Merge sort without recursion
def merge(left, right):
  result = []
  i = j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result.extend(left[i:])
  result.extend(right[j:])
  return result

def mergeSort(arr):
  step = 1 # start with sun-array of length 1
  length = len(arr)
  
  while step < length:
    for i in range(0, length, 2 * step):
      left = arr[i:i + step]
      right = arr[i + step:i + 2 * step]
      
      merged = merge(left, right)
      
      # Place the merged array back into the original
      for j, val in enumerate(merged):
        arr[i + j] = val
    step *= 2 # Double the sub-array length for the next itaraction
  return arr
mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print(mysortedlist)

x = [9, 1, 5, 0, 3, 4, 2, -9, 5987]
y = max(x)
minVal = x[0]
for i in x:
  if i < minVal:
    minVal = i
print("Minimum value is:", minVal, "maximum value is:", y)

# Stack data structure
stack = []

# push
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")
print("Stack:", stack)

# peek
topelement = stack[-1]
print("Peek:", topelement)

# pop
poppedelemnt = stack.pop()
print("Popped elemnt:", poppedelemnt)
print("Stack after pop:", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty:", isEmpty)

# size
print("Size:", len(stack))

# Stack using List/Array
class Stack:
  def __init__ (self):
    self.stack = []
  def push(self, element):
    self.stack.append(element)
  def peek(self):
    if self.isEmpty():
      return "stack is empty"
    return self.stack[-1]
  def pop(self):
    if self.isEmpty():
      return "stack is empty"
    return self.stack.pop()
  def isEmpty(self):
    return len(self.stack) == 0
  def size(self):
    return len(self.stack)
mystack = Stack()
mystack.push("E")
mystack.push("F")
mystack.push("G")
mystack.push("H")

print("Stack:", mystack.stack)
print("Pop:", mystack.pop())
print("Stack after pop:", mystack.stack)
print("Peek:", mystack.peek())
print("IsEmpty:", mystack.isEmpty())
print("size:", mystack.size())
    
# stack using linked list
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
class Stack:
  def __init__(self):
    self.head = None
    self.size = 0
  def push(self, value):
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1
  def pop(self):
    if self.isEmpty():
      return "stack is empty"
    poppedNode = self.head
    self.head = self.head.next
    self.size -= 1
    return poppedNode.value
  def peek(self):
    if self.isEmpty():
      return "stack is empty"
    return self.head.value
  def isEmpty(self):
    return self.size == 0
  def getsize(self):
    return self.size
  def traverseandPrint(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.value, end=" -> ")
      currentNode = currentNode.next
    print()
mystack = Stack()
mystack.push("I")
mystack.push("J")
mystack.push("K")
mystack.push("L")

print("Linkedlist:", end="")
mystack.traverseandPrint()
print("Peek:", mystack.peek())
print("Pop:", mystack.pop())
print("Linkedlist after pop:", end="")
mystack.traverseandPrint()
print("IsEmpty:", mystack.isEmpty())
print("size:", mystack.getsize())

# python list as a queue  
queue = []

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue", queue)

# Peek
frontElement = queue[0]
print("Peek", frontElement)

# Dequeue
poppedElement = queue.pop(0)
print("Dequeue", poppedElement)

# isEmpty
isEmpty = not bool(queue)
print("Is empty", isEmpty)

# Size
print("Size", len(queue))

# Python class as a queue
class Queue:
  def __init__(self):
    self.queue = []
  def enqueue(self, element):
    self.queue.append(element)
  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]
  def isEmpty(self):
    return len(self.queue) == 0
  def getsize(self):
    return len(self.queue)

# Create queue
myQueue = Queue()

myQueue.enqueue("D")
myQueue.enqueue("E")
myQueue.enqueue("F")

print("Queue", myQueue.queue)
print("Peek", myQueue.peek())
print("Dequeue", myQueue.dequeue())
print("Queue after Dequeue", myQueue.queue)
print("Is empty", myQueue.isEmpty())
print("Size", myQueue.getsize())

# Creating a Queue using a Linked List
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
class Queue:
  def __init__(self):
    self.front = None
    self.rear = None
    self.length = 0
  def enqueue(self, element):
    new_node = Node(element)
    if self.rear is None:
      self.front = self.rear = new_node
      self.length += 1
      return
    self.rear.next = new_node
    self.rear = new_node
    self.length += 1
  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.front
    self.front = temp.next
    self.length -= 1
    if self.front is None:
      self.rear = None
    return temp.data
  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.front.data
  def isEmpty(self):
    return self.length == 0
  def getSize(self):
    return self.length
  def printQueue(self):
    temp = self.front
    while temp:
      print(temp.data, end=" - > ")
      temp = temp.next
    print()
# Create a queue
myQueue = Queue()

myQueue.enqueue("G")
myQueue.enqueue("H")
myQueue.enqueue("I")

print("Queue ", end="")
myQueue.printQueue()
print("Peek ", myQueue.peek())
print("Dequeue ", myQueue.dequeue())
print("Queue after dequeue ", end="")
myQueue.printQueue()
print("Is empty ", myQueue.isEmpty())
print("Queue size is ", myQueue.getSize())

# Linked list
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
def tranverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")
def findMinValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

tranverseAndPrint(node1)
print("The lowest value in the linked list is:", findMinValue(node1))


f = open("demofile.txt")
print(f.readline())
f.close()

with open("demofile.txt") as f:
  print(f.read())

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

with open("demofile.txt") as f:
  print(f.read())

f = open("myfile.txt", "w")
f.close()

import os
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

if os.path.exists("test"):
  os.rmdir("test")
else:
  print("Folder does not exist")


# Draw a line in a diagram from position (0,0) to position (6,250):
# import matplotlib
# matplotlib.use('TkAgg')


import num as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0:2, 0:2, 1:2])


# Deleting a specific node in a singly linked list in Python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
def tranverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")
def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next
  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next
  if currentNode.next is None:
    return head
  currentNode.next = currentNode.next.next
  return head
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
tranverseAndPrint(node1)

# Delete node4
deleteSpecificNode(node1, node4)

print("\nAftee deletion:")
tranverseAndPrint(node1)

# Inserting a node in a singly linked list in Python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def insertNodeAtPosition(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode
  currentNode = head
  for _ in range(position - 2):
    if currentNode.next is None:
      break
    currentNode = currentNode.next
  newNode.next = currentNode.next
  currentNode.next = newNode
  return head
node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseAndPrint(node1)


newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)

arr = np.array([1, 2, 3, 4])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)


# Create a Hash Function that sums the Unicode numbers of each character and return a number between 0 and 9

# 10 empty buckets
my_list = [[], [], [], [], [], [], [], [], [], []]

# hash function
def hash_function(name):
  sum_of_chars = 0
  for char in name:
    sum_of_chars += ord(char)
  return sum_of_chars % 10
   
# add name and phone function 
def add(name, phone):
  index = hash_function(name)
  my_list[index].append((name, phone))
# check function if name exists
def contain(name):
  index = hash_function(name)
  for i in my_list[index]:
    if i[0] == name:
      return True
  return False
# delete a name
def delete(name):
  index = hash_function(name)
  for i in my_list[index]:
   if i[0] == name:
    my_list[index].remove(i)
    break
# find phone number by name
def get_phone(name):
  index = hash_function(name)
  for i in my_list[index]:
    if i[0] == name:
      return i[1]
  return None
add('KEN', '0712345678')
add('Pete', '0723456789')
add('Jones', '0734567890')
add('Lisa', '0745678901')
add('Siri', '0756789012')
add('Bob', '0767890123')
add('Stuart', '0778901234')

print(my_list)
delete('KEN')
print(my_list)
print("'Pete' is in the Hash Table:", contain('Pete'))
print("'Jones' phone:", get_phone('Jones'))


# # Pre-Order Traversal of Binary Trees
# class TreeNode:
#   def __init__(self, data):
#     self.data = data
#     self.left = None
#     self.right = None
# def preOrderTraversal(node):
#   if node is None:
#     return
#   print(node.data, end=", ")
#   preOrderTraversal(node.left)
#   preOrderTraversal(node.right)
  
# root = TreeNode("R")
# nodeA = TreeNode("A")
# nodeB = TreeNode("B")
# nodeC = TreeNode("C")
# nodeD = TreeNode("D")
# nodeE = TreeNode("E")
# nodeF = TreeNode("F")
# nodeG = TreeNode("G")

# root.left = nodeA
# root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

# nodeB.left = nodeE
# nodeB.right = nodeF

# nodeF.left = nodeG

# preOrderTraversal(root)



# In-Order Traversal of Binary Trees
# class TreeNode:
#   def __init__(self, data):
#     self.data = data
#     self.left = None
#     self.right = None
# def preOrderTraversal(node):
#   if node is None:
#     return
#   preOrderTraversal(node.left)
#   print(node.data, end=", ")
#   preOrderTraversal(node.right)
  
# root = TreeNode("R")
# nodeA = TreeNode("A")
# nodeB = TreeNode("B")
# nodeC = TreeNode("C")
# nodeD = TreeNode("D")
# nodeE = TreeNode("E")
# nodeF = TreeNode("F")
# nodeG = TreeNode("G")

# root.left = nodeA
# root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

# nodeB.left = nodeE
# nodeB.right = nodeF

# nodeF.left = nodeG

# preOrderTraversal(root)


# Post-Order Traversal of Binary Trees
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
def preOrderTraversal(node):
  if node is None:
    return
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)
  print(node.data, end=", ")
  
root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

preOrderTraversal(root)
print()

# R A C D B E F G Pre-order Tranverse = Root → Left → Right 
# C A D R E B G F In-order traversal (Left → Root → Right)
# C D A E G F B R Post-order traversal (Left → Right → Root)


# Traverse using Breadth First Search (BFS)
from collections import deque

def bfsTraversal(root):
  if root is None:
    return
  
  queue = deque([root])
  
  while queue:
    current = queue.popleft()
    print(current.data, end=" -> ")
    
    if current.left is not None:
      queue.append(current.left)
      
    if current.right is not None:
      queue.append(current.right)
      
root = TreeNode("R")
nodeA = TreeNode("H")
nodeB = TreeNode("I")
nodeC = TreeNode("J")
nodeD = TreeNode("K")
nodeE = TreeNode("L")
nodeF = TreeNode("M")
nodeG = TreeNode("N")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

bfsTraversal(root)
print()


# Traversal of a Binary Search Tree in Python
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=" -> ")
  inOrderTraversal(node.right)
def search(node, target):
  if node is None:
    return None
  elif node.data == target:
    return node
  elif target < node.data:
    return search(node.left, target)
  else:
    return search(node.right, target)
def insert(node, data):
  if node is None:
    return TreeNode(data)
  else:
    if data < node.data:
      node.left = insert(node.left, data)
    elif data > node.data:
      node.right = insert(node.right, data)
  return node
def minValue(node):
  current = node
  while current.left is not None:
    current = current.left
  return current
def delete(node, data):
  if not node:
    return None
  if data < node.data:
    node.left = delete(node.left, data)
  elif data > node.data:
    node.right = delete(node.right, data)
  else:
    # Node with only one child or no child
    if not node.left:
      temp = node.right
      node = None
      return temp
    elif not node.right:
      temp = node.left
      node = None
      return temp
    
    # Node with two children, get the in-order successor
    node.data = minValue(node.right).data  # Copy the in-order successor's content to this node
    node.right = delete(node.right, node.data) # Delete the in-order successor
  return node
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18
  
inOrderTraversal(root)
print()

# Search for a value
result = search(root, 15)
if result:
  print(f"Found the node with value: {result.data}")
else:
  print("Value not found in the BTS.")

# Inserting new value into the BST
insert(root, 10)
inOrderTraversal(root)
print("\nLowest value:", minValue(root).data)
delete(root, 15)
inOrderTraversal(root)

# Implement AVL Tree
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.height = 1
    
def getHeight(node):
  if not node:
    return 0
  return node.height
def getBalance(node):
  if not node:
    return 0
  return getHeight(node.left) - getHeight(node.right)
def rightRotate(y):
  print("Rotate right on node", y.data)
  x = y.left
  T2 = x.right
  x.right = y
  y.left = T2
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  return x
def leftRotate(x):
  print("Rotate left on node", x.data)
  y = x.right
  T2 = y.left
  y.left = x
  x.right = T2
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  return y
def insert(node, data):
  if not node:
    return TreeNode(data)
  if data < node.data:
    node.left = insert(node.left, data)
  elif data > node.data:
    node.right = insert(node.right, data)
  # Update the balance factor and balance the tree
  node.height = 1 + max(getHeight(node.left), getHeight(node.right))
  balance = getBalance(node)
  # Balancing the tree
  # Left Left
  if balance > 1 and getBalance(node.left) >= 0:
    return rightRotate(node)
  # Left Right
  if balance > 1 and getBalance(node.left) < 0:
    node.left = leftRotate(node.left)
    return rightRotate(node)

  # Right Right
  if balance < -1 and getBalance(node.right) <= 0:
    return leftRotate(node)

  # Right Left
  if balance < -1 and getBalance(node.right) > 0:
    node.right = rightRotate(node.right)
    return leftRotate(node)

  return node

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

# Inserting nodes
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
  root = insert(root, letter)

inOrderTraversal(root)
  
  




