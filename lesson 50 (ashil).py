#بسيط يحتاج فقط تحت كلمة سر وتطلب من المستخدم ادخالها وطالما هي خطا لا تسمح له
#3 عنده 5 محاولات

password = "a&f"
tries = 5

#السؤال

chick_password =input("what's the password: ")

#طالما الذي ادخله لا يساوي الباوسورد الصحيح نقص واطبع واسال مجددا

while chick_password != password:

    tries -= 1
    print(f"wrong password!!\nyou have last {tries} tries")
    chick_password = input("typing password again:\n")

# اذا وصلت المحاولات للصفر يعني حتئ لو كتب لا تاخذ منه

    if tries == 0:

        print("-" * 50 + "\nyou have end your tries!!")
        break  

#اذا كلمه السر صحيحه نفذ هذه الاوامر:

else: 
    print("_" * 50 + "\n")
    print ("yup that's it🦥")