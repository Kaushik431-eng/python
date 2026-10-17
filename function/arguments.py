def myfunction(frame):
    print(frame + " refsnes ")


myfunction("email")
myfunction("app")
myfunction("mobile")

# number of argument


def myname(fname, lname):
    print(fname, "", lname)


myname("kaushik", "chavda")


# defult parameters value
def def_func(name="kaushik"):
    print("hello", name)


def_func("zain")
def_func("niks")
def_func()


# keyword arguments


def my_key(animal, name):
    print("i have a ", animal)
    print("my", animal, "'s is ", name)


my_key(animal="dog", name="buddy")
