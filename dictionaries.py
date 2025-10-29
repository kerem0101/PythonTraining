mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict2["name"]
print(value)

mydict["email"]="max@xyz.com"
print(mydict)

mydict["email"]="coolmax@xyz.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

if "city" in mydict:
    print(mydict["city"])

try:    
    print(mydict["city"])
except:
    print("Error")

for key in mydict2:
    print(key)

for value in mydict2.values():
    print(value)


for key, value in mydict2.items():
    print(key, value)

mydict2_cpy=mydict2
mydict2_cpy["email"]="mary@xyz.com"
print(mydict2_cpy)
print(mydict2)

mydict2_cpy=mydict2.copy() #dict(mydict) is same
mydict2_cpy["number"]="698-754"
print(mydict2_cpy)
print(mydict2)

print(mydict)
print(mydict2)
mydict2.update(mydict)
print(mydict2)

mydict3 = {3: 9, 6: 36, 9: 81}
print(mydict3)
value = mydict3[3]
print(value)

mytuple = (8,7)
mydict = {mytuple: 15}
print(mydict)