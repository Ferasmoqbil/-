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


# Two Dimensional Dictionary
languages = {
    "one" : {
        "name" : "html",
        "progress" : "10%"
    },
    "Two" : {
         "name" : "python",
         "progress" : "80%"
    },
    "Three" : {
            "name" : "Js",
            "progress" : "10%"
        }
}

print("=" * 50)
print(languages)
print("=" * 50)
print(languages["one"])
print("=" * 50)
print(languages["Three"]["name"])
print("=" * 50)
