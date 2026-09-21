# create the variables

x = 5
y = 10

print(x + 10)
print(y)

# casting
x = str(3)
y = int(3)
z = float(3)

print(x, y, z)


# get the type function using
x = 20
y = "kaushik"

print(type(x))
print(type(y))


# assign multiple value

x, y, z = "kaushik", "zain", "navdeep"

print(x)
print(y)
print(z)

# output variables

x = "kaushik chavda is a data scientist"

print(x)

x = "kaushik chavda"
y = "is a"
z = "data scientist"

print(x, y, z)

# global variable
x = "kaushik chavda "


def myfunc():
    print("my name is " + x)


myfunc()
