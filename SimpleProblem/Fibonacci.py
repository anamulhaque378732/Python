# fibonacci series


previous = 0
next = 1

for i in range(10):
    print(previous, end=" ")
    result = previous + next
    previous = next
    next = result
