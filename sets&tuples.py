shopping_list = ["eggs", "milk", "bread", "butter"]
print(type(shopping_list))
shopping_tuple = (("eggs", "milk", "bread", "butter"),"eggs", "milk", "bread", "butter")
print(type(shopping_tuple))

#list are mutable
#tuples are immutable

#dictionaries------
#unordered key value pairs

student_1 = {
    "name": "lewis",
    "stream": "data",
    "list": [1,2,3,4]
}

student_1["name"] = "notLewis"
student_1["list"].remove(2)

print(student_1)


#SETS AND FROZEN SETS
#they can almost be treated like a list
#sets contain only unique values

carParts = {"wheels", "doors", "windows", "engine"}
print(type(carParts))
carParts.add("antenna")
carParts.discard("doors")
print(carParts)