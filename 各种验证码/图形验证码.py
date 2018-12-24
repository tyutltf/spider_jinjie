import pytesseract
from PIL import Image
import tesserocr



#简单验证  特别垃圾
image=Image.open('3.jpg')
result=tesserocr.image_to_text(image)
print(result)


#完全验证 也不咋地。。
image1=Image.open('3.jpg')
image1=image1.convert('L')
threshold=127
table=[]
for i in range(256):
    if i <threshold:
        table.append(0)
    else:
        table.append(1)
image2=image1.point(table,'1')
image2.show()  #二值化图片显示
result=pytesseract.image_to_string(image2)
print(result)