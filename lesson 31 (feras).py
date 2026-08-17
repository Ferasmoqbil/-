#clear()
# تقوم بتنضيف او حذف العناصر الموجودة داخل القاموص
user={
    "name" : "feras"
}
print(user)
user.clear()
print(user)
print("="*50)


#update()
# يقوم بتحديث او اضافة عناصر داخل القاموص
mamper={
    "name" : "feras"
}
print(mamper)
mamper["age"]=16 #طريقة اخرى بدون update()
print(mamper)
mamper.update({"country":"yamene"})
print(mamper)
print("="*50)


#copy()
# ايش تتقوع اشرح في النسخ بالله
mine={
    "name" : "feras"
}
b=mine.copy()
print(b)
mine.update({"age" : 16})
print(mine)
print(b)
print("="*50)
