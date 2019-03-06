i = 0

while i < 5:
    print(i)
    i += 1


i = 0
while True:
    print(i)
    if i >= 5:
        print("exit")
        break
    i += 1


min_length = 2

# name = input("Please eneter your name:")

# while not (len(name) >= min_length and name.isprintable() and name.isalpha()):
#     name = input("Please eneter your name:")
# print("Hello , {0}".format(name))


while True:
    name = input("Please eneter your name:")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
print("Hello , {0}".format(name))




