company = {
    "employ1": {"name": "kaushik chavda", "age": 20, "post": "data scientist"},
    "employ2": {"name": "niks dattani", "age": 21, "post": "video editor"},
    "employ3": {"name": "zain siddiqui", "age": 22, "post": "bussiness analitics"},
    "employ4": {"name": "price sojitra", "age": 22, "post": "video editor"},
}

print(company)


# loop through nested dictionaries


company = {
    "employ1": {"name": "kaushik chavda", "age": 20, "post": "data scientist"},
    "employ2": {"name": "niks dattani", "age": 21, "post": "video editor"},
    "employ3": {"name": "zain siddiqui", "age": 22, "post": "bussiness analitics"},
    "employ4": {"name": "price sojitra", "age": 22, "post": "video editor"},
}
for x, obj in company.items():
    print(x)

    for y in obj:
        print(y + ":", obj[y])
