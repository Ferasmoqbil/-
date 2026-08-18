# مشروع الحلقة 75 نتدرب عليه

# يخزن الاجابه ويفصلها ب كوما ","
skills = input ("give me nams of programing lunguage and split with comma ',':\n").split()

# الاداة الجديده والتي تحط ارقام للقوائم
myskills = enumerate(skills, 11)    # تكتب المتغير وتكتب من وين يبدأ

# تقدر تخليه قيمتين لانه اصلا قيميتين بس عشان تحكم اكبر
for c, s in myskills:

    # هنا استخدمت القيمتين للتحكم بماذا اضع الفاصل بينهم 
    print(f"{c} - {s}")

# شغل الكود وبتفهم 