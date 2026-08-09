# Tuple Syntax & Type Tuple
tuple1= ("feras", "ashil")
tuple2= "feras", "ashil"
print(tuple1)
print(tuple2)


print(type(tuple1))
print(type(tuple2))


#Tuple Indexind
tuple3= 1, 2, 3, 4, 5
print(tuple3[-2])
print(tuple3[2])


#Tuple Assing Vaiues
tuple3= 1, 2, 3, 4, 5
# tuple3[-1]= "three"
#لا ينفع تبديل او اضافة او تعديل على Tuple على عكس list
#print(tuple3) #ان فعلت هذا الكود بيضهر لك خطا


#Tuple Items
#هنا شفت بس ان Tuple انها تستقبل كل الانواع اولا للتاكد
tuple4= "feras", "feras", 1, 2, 3, 100.5, True
print(tuple4[-1])
print(tuple4[-2])
print(tuple4[1])