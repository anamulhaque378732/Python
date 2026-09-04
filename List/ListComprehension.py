# list comprehension

# [Expression for item in list]

# example - 1
listNumber = [10, 20, 30, 40, 50, 60, 70, 80, 90]  # main list : add 5 bye all element


newList = [i + 5 for i in listNumber]
newList1 = [i - 5 for i in listNumber]
newList2 = [i * 5 for i in listNumber]
newList3 = [i / 5 for i in listNumber]
# print(newList, newList1, newList2, newList3)

# interating through a string in list Comprehension

str1 = "Hello World"
newStr = [i for i in str1]
anotherMethod = list(str1)
# print(newStr, anotherMethod)


# using range() function in list Comprehension


OddNumber = [i for i in range(1, 20, 2)]
evenNumber = [i for i in range(2, 21, 2)]
# anther method
odd = list(range(1, 20, 2))
# print(OddNumber, evenNumber)


# using if with list comprehension


divide5 = []
for i in range(1, 20):
    if i % 5 == 0:
        divide5.append(i)
# print(divide5)


divide3 = [i for i in range(1, 20) if i % 3 == 0]
# print(divide3)


divide5And3 = []
for i in range(1, 20):
    if i % 3 == 0 and i % 5 == 0:
        divide5And3.append(i)
# print(divide5And3)

# nested if with list comprehension

divide3And4 = [i for i in range(1, 30) if i % 3 == 0 and i % 4 == 0]
# print(divide3And4)


listNum = []
for i in range(1, 20):
    if i % 2 == 0:
        listNum.append("Even -->")
    else:
        listNum.append("Odd-->")
# print(listNum)


listNumbers = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 30)]

# print(listNumbers)
