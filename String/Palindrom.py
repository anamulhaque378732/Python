# palindrom sting checking


a = input("enter string")
if a == a[::-1]:
    print("Palindrom")
else:
    print("Not palimdrom")

# string reversing


inp = "I love python"
inp = inp.split(" ")
# print(inp)

result = ""
for i in inp:
    result += i[::-1] + " "
print(result)
