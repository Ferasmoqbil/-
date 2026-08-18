# نستدعي مكاتب 
import pyfiglet
import termcolor

# سؤال عن الاسم للتعديل: 
name = input("enter your name: ")

# يطبع الاسم لوحده بدون الوان فقط شكل 
# print(pyfiglet.figlet_format("ashil"))

# يطبع الشكل واللون الذي ستختاره: 
print(termcolor.colored(pyfiglet.figlet_format(name), color= "magenta"))

# magenta == purple 