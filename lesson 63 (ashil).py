#المهمه كود لو في اكثر من حرف يبعدهم ويخلي بس الكلمه بدون حروف

# ناخذ الاسم لو هو يطبع له الطريقه كيف تشتغل ام بس تشتغل وخلاص
name = input("what's your name Before anything:\n")
# ناخذ الكلمه 
x = input("what's the words: ")
# الامر الخاص ب الادمن ويشرح طريقه التشغيل:
if name == "feras" or name == "ashil":
    
 def cleanword(text):

    if len(text) == 1:

        return text
    
    if text[0] == text[1]:

        print(text) # هذي البرينت هي تطبع طريقه التشغيل او الكود من منظور الالة

        return cleanword(text[1:])
    
    return text[0] + cleanword(text[1:])

# اذا مو من الادمن يوريه الاجابه علطول:
else:
    def cleanword(text):

     if len(text) == 1:

        return text
    
     if text[0] == text[1]:


        return cleanword(text[1:])
    
     return text[0] + cleanword(text[1:])

# يطبع الكلمه للادمن وغير الادمن في الاخير
print("\nthe final word's: " + cleanword(x))