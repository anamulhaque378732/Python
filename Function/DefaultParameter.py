# default parameter
def greetingFunction(name="Rohim", age=26):
    print(f"Hello {name}. You are {age} years old")


# greetingFunction("Anamul", 36)


# greetingFunction(age=25, name="Anamul")


# print vs return

# print update od modify possible nah


def sum(a, b):
    print(a + b)


# sum(5, 6)


def sumWithReturn(a, b):
    return a + b


result = sumWithReturn(5, 65) * 5
result += 6

print(result)

# function with no argument and no return value in python


def gre():
    print("Anamul")


# function with no argument and no return value in python


def sum():
    a = input()
    b = input()
    print(a + b)


# sum()

# function with no argument  but return value in python


def sub():
    a = 6
    b = 65
    return b - a


# print(sub())

# function with  argument and no return value in python


def mul(num1, num2):
    print(num1 * num2)


# mul(4, 5)

# function with  argument and  return value in python


def devide(a, b):
    return a / b


print(devide(4, 5))
