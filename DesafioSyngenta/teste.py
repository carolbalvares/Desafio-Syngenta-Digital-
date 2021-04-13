from PIL import Image 
img = Image.open('HireMe.bmp')

File_object = open(r"secret.txt","w")
text=''
cont=0
numbersUntilGreenPixel=[]
numberPixels=0
for y in range(img.height):
  for x in range(img.width):
    pixel = img.getpixel((x, y))
    text += str(pixel)
    if pixel==51:
        numberPixels=0
        cont+=1
        """ img.putpixel((x,y),255) """
    else:
        numberPixels+=1

print('Numero de pixels verdes:')
print(cont)

File_object.write(text)
File_object.close()
img.show()