from random import randint, uniform

# نسأل المستخدم يدخل الرقم اللي يشتيه
ask = input("gimmi ltimit for random numbers: ")

# نفحص إذا الكلمة فيها نقطة، يعني المستخدم أدخل رقم عشري (float)
if "." in ask:
    limit_float = float(ask)
    
    # نقسم النص من عند النقطة ونحسب كم أرقام أجو بعد الفاصلة بالضبط
    decimals = len(ask.split(".")[1])
    
    # نطلع رقم عشوائي عشري بين 1 والرقم اللي أدخله
    raw_num = uniform(1, limit_float)
    
    # هنا الفكرة! ننسق الرقم عشان يطبع نفس عدد الخانات بالضبط حتى لو فيها أصفار باليمين
    random_num = f"{raw_num:.{decimals}f}"
    
    print(f"your randomlly number's {random_num}")

# إذا ما بش نقطة، نفحص هل المدخل فيه حروف أو رموز مش أرقام
elif not ask.isdigit():
    print(f"sorry [{ask}] is not even number")

# إذا طلع رقم صحيح (int) وما بش فيه مشاكل
else:
    limit = int(ask)
    print(f"your randomlly number's {randint(1, limit)}")