# nested Loop

# for i in range(1,6):
#     for j in range(1,6):
#         print(i*j, end = "  ")
#     print()
"""
# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12  15
# 4  8  12  16  20
#  5  10  15  20  25
"""

# for row in range(8):
#     for col in range(row + 1):
#         print("#", end=" ")
#     print()

"""
# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 
# # # # # # # 
# # # # # # # # 
"""

# assci value

# for row in range(6):
#     for col in range(row + 1):
#         print(chr(97 + row), end=" ")
#     print()


"""
a 
b b 
c c c 
d d d d 
e e e e e 
f f f f f f 
"""

# for row in range(6):
#     for col in range(row + 1):
#         print(chr(65 + row), end=" ")
#     print()

"""
A 
B B 
C C C 
D D D D 
E E E E E 
F F F F F F 
"""


bazar_list = [
    [
        "alu",
        "piyaz",
        "begun",
        "vendi",
    ],
    ["beaf", "Mutton", "chicken"],
    ["jira", "ada", "holud", 12, 23, 2.5],
]


for item in bazar_list:
    for small_item in item:
        print(small_item, end=" ")
    print()
