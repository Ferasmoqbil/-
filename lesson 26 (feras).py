#Not Orderwd And Not Index
#يقوم الكود باخذ العناصر  بشل عشوائي و غير مرتب ولايمكنك استعمال Index
my_set_one = {"feras", "ashil", "glal"}
print(my_set_one)
#print(my_set_one[0]) # بإعطاك Error لا تستخدم هذا الكود لانه سوف يقوم 


#Slicing Cant Be Done
#
my_set_two = {1, 2, 3, 4, 5, 6}
#print(my_set_two[0:3]) #ايضا لا يمكنك استعمال هذه الطريقة لانه عشوائي


#Has Omly Immutable Date Type
# جربنا هنا اضافة انواع مختلفة من العناصر لكي نتاكد انها ااقبل اي نوع
#my_set_three={"feras", "feras", 100, 100.5, True, [1, 2, 3]} # السيت لا تقبل القوائم ولاكنها تقل Tuple
my_set_three={"feras", "feras", 100, 100.5, True, (1, 2, 3)}
print(my_set_three)

# اذا لاحضت السيت يقوم بحذف العناصر المكرره عنده تلقائيا
