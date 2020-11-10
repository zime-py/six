# 1. a smple function
# def fun():
# 	print('hello world')
# fun();

#2.parameter in a function
# def fnn(a,b):
# 	print(a+b);
# fnn(2,2);

# 3.return a function
# def fun(a,b):
# 	return a+b;
# sos=fun(2,2);
# print(sos);

# 4.attributr argumernt/attribute parameter of function
# def fun(*args):
# 	print(args);
# fun(1,2,3,4,5,6,7);
# fun('mahmud','hossin','lamyaa');


# 5. call attribute parameter value by index
# Arbitrary Arguments are often shortened to *args in Python documentations.
# def fun(*args):
# 	print('my mname is' + args[2]); #args[2]
# fun('1','2','lamaa')


# 6.Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
# def fun(name,roll,age):
# 	print('i am '+ name +'my roll'+ roll +'my age is'+ age )
# fun(name='mahmd',roll='12345',age='26')    


# 7. how to parsed interger value by str in keyword Argument
# def fun(name,roll,age):
# 	print('i am '+ name +'my roll'+ roll +'my age is'+ age )
# #fun(name='mahmd',roll=12345,age=26 )  #not work
# fun(name='mahmd',roll=str(12345),age=str(26) ) 


# 8.Arbitrary Keyword Arguments, **kwargs
# def fun(**kwargs):
# 	print(kwargs)
# fun(name='mamud',roll='12345',city='rajshhai')
##########AND######
# def fun(**kwargs):
# 	print('My name is'+kwargs['name']+'my roll'+kwargs['roll']+'my city is'+kwargs['city'])
# fun(name='mamud',roll='12345',city='rajshhai')
#####AND######
# def fun(**kwargs):
# 	print('My name is'+kwargs['name']+'my roll'+kwargs['roll']+'my age is'+kwargs['age'])
# ##fun(name='mamud',roll=12345,age=26) ##NOT WORK ROLL and AGE VALUE
# fun(name='mamud',roll=str(12345),age=str(26))


# 9.a unction has multiple object 
# def fun(name,roll,age):
# 	print('my name is'+name+'my roll is'+roll+'my age is'+age)
# one=fun('mahmud',str(12345),str(25))
# two=fun('hossain',str(6789),str(26))
# ##three=fun('lamyaa',0000,30)    ##this line not work cause not use of stringfy


# 10.Passing a List as an Argument by using for loop
# def fun(foods):
# 	for x in foods:
# 		print(x)
# fruits =['apple','banana',123]
# fun(fruits)
####OR
# def fun(*args):
# 	for x in args:
# 		print(x)
# fun('a','b','c','d','e')
####OR
# def fun(**kwargs):
# 	for x in kwargs:
# 		print(kwars)
# fun(a='apple',b='banana',c='orange')


# 11.lambda function
#Lambda functions can take any number of arguments:
# sos=lambda x:x+2;
# print(sos(2))

# 12.Multiply argument a with argument b and return the result:
# sos=lambda x,y:x+y;
# print(sos(2,5))


#13. create a simple class
# class one:
# 	x='hello';
# print(one)


#14.create an object
# class one:
# 	s='hello';
# x=one()
# print(x.s)


#15.The __init__() Function
#Use the __init__() function to assign values to object properties,  
#or other operations that are necessary to do when the object is being created:
#Note: The __init__() function is called automatically every time the class is being used to create a new object.
# class one:
# 	def __init__(self,name,roll):
# 		self.name=name
# 		self.roll=roll
# x=one('mahmd',123)
# print(x.roll)


#16.Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#The self parameter is a reference to the current instance of the class, 
#and is used to access variables that belong to the class
# class one:
# 	def __init__(self,name,roll):
# 		self.name=name
# 		self.roll=roll
# 	def cool(self):
# 		print(self.name)
# sos=one('mahmud',1234)
# sos.cool();


# 17.The self Parameter, we also use self alter another paramater
# class one:
# 	def __init__(pop,name,age):   #here use pop alter of self
# 		pop.name=name
# 		pop.age=age
# 		print(pop.name)
# sos=one('mahmd',12345)


#18.Modify Object Properties
# class person:
# 	def __init__(self,name,age):
# 		self.name=name
# 		self.age=age
# 	def one(self):
# 		print('my name is '+ self.name)
# 		print('my roll is' +self.age)
# sos=person('mahmud',25)
# sos.age=250
# print(sos.age)


#19.Delete Object Properties
# class person:
# 	def __init__(self,name,age):
# 		self.name=name
# 		self.age=age
# 	def one(self):
# 		print('my name is '+ self.name)
# 		print('my roll is' +self.age)
# sos=person('mahmud',25)
# del sos.age
# print(sos.age)


# 20. Delete Objects
# You can delete objects by using the del keyword:
# class person:
# 	def __init__(self,name,age):
# 		self.name=name
# 		self.age=age
# 	def one(self):
# 		print('my name is '+ self.name)
# 		print('my roll is' +self.age)
# sos=person('mahmud',25)
# del sos
# print(sos)


#21.Python Inheritance
# bellow class two inhereted all property from class one
# class one:
# 	def __init__(self,name,roll):
# 		self.name=name
# 		self.roll=roll
# 		print(self.roll)
# class two(one):
# 	def child(self):
# 		print(self.name)

# sos=two('mahmd',123)
# sos.child()


# 22.Add the __init__() Function in both class
# class person:
# 	def __init__(self,fname,lname):
# 		self.fname=fname
# 		self.lname=lname
# 	def one(self):
# 		print(self.fname, self.lname)
# class student(person):
# 	def __init__(self,fname,lname):
# 		person.__init__(self,fname,lname)
# sos=student('mahmd','hossain')
# sos.one()


#23.Use the super() Function
#Python also has a super() function that will make the 
#child class inherit all the methods and properties from its parent
# class person:
# 	def __init__(self,fname,lname):
# 		self.fname=fname
# 		self.lname=lname
# 	def one(self):
# 		print(self.fname, self.lname)
# class student(person):
# 	def __init__(self,fname,lname):
# 		super().__init__(fname,lname)
# sos=student('mahmd','hossain')
# sos.one()


# 24.add extannally parameter in init 
# class person:
# 	def __init__(self,fname,lname):
# 		self.fname=fname
# 		self.lname=lname
# 	def one(self):
# 		print(self.fname, self.lname)
# class student(person):
# 	def __init__(self,fname,lname):
# 		super().__init__(fname,lname)
# 		self.graduationyear = 2019
# sos=student('mahmd','hossain')
# sos.one()
# print(sos.graduationyear)


#25.Add Methods
# Add a method called welcome to the Student class
# class person:
# 	def __init__(self,name,roll):
# 		self.name=name
# 		self.roll=roll

# 	def one(self):
# 		print(self.name, self.roll)

# class student(person):
# 	def __init__(self,name,roll,age):
# 		super().__init__(name,roll)
# 		self.age=age                     #add a parameter externally

# 	def two(self):                    #add a method externally
# 		print(self.name, self.roll, self.age)

# sos=student('mahmud','1234','25')
# sos.two()


#26.