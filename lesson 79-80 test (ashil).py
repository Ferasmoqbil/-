# نسحب راندوم للعشوائية لاكن مو كامله فقط الي نحتاجة عشان المساحة
from random import choice

print ("you just can guess with this name's \nashil \nferas \nmuhamed \nasyl \nebstin \ndidi \nbilal \nosama")
# نسوي القائمة ونخليها من المسافات الي ممكن يحطها المستخدم 
guess = input("guess the name inside the list: ").strip().lower()

list = ["ashil", "feras", "muhamed", "aseel", "ebstin", "didi", "bilal", "osama"]

# تجاهل التالي هذي فانكشن نزع الاحرف المتكرره فقط :
def cleanword(text):

     if len(text) == 1:

        return text
    
     if text[0] == text[1]:


        return cleanword(text[1:])
    
     return text[0] + cleanword(text[1:])


# نحط الخيار العشوائي في متغير راندو: 
rando = choice(list)

cleanword(rando)

if rando == "ebstin":
    print(f"look!! it's your brother: [{rando}]")

elif guess == rando:
    print(f"you huess right the name's : {rando}")

else:
    print(f"sorry you guess is wrong bcs the name is {rando}")

# هذه كود ما فيه فايده غير اختبار لنفسي + انا فاضي وابغا ابرمج لاكن مكسل اشوف مقاطع دون حراك