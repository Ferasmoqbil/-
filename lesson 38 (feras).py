#User Input
# يقوم هذا الكود باخذ اسمك و السلام عليك فقط

fname=input("What's your first name? : ")
mname=input("What's your middle name? : ")
lname=input("What's your last name? : ")

fname=fname.strip() .capitalize()
mname=mname.strip() .capitalize()
lname=lname.strip() .capitalize()

print(f"Hi {fname} {mname} {lname}, naice to meet you")