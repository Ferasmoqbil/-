#setdefault()
# يقوم باضافة العنصر اذا لم يكن موجود واذا كان موجود سيضهر فقط
user={
    "name" : "feras"
}
print("=" * 50)
print(user)
print(user.setdefault("name", "Ahmad"))
print(user.setdefault("age", 16))
print(user)
print("=" * 50)


#popitem()
# يستخرج اخر شيء ضفته داخل القتموص
member={
    "name" : "feras"
}
print(member)
member.update({"age" : 16})
print(member.popitem())
print("="*50)


#items()
#
view={
    "name" : "feras",
    "skill" : "PS4"
}
allItem = view.items()
print(view)
view["age"] = 16
print(allItem)
print("=" * 50)


#fromkeys()
#
a=("keyone", "keytwo", "keythree")
b=("X")
print(dict.fromkeys(a, b))
print("=" * 50)