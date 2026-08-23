
# problem 1
length = int (input("Enter Length : "))
breadth = int (input("Enter Breadth : ") )
if length == breadth:
    print("This is square")
else: 
    print(" this is Rectangle")

# problem 2

num1 = 120000
num2 = 200000
num3 = 16000

if num1 >= num2 and num1 >= num3 :
  print(num1 ,"Num - 1 is greater")
elif num2 >= num1 and num2 >= num3 :
  print( num2,  "Num - 2 is Grater")
else: print( num3 , "Num - 3 is greater")

# problem3


nmu4 = 12
if not isinstance( nmu4, int)  :
     print("Give me integer number")
elif nmu4 % 2 == 0 : 
    print("Number is even")
else : print("Number is odd")


# problem 4

year = 1900
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("year is leap year")
else: print("Year not leap year")