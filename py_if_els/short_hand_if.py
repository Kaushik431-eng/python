# short hand if

a = 20
b = 30

if b > a:
    print("b is grater then b")

a = 100
b = 200

print("A") if a > b else print("B")


# assign value with if else

a = 10
b = 30
bigger = a if a > b else b
print("bigger is", bigger)


# multiple condition in one line

a = 300
b = 300

print("a") if a < b else print("=") if a == b else print("b")


# practicle example
username = ""
display_name = username if username else " kaushik chavda "

print("welcome", display_name)
