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
        numbersUntilGreenPixel.append(numberPixels)
        numberPixels=0
       
        """ img.putpixel((x,y),255) """
    else:
        numberPixels+=1



letter=[]
for i in numbersUntilGreenPixel:
    for x in range(len(numbersUntilGreenPixel)):
        if (numbersUntilGreenPixel[x]==1 or numbersUntilGreenPixel==27*i):
            letter.append('a')
        elif (numbersUntilGreenPixel[x]==2 or numbersUntilGreenPixel==28*i):
            letter.append('b')
        elif (numbersUntilGreenPixel[x]==3 or numbersUntilGreenPixel==29*i):
            letter.append('c')
        elif (numbersUntilGreenPixel[x]==4 or numbersUntilGreenPixel==30*i):
            letter.append('d')
        elif (numbersUntilGreenPixel[x]==5 or numbersUntilGreenPixel==31*i):
            letter.append('e')
        elif (numbersUntilGreenPixel[x]==6 or numbersUntilGreenPixel==32*i):
            letter.append('f')
        elif (numbersUntilGreenPixel[x]==7 or numbersUntilGreenPixel==33*i):
            letter.append('g')
        elif (numbersUntilGreenPixel[x]==8 or numbersUntilGreenPixel==34*i):
            letter.append('h')
        elif (numbersUntilGreenPixel[x]==9 or numbersUntilGreenPixel==35*i):
            letter.append('i')
        elif (numbersUntilGreenPixel[x]==10 or numbersUntilGreenPixel==36*i):
            letter.append('j')
        elif (numbersUntilGreenPixel[x]==11 or numbersUntilGreenPixel==37*i):
            letter.append('k')
        elif (numbersUntilGreenPixel[x]==12 or numbersUntilGreenPixel==38*i):
            letter.append('l')
        elif (numbersUntilGreenPixel[x]==13 or numbersUntilGreenPixel==39*i):
            letter.append('m')
        elif (numbersUntilGreenPixel[x]==14 or numbersUntilGreenPixel==40*i):
            letter.append('n')
        elif (numbersUntilGreenPixel[x]==15 or numbersUntilGreenPixel==41*i):
            letter.append('o')
        elif (numbersUntilGreenPixel[x]==16 or numbersUntilGreenPixel==42*i):
            letter.append('p')
        elif (numbersUntilGreenPixel[x]==17 or numbersUntilGreenPixel==43*i):
            letter.append('q')
        elif (numbersUntilGreenPixel[x]==18 or numbersUntilGreenPixel==44*i):
            letter.append('r')
        elif (numbersUntilGreenPixel[x]==19 or numbersUntilGreenPixel==45*i):
            letter.append('s')
        elif (numbersUntilGreenPixel[x]==20 or numbersUntilGreenPixel==46*i):
            letter.append('t')
        elif (numbersUntilGreenPixel[x]==21 or numbersUntilGreenPixel==47*i):
            letter.append('u')
        elif (numbersUntilGreenPixel[x]==22 or numbersUntilGreenPixel==48*i):
            letter.append('v')
        elif (numbersUntilGreenPixel[x]==23 or numbersUntilGreenPixel==49*i):
            letter.append('w')
        elif (numbersUntilGreenPixel[x]==24 or numbersUntilGreenPixel==50*i):
            letter.append('x')
        elif (numbersUntilGreenPixel[x]==25 or numbersUntilGreenPixel==51*i):
            letter.append('y')
        elif (numbersUntilGreenPixel[x]==26 or numbersUntilGreenPixel==52*i):
            letter.append('z')
        else:
            print(numbersUntilGreenPixel[x])
print(letter)


File_object.write(text)
File_object.close()
img.show()