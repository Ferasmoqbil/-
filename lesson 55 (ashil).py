#انشاء قائمه من نوع ديكشناري ونرتبها ب الطباعه باستخدام اف 


#القائمة:

mytest = {
    "HTML":{
        "title": "My Website",
        "description": "This is my website"
    },
    "css":{
        "background-color": "white",
        "color": "black"
    },
}

#نبدا نخليه يطبعهم منفصلين

for key, value in mytest.items():

#يطبع الاسم الاول لحاله

    print(f"{key} is")

#يفصل المميزات ك واحده بسطر وكل واحده مع الاسم تبعها والوصف تبعها

    for new, old in value.items():

# الفصل والطباعه

        print(f"{new} => {old}")

