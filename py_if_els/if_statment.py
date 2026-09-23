# simple if statment
a = 300
b = 400

if a < b:
    print("b graterthen a ")

# multiple statment in the block
age = 18

if age >= 18:
    print("you are adult")
    print("you can vote")
    print("you have full legal right")


# elif statment
age = 70

if age < 13:
    print("you are child")
elif age < 20:
    print("you are teenager")
elif age < 60:
    print("you are adult")
elif age >= 65:
    print("you are senior")

# else statment


a = 500
b = 300
if b > a:
    print("b is grater then a")
elif a == b:
    print("a and b are equal")
else:
    print("a is grater then b")

# else withuot elif
a = 20
b = 20
if b > a:
    print("b is grater the a")
else:
    print("b is not garter then a ")

    # else as fallback
username = "email"
if len(username) > 0:
    print(f"welcome,{username}!")
else:
    print("error: username can not be empty")
