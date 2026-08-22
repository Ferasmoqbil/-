# الاسثنائات | Exceptions

# يشوف الرقم ويخليك انت تكتب الايرور

# نسجل الرقم في متغير: 
num = input("gimmi random number: ")

# اذا الرقم موجود في مكتبة الحروف الكبيرة والصغيرة يعطيه الايرور 
if not num.isdigit():

# الايرور انت تكتبة مابين القوسين العلامتين حق النصوص :
    raise ValueError(f"{num} is not even a number!!")

else:

# اذا ادخل رقم اطبع:
    print(f"{num} is a good number🦥")


# (ملاحظة: يجب علئ الرقم ان يكون من نوع انتيجير)

# الموقع الخاص ب حلول الاستثناءات :

# https://docs.python.org/3/library/exceptions.html 