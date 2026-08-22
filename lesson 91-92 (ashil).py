try:
    # اذا مافي ايرور بيطبعها
    x = float([5,9,1,1,1,1])
    print(x)
except NameError:
    # اذا في خطا من هذا النوع نوع الاسم ب يطبع ذا: 
    print("name error, ashil")
except ValueError:
    # اذا في خطا من هذا النوع بيطبع ذا 
    print("value error, ashil")
except TypeError:
        # اذا في خطا من هذا النوع بيطبع ذا: 
    print("None type, ashil")
except list:
        # اذا في خطا من هذا النوع بيطبع ذا: 
    print("list error, ashil")
except:
    # اذا في اي خطا اخر ما ذكرته اطبع ذا: 
    print("there's a error!!, ashil")
finally:
    # في كل الحالات اذا في خطا او لا اطبع ذا : 
    print("typing in your note!!")
# فقط اجرب الاداة والايرور 
