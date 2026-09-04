# 2D list comprehension

matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
]

# tranpose matrix conversion
newMatrix = []
# simple way

for row in range(2):  # outer loop
    # print(row)
    b = []
    for col in matrix:  # inner loop
        # print(col)
        b.append(col[row])
    newMatrix.append(b)
# print(newMatrix)


# short way list comprehensoin
result = [[col[row] for col in matrix] for row in range(2)]
print(result)
