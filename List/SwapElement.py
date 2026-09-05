# swap 2 element

numList = [18, 2, 5, 8, 7, 6, 4, 9, 11]
temp = numList[0]
numList[0] = numList[-1]  # a[len(numList)-1]

numList[-1] = temp
# print(numList)
