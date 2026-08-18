#تطبيق عملي للانبوت او الادخال بس
#اولا باسال عن الاسم و الايميل
name=input("What's your name? : ")
email=input("What's your email? : ")
#ثانيا اقوم باخذ اليوزر و الويب سايت 
TheUser= email[:email.index("@")]
TheWebsit= email[email.index("@") + 1:]
#ثالثلا اقوم بطباعة
print(f"hi {name.capitalize().strip()}, wilcome to hare, your email {email}")
print(f"your user is {TheUser} and your websit is {TheWebsit}")