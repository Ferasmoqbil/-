# نستدعي دالة الوقت
import datetime

# نسال المستخدم لتكمله المعلومات : 
years = int(input("what's year your have born in it?: "))
month = int(input("what's month your have born in it?: "))
day = int(input("what's day your have born in it?: "))

# ناخذ الوقت ونحطه في متغير ليسهل استدعاءه 
birth = datetime.datetime(years, month, day)

# نحط الوقت الحالي في متغير: 
now = datetime.datetime.now()

# نسوي حسبة بسيطة لنطلع السنين والاشهر : 
age_years = now.year - birth.year - ((now.month, now.day) < (birth.month, birth.day))
age_months = (now.year - birth.year) * 12 + now.month - birth.month

# ناخذ الي المستخدم سجله وننقصه من الوقت الحالي
print(f"you lived for {(now - birth).days}")
print(f"you lived for {age_years}")
print(f"you lived for {age_months}")

# (ملاحظه: المكتبه ذي تحدث نفسها باجزاء من الثانيه لتسجيل الوقت الحالي فستتغير كل يوم التاريخ عن التاريخ) 