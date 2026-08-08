# هنا متغيرات للتجربة
name = "feras"
age = 16
rank = 1

#هنا قاعد اجرب الكود العادي بدوم استعمال "{:s}"
print("my name is : " +name)
#هنا قاعد اجرب الكود مع استعمال "{:s}"
#وهي للكلماتٍ
print("My Name is : {:s}\nMy Age is : {:d}".format(name, age))
#وهنا استعملت "{:d}"
#وهي للارقام الصحيحة
print("My Name is : {:s}\nMy Age is : {:d}".format(name, age))
#وهنا استعملت "{:f}"
#وهي للارقام الهشرية
print("My Name is : {:s}\nMy Age is : {:d}\nand My Rank is : {:f}".format(name, age, rank))

# {:s} => str
# {:d} => int
# {:f} => flout

############################################################################

# اسم ثاني للتجربة ثانية
name_two = "ashil"
# لغة البرمجة الي تستعملها
language = "python"
# المدة او الخبرة
month = 6
print("My Name is {:s}, I'am {:s} Developer With {:d} Months Exp".format(name_two, language, month))
############################################################################

#التحكم بالارقام العشرية (flout)
My_Number = 10
# هنا سابلي 6 اصفار عشرية
print("My Number is: {:f}".format(My_Number))
# سابلي 2 اصفار عشرية 
print("My Number is: {:.2f}".format(My_Number))
#_________________________________________________________---

#هنا بجرب التحكم بالنصوص بإستخدام "{:s}"
mess = " hi my friends and fuck "+ name_two 
print("My message is: {:s}".format(mess))
print("My message is: {:.13s}".format(mess))


# الان بجرب استعمله في "{:d}" بجرب احط فواصل بين الارقام
My_Money=2009876598087
print("My Money in Bank is {:d}".format(My_Money))


#هنا فصل كل خانه رقمية بـ _
print("My Money in Bank is {:_d}".format(My_Money))


#هنا فصل كل خانه رقمية بـ ,
print("My Money in Bank is {:,d}".format(My_Money))


# اقرء الكود عشان تفهم مالي خلق اشرح
a, b, c= "one", "two", "three"
print("Hello {} {} {}".format(a, b, c))
#قاعد اتعلم كيف اغير الترتيب بس
print("Hello {1} {2} {0}".format(a, b, c))
print("Hello {2} {0} {1}".format(a, b, c))


#قاعد اجرب بس انت اصلا فاهم المكتوب مافي داعي اشرح
x, y, z= 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:F} {0:.3f} {1:.1f}".format(x, y, z))



#ولا شيء بس قرمات بإستعمال f
print(f"my name is: {name} and my age is: {age}")