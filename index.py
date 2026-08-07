#حلقة رقم42
# المطلوب تطبيق يسال عن الدوله والحالة اذا كان يدرس ام لا ويحدد السعر علئ هذه المعايير

Price = 100
name = input("what's your name?").capitalize()
country = input("where are you from? ").capitalize()
study = input("do u study? (yes/no) ")


#if country == "Ksa" or "Egypt" or "Yemen": (error) يجب ان يكون كل شرط على حده


if country == "Ksa" and country == "Egypt" and country == "Yemen":


    Price -= 50 # ينخفض السعر ب النسبه للدول العربية المحددة


    if study.lower() == "yes" or study.lower() == "y" or study.lower() == "yas" or study.lower() == "yess":
        print(f"hello {name} from {country}. your price is: {Price - 20} SAR.")
    else:
        print(f"hello {name} from {country}. your price is: {Price} SAR.")


else: #اذا كان لون الكود الذي في الاسفل ب اللون الغامق او داكن فاعلم انه لن يتفعل في جميع الحالات الذي سيدخلها المستخدم


    if study.lower() == "yes" or study.lower() == "y" or study.lower() == "yas" or study.lower() == "yess":
        print(f"hello {name} from {country}. your price is: {Price - 20} SAR.")
    else:
        print(f"hello {name} from {country}. your price is: {Price} SAR.")

#(اصيل) استغرق الكود 7د اذا كان هناك تعديلات اخبرني علئ الانستقرام.