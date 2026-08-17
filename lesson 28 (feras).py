#difference()
# مافهمت ايش فايدة بشكل تمام اصلا
a={1, 2, 3, 4}
b={1, 2, 3, "feras", "ashil"}
print(a)
print(a.difference(b)) #a - b
print(a)
print("=" * 40)


#difference_update()
# نفس فايدة الاولى بس في الاولى ما يتحدث و في ذي يتحدث
c={1, 2, 3, 4}
d={1, 2, 3, "feras", "ashil"}
print(c)
c.difference_update(d) #c - d
print(c)
print("=" * 40)


#intersection()
# يقوم بإستخراج العناصر المشتركة و حذف العناصر الغير مشتركة ولاكن بدون تحديث او حفظ ذلك
e={1, 2, 3, 4, "X"}
f={"feras", "X", 2}
print(e)
print(e.intersection(f)) #e & f
print(e)
print("="*40)


#intersection_update()
#يقوم بإستخراج العناصر المشتركة و حذف العناصر الغير مشتركة و يقوم بتحديث ذلك و حفظه
g={1, 2, 3, 4, "X"}
h={"feras", "X", 2}
print(g)
g.intersection_update(h) #g & h
print(g)
print("="*40)


#symmetric_difference()
# هاد مهمته يطلع الحاجات الغير موجودة فيلاالاثنين يعني يقوم بحذف الاشياء المشتركة ويبقي الاشياء الغير المشتركة ولاكن بدون حفظ او تحديث
i={1, 2, 3, 4, 5, "X"}
j={"feras", "Zero", 1, 2, 3}
print(i)
print(i.symmetric_difference(j))
print(i)
print("="*40)


#symmetric_difference_update()
# هاد مهمته يطلع الحاجات الغير موجودة فيلاالاثنين يعني يقوم بحذف الاشياء المشتركة ويبقي الاشياء الغير المشتركة ولاكن بدون حفظ او تحديث
k={1, 2, 3, 4, 5, "X"}
l={"feras", "Zero", 1, 2, 3}
print(k)
k.symmetric_difference_update(l)
print(k)
print("="*40)