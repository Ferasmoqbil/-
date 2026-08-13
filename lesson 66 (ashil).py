# نقرأ ماذا بداخل الملف تبعنا من اكواد او الخ 
test_file = open("ashil.text", "r")

# امر القراءه يقرا كل شيئ :
#print(test_file.read())

# فاصل
#print("-"*50)

# يقرا السطر كامل :
#print(test_file.readline())

# نسوي مشروع بسيط يطبع الي داخل الملف حبه حبه
for lines in test_file:
    print(lines)

# اذا وصلت الاحرف الابجديه لحرف الاي, وقف
    if lines.startswith("E"):
        break