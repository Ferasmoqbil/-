# بحاول اسوي كود ينشئ ملف في مكان الاكواد ويعدل عليه براحة المستخدم 

user_file = open("user_file.text","w", encoding='UTF-8')

# سؤال المستخدم : 
user = input("what are u gonna write in this file: \n") # قيمه متغيره 

# نكتب مثل ما المستخدم كتب, داخل الملف
user_file.write(user)

# نقفله للمستخدم ك احتياط اذا حصل قليتش وسالة مره اخرئ 
user_file.close()

# ننشئ متغير للقراءة ونحط مسار الملف ونخليه للقراءة فقط 
read_file = open("user_file.text", "r")


# نطبع ماذا موجود دخل الملف 
print (read_file.read())

# نقفله للحفظ
read_file.close()