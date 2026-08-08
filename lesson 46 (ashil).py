# المطلوب قائمة ادمن تسالك عن اسمك وتتاكد اذا موجود
# تستطيع ان تدخل اسمك وهي تضيفك لقائمة الادمن
# ويقدر يحذف اسم من الاسماء او يضيف اسم

admin = ["Ashil", "Feras"]

# نساله عن اسمه للتاكد من اذا كان موجود في الادمن ام لا

name = input("what's your name?.. ").strip().capitalize()

# استقبال اذا كان في الادمن

if name in admin:
    print(f"hi {name} you are in admin welcome back")

# نعطيه خيارات الحذف والاضافه ورؤيه قائمه الادمن

    edit = input (" to select delete enter '1' to enter new name enter '2' if u want to see the list enter anything ec(1-2)")
    if edit == "1":

        delete_name = input(f"witch name u want to delete?\n{admin}").strip().capitalize()

# نبحث عن الاسم الذي من المفترض ان نحذه اذا كان موجود في القائمه ام لا

        if delete_name in admin:

# نحذفه اذا تواجد

            admin.remove(delete_name)
            print (admin)

#اذا الاسم غير موجود نطبع له هذه الرساله 

        else:

            print(f"sorry there's nobody his name's {delete_name}")


    elif edit == "2":

#نسال عن الاسم الجديد الذي سينضاف

        new_name = input("what's your new name? ").strip().capitalize()

        # نضيف الاسم

        admin.append(new_name)

 # نطبع قائمه جديدة ليراها

        print(f"you have added this's a new list {admin}")

# نعطيه القائمه اذا ادخل شي غير الحذف والاضافه لان تم التاكد انه ادمن

    else:
        print(f"this's admin list \n{admin}")

#اذا هو مو ادمن نطبع له ذي
else:
    print("sorry you are not in admin")