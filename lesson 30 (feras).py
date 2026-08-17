#Dictionry


# قاعد اتعلم كتابة القواميس و ايش هي بس
user = {
    "name" : "feras",
    "age" : 16,
    "country" : "yemene",
    "skills" : ["Pythone"],
    "rating" : 1
}

print(user)
# طرسقة لطباعة عنصر محدد في القاموس
print(user["name"])
#طريقة اخرى لطباعة عنصر في القاموس
print(user.get("age"))

# بيطبع لي جميع المفاتيح في القاموس
print(user.keys())
# بيطبع لي جميع العناصر في القاموس
print(user.values())