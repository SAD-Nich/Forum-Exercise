#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Write a Python program which accepts the radius of a circle from the user and compute the area
r= float(input("radius:"))
area= 3.14*r**2
print(f"the area of the cirlce is {area}")


# In[2]:


#2 Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
fn= input("First Name:")
ln= input("Last Name:")
print(ln, fn)


# In[5]:


#3 Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","Black"]
print(f"The first color from the list is {color_list[0]}")
print(f"The last color from the list is {color_list[-1]}")


# In[6]:


#4 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n= int(input("Give n a value:"))
print(f"The value of n is {n+n**2+n**3}")


# In[7]:


#5 Write a Python program to get the volume of a sphere with radius 6.
r = 6
volume = (4/3*3.14*r**3)
print("The radius of the circle is 6")
print(f"The volume of the circle is {int(volume)} or {float(volume)}")


# In[8]:


#6 Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
num = int(input("Input any random number:"))
if num < 17:
    print(17-num)
else:
    print((num-17)*2)


# In[9]:


#7 Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
num1 = float(input("Input a number:"))
num2 = float(input("Input a second number:"))
num3 = float(input("Input a third number:"))
if num1 == num2 == num3:
    print(f"The result is {int(num1 + num2 +num3)*3}")
else:
    print(f"The result is {int(num1+num2+num3)}")


# In[10]:


#8 Write a Python program to find wheter a given number (accept from the user) is even or odd, print out an appropriate message to the user.
num = int(input("Input any number:"))
if num % 2 == 0:
    print("This number is an even number")
else:
    print("This number is an odd number")


# In[12]:


#9 Write a Python program to test whether a letter is a vowel or not
characters = input("Type in any letter:")
if characters in ('a', 'e', 'i', 'o', 'u'):
    print("This letter is a vowel")
elif characters in ('A', 'E', 'I', 'O', 'U'):
    print("This letter is a vowel")
else:
    print("This letter is a consonant")


# In[14]:


#10 Write a Python program to check whether a specified value is contained in a group of values.
stuff = ("Tea","Coffee","Ice","Diamonds","Rocks","Fishes","Stones","Stories")
item = input("What do you want?:")
item = item.capitalize()
if item in stuff:
    print("It's available")
else:
    print("It's not available")


# In[17]:


#11 Write a Python program to create a histogram from a given list of integers.
import matplotlib.pyplot as plt

x = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10]
plt.hist(x, bins=4, edgecolor='black')


# In[18]:


#12 Write a Python program to print all even numbers from a given numbers list in the same order.
numbers = [
 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
 958, 743, 527
    ]
for n in numbers:
    if n % 2 == 0:
        print(n, end=". ")


# In[19]:


#13 Write a Python program that will accept the base and height of a triangle and compute the area.
base = float(input("What is the base of the triangle?:"))
height = float(input("What is the height of the triangle?:"))
total = float((base*height)/2)
print(f"The value of the triangle's area is {int(total)}")


# In[20]:


#14 Write a Python program to get the least common multiple (LCM) of two positive integers.
num1 = float(input("Put in any number: "))
num2 = float(input("Put in a second number: "))
if num1 > num2:
    greater = num1
else:
    greater = num2
while (True):
    if ((greater % num1 == 0) and (greater % num2 == 0)):
        lcm = greater
        break
    greater += 0.5
print(f"The L.C.M is {int(lcm)}")


# In[21]:


#15 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
num1 = float(input("Input a number:"))
num2 = float(input("Input a second number:"))
num3 = float(input("Input a third number:"))
if num1 == num2 or num1 == num3 or num2 == num3:
    print("The result is 0 for whatever reason.")
else:
    print(f"The result is {int(num1+num2+num3)}")


# In[22]:


#16 Write a Python program to solve (x + y) * (x + y)
x= float(input("Give x a number:"))
y= float(input("Give y a number:"))
z= ((x+y)**2)
print(f"The result is {int(z)} or {float(z)}")


# In[23]:


#17 Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
amt = float(input("Amount:"))
int = float(input("Rate of Interest:"))
years = float(input("For how many years?:"))
FV = amt*((1+(0.01*int)) ** years)
print(f"Expected value in the future is {round(FV,2)}")


# In[28]:


#18 Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
x1 = float(input("Point for x1:"))
y1 = float(input("Point for y1:"))
x2 = float(input("Point for x2:"))
y2 = float(input("Point for y2:"))
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}) is {round(distance)}")


# In[33]:


#19 Write a python program to sum of the first n positive integers.
c= float(input("Give a number:"))
sum = (c * (c + 1)) / 2
print("The sum of the first", c ,"positive integers is", round(sum))


# In[43]:


#20 Write a Python program to convert height (in feet and inches) to centimeters
ft= float(input("How tall are you in feet:"))
In= float(input("and inches?:"))
eval= (ft*12*2.54)+(In*2.54)
print("Your height in centimeters is", round(eval,2),"cm")


# In[47]:


#21 Write a Python program to calculate the hypotenuse of a right angled triangle.
side1 = float(input("Length of one side:"))
side2 = float(input("Length of other side:"))
cal= ((side1**2+side2**2)**0.5)
print("The hypotenuse of the triangle is", round(cal))


# In[48]:


#22 Write a Python program to calculate body mass index.
h = float(input("How tall are you in meters?"))
w = float(input("How heavy are you in kilograms?:"))
print("Your BMI is", round(w / (h**2), 2))


# In[55]:


#23 Write a Python program to calculate midpoints of a line
x1=float(input("x1?:"))
y1=float(input("y1?:"))
x2=float(input("x2?:"))
y2=float(input("y2?:"))
mid=((x1+x2)/2,(y1+y2)/2)
print(f"The midpoint of {(x1,y1)} and {(x2,y2)} is {(mid)}")


# In[59]:


#24 
t=[]
for i in range(2000,3201):
    if(i%7==0)and(i%5!=0):
        t.append(str(i))
print(*t, sep=", ",end=".")

