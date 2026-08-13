# مجرد تطبيق للفانكشن الثاني لان هناك طريقتين

#اسئله:
first_name = input ("hi what's your name: ")
sec_name = input("hello what's your sec name: ")

# اول فانكشن وهو المشهور:
def say_hi(name):
    return print("hello "+ name)

# ثاني فانكشن: 
hello = lambda name : print("hi "+ name)

# استدعائهم
hello(first_name)
say_hi(sec_name)