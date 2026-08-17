#clear()
#يقوم بتنضيف set
a={1, 2, 3,}
a.clear()
print(a)


#union()
# يقوم بدمج عناصر set ولاكن كما يبدوا بدون ترتيب
b={"one", "two", "three"}
c={1, 2, 3,}
x={"zero", "cool"}
# اختصار union()
print(b | c)
#union بدون اختصار
print(b.union(c, x))


#add
# يقوم اضافة عنصر واحد الى اخر set
d={1, 2, 3, 4}
#d.add(5, 6) # لا تضع اكثر من عنصر في add لانه بيطلع لك erorr
d.add(5)
d.add(6)
print(d)


#copy
# تقوم بنسخ
e={1, 2, 3, 4}
f=e.copy()
print(f)


#remove()
# ادات للحذف
f={1, 2, 3, 4}
f.remove(1)
#f.remove(7)# بيطلع لك خطا لان ادات الحذف remve يجب ما تقوم بحذفة موجوجد
print(f)


#discard()
# ادات للحذف
g={1, 2, 3, 4}
g.discard(1)
f.discard(7)# يقوم بحذف الاشياء التي تطلبها اذا وجدت واذا لم توجد لن يحصل خطا على عكس remove
print(g)


#pop()
# يقوم pop في set باخراج عنصر عشوائيا لانه في set لا يمكنك تحديد العنصر
i={"A", True, 1, 2, 3, 4, 5}
print(i.pop())



#update
#يقوم هذا الكود بتحديث العنصر بإضافة العنصر ب÷ستخام update() وتشبه add() ولاكن بحذفر العناصرالمكررة
j= {1, 2, 3}
k={1, "A", "B", 2}
j.update(["Html", "Css"])
j.update(k)
print(j)