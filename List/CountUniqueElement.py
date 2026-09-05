# unique element

numList = [1, 22, 22, 3, 5, 5, 6, 9, 5, 9, 47]

uniqueElement = []
conut = 0
for num in numList:
    if num not in uniqueElement:
        conut += 1
        uniqueElement.append(num)

print(uniqueElement, conut)


# given a list extract all element whose frequnecy is greater than k.

numsList = [4, 6, 3, 3, 4, 3, 4, 3, 8, 4]
k = 3

newList = []

for num in numsList:
    freq = numsList.count(num)
    if freq > k and num not in newList:
        newList.append(num)
print(newList)
