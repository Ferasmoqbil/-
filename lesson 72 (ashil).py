# تجربة للفهم 

def formatout(text):
#    print(text)
    return f"- {text} -"

my_friends = ["ashil", "feras", "ahmed"]

# ماب لتفعيل الربط بين الفانكشن مع كل اسم موجود في القائمة او مجموعة الاشياء والاسماء
for x in map(formatout, my_friends):
    print(x)

#formatout("ahmed")