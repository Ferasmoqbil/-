#نحط فانكشن ونحط القيمه الافتراضيه فاضيه

def info(name="unknown", age="unknown", country="unknown"):
    print(f"Name: {name}, Age: {age}, Country: {country}")

#نساله عن الحاجات عشان نملي القيمه الافتراضيه

newname = input("what's your name :\n").capitalize().strip()
agee = input("how older are you: \n").strip()
countryy = input("where's are you from: \n").capitalize().strip()

#نحط الاجوبه من الاسئله بدل القيمه الافتراضيه

info(newname, agee, countryy)
# اظن اخر كود ب الفتره الصباحيه