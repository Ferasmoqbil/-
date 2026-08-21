# نستورد المكتبة:
from PIL import Image

# نحط رابط الصوره الي اخل ملف الكود لو كان جماعي ولو كان خاص نحط رابطها الي في الكمبيوتر: 
urlofimage = "Screenshot 2026-04-20 002414.png"

# نفتحها عشان نعدل عليها براحتنا
# (ملاحظة: الفتح ليس عرض الصورة) 
myimage = Image.open(urlofimage)

# نحط احداثيات نستخدمها للقص داخل متغير 
mybox = (50, 200, 600, 600)

# نقص ونحط متغير الاحداثيات: 
croping = myimage.crop(mybox)

# نحطهم كلهم في متغير ونغير اللون للاسود باستخدام حرف ال : 
myconveted = croping.convert("L")

# نعرض الصورة: 
myconveted.show()

# نحفظها في اسم جديد عشان تشتغل وتنعرض ب نجاح : 
myconveted.save("newimage.png")

# (ملاحظة: في حركات للتعديل افضل لاكن هو ذكر قال انها كثيره والافضل انك تدرسها لانها سهلة وما تحتاج شرح) 
# وهذا هو الرابط الي اعطانا عشان نذاكر منه 
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html