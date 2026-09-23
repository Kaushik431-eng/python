thisdics = {"name": "kaushik", "age": 20, "cource": "mca"}

print(thisdics)
print(thisdics["name"])
print(len(thisdics))
print(type(thisdics))


# access Dictionaries items

# get keys

mydetails = {"name": "kaushik chavda", "age": 20}
x = mydetails.keys()
print(x)


fruits = {"name": "banana", "price": 50}
x = fruits.keys()
print(x)
fruits["contiti"] = 20

print(x)

# items
dicsitems = {"name": "zain siddiqui", "city": "una"}
x = dicsitems.items()
print(x)

# change the dictionaries items

mydetails = {"name": "kaushik chavda", "city": "dhari", "post": "data scientist"}
mydetails["city"] = "vaghavadi"

print(mydetails)

# update dictionaries

amploy = {
    "name": "kaushik",
    "email": "kaushikchavda919@gmail.com",
    "password": "12345678909",
}
amploy.update({"name": "zain"})
print(amploy)

# add items

amploy = {"name": "navdeep", "email": "navdeep@gmail.com", "password": "niks1232"}
amploy["company"] = "xbyts"
print(amploy)

# remove items

amploy2 = {
    "name": "kaushik",
    "age": 20,
    "email": "kaushikchavda919@gmail.com",
    "password": 12345432,
}
amploy2.pop("age")

print(amploy2)
