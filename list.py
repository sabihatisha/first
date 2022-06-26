# food=["pizza","hamburger","hotdog","spagetti"]
# food[0]= "sushi"
# food.append("bhath")
# print(food)
# for x in food:
# print(x)

# 2d list
# dinner=["pizza","hamburger","hotdog","spagetti"]
# drink=["cocacola","sprite","fanta","deo"]
# dessert=["icecrem","tiramisu","payesh"]

# food=[drink,dinner, dessert]
# print(food[0][3])


# set
# utensils={"fork", "spoon","knife"}
# dishes={"plate","deg","glass"}
# for x in utensils:
#   print(x)
# dinner_table= utensils. union(dishes)
# print(dinner_table)
# print(dishes.intersection(utensils))

# dictinary

# Capitals={'usa': 'whasington dc',
#          'india': 'New delhi',
#          'russia': 'moscow',
#         'china': 'bejing'}
# Capitals.update({'germany':'berline'})
# print(Capitals['russia'])
# print(Capitals.get('germany'))
# print(Capitals.keys())
# print(Capitals.values())
# print(Capitals.items())
# Capitals.update({'germany':'berline'})


# Indexing
# name="sabiha jannath Tisha"
# first_name=name[3].upper()
# last_name= name[8:].lower()
# if(name[0].islower()):
#     name= name.capitalize() for only first letter
#     print(name)

# print(first_name)
# print(last_name)

# function
# def hello(name):
#    print("hello "+name)

# hello("Bro")

# def life(future,past,present,age):
#    print("hello "+future+past+present+str(age))

# life("idaho ","leading ","bekar ", 21)


# nested function call
# print(round(abs(float(input("Enter a whole posotive number:")))))


# Scope
# There are two kind of scope global and local
# name= "bro"  #global scope availavle inside and outside function
# def my():
#    name="tisha"  #local scope only available inside of function
#    print(name)
# print(name)
# my()


# def add (num1, num2):
#    sum=num1+num2
#    return sum
# print(add(1,2))

#def add(*args):
#    sum = 0
#    for i in args:
#        sum += i
#    return sum
#print(add(1,2,3,4))

#Amimel="cow"
#items= "moon"
#print("The "+Amimel+" Jumped over the "+items)
#print("The{}jumped over the{}".format("cow","moon"))

#import random
#x= random.randint(1,6)
#print(x)
#mylist=['rock','paper','sesser']
#z=random.choice(mylist)
#print(z)
#cards=[1,2,3,4,5,6,7,8,9]
#random.shuffle(cards)
#print(cards)




