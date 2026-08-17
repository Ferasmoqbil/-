#issuperset()
# هنا يقلك هل عناصر المتغير الثاني موجود في المتغير الاول 
a={1, 2, 3, 4}
b={1, 2, 3}
c={1, 2, 3, 4, 5}
print(a.issuperset(b)) #True
print(a.issuperset(c)) #False
print("=" * 40)


#issubset()
# هنا يقلك هل عناصر المتغير الاول موجود في المتغير الثاني 
d={1, 2, 3, 4}
e={1, 2, 3}
f={1, 2, 3, 4, 5}
print(d.issubset(e)) #False
print(d.issubset(f)) #True
print("=" * 40)


#isdisjoint()
# هذا الكود يقوم بنضر الا المغيرات او السيت ليرا هل هناك عناصر مشتركة او لا لو يوجد عناصر مشتركة يعطينا False ولو كان لايوجد عناصر مشتركة يعطينا True
g={1, 2, 3, 4}
h={1, 2, 3}
i={10, 11, 12}
print(g.isdisjoint(h)) #False
print(g.isdisjoint(i)) #True
print("=" * 40)


