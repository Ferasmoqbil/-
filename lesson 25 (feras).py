#Tuple Concatenation
#دمج Tuple
a=1, 2, 3, 4
b=5, 6
c= a + b
d= a+ ("feras", "A", True) + b
print(c)
print(d)

#Tiple, List, String Repeat (*)
#يقوم بتكرار القائمة او str او Tuple
string=("feras ")
List=[1, 2]
Tuple= "A", "B"

print(string*6)
print(List*6)
print(Tuple*6)


# Method => count()
# يعد كم تكررت الحاجة التي تطلبها كم مرة
x= (1, 2, 3, 8, 4, 5, 6, 7, 8,)
print(x.count(8))


# Method => index()
#يخبرك مكان او انداكس الشيء التي تريد تبحث عنه 
z=1, 3, 7, 8, 2, 6, 5
print(z.index(7))
# print(f"The Position of index Is: " + {z.index(7)}) #ذا الكود بيسبب مشكلة لازم نستعمل الفورمات
print(f"The Position of index Is:  {z.index(7)}")


#Tuple Destruct
n= "A", "B", "C"
m, j, t=n

print(m)
print(j)
print(t)
