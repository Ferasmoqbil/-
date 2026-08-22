'''
this code gonna ask for number 
if the number the user give it to him is integer
he will say " (number) it's a good number!!"
and if user give him something's not even a number
he's gonna say "bad, this is not number"
'''
#  يجرب الكود وتحكم اكبر ب استخدام "جرب" وتتحكم ب الايرور
try:
    askforinteger = int(input("gimmi integer number: "))

# اذا طلع ايرور استثناء او ايرور يطبع : 
except:
    print("bad, this is not number")

# غير ذلك والكود مشي طبيعي يطبع ذا : 
else:
    print(f"{askforinteger} it's a good number!!")
