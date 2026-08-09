#الهدف نسوي لوب ب استخدام اف ونخليه يطبع اسماء الطلاب واذا كان اسم الطالب هو اشيل او فراس يطبع لهم جملة خاصة

#قائمة الطلاب:

study = ["mohab", "ashil", "feras", "mohamed", "ali"]


# حلقه لوب باسخدام اف

for i in sorted(study):


    #اذا كان اسم الطالب هو اشيل او فراس يطبع لهم جملة خاصة

    if i == "ashil" or i == "feras":
        print("the best student is🦥 :" + i)


    # واذا كان اسم الطالب غير اشيل او فراس يطبع لهم جملة عادية

    else:
        print("the students name's this year is :" + i)


#انتهت الحلقة

print("loop is done")