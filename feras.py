# هنا متغيرات للتجربة
name = "feras"
age = 16
rank = 1

#هنا قاعد اجرب الكود العادي بدوم استعمال "%s"
print("my name is : " +name)
#هنا قاعد اجرب الكود مع استعمال "%s"
#وهي للكلماتٍ
print("My Name is : %s\nMy Age is : %s"% (name, age))
#وهنا استعملت "%d"
#وهي للارقام الصحيحة
print("My Name is : %s\nMy Age is : %d"% (name, age))
#وهنا استعملت "%f"
#وهي للارقام الهشرية
print("My Name is : %s\nMy Age is : %d\nand My Rank is : %f"% (name, age, rank))

# %s => str
# %d => int
# %f => flout

############################################################################

# اسم ثاني للتجربة ثانية
name_two = "ashil"
# لغة البرمجة الي تستعملها
language = "python"
# المدة او الخبرة
month = 6
print("My Name is %s, I'am %s Developer With %d Months Exp" % (name_two, language, month))
############################################################################

#التحكم بالارقام العشرية (flout)
My_Number = 10
# هنا سابلي 6 اصفار عشرية
print("My Number is: %f"% My_Number)
# سابلي 2 اصفار عشرية 
print("My Number is: %.2f"% My_Number)
#_________________________________________________________---

#هنا بجرب التحكم بالنصوص بإستخدام "%s"
mess = " hi my friends and fuck "+ name_two 
print("My message is: %s"% mess)
print("My message is: %.13s"% mess)