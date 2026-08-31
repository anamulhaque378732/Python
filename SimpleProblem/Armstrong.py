# Armstrong number

# method number 1
# a = int(input("Number "))
# num_len = len(str(a))


# temp = a

# sum = 0
# while temp > 0:
#     lst_digit = temp % 10
#     sum = sum + lst_digit**num_len
#     temp //= 10
# if sum == a:
#     print("Armstrong Number")
# else:
#     print("Not Arms strong number")

# mrthod 2


b = input()
number_len = len(b)
total = 0
for i in b:
    total = total + int(i) ** number_len
if int(b) == total:
    print("Armstrong Number")
else:
    print("Not Arms strong number")
