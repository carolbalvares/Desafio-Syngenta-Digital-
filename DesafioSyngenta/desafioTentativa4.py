import ast
import re
from PIL import Image 
img = Image.open('HireMe.jpg')
count = 0
allPixels=[]
for y in range(img.height):
  for x in range(img.width):
    pixel = img.getpixel((x, y))
    if(pixel==(0,0,0)):
        del pixel
    else:
        count+=1
        allPixels.append(pixel)

numbers_array=[]
for element in allPixels:
    for number in element:
        numbers_array.append(number)

grouped_numbers=[]
cont_aux=0
list_aux=[]
for numbers in numbers_array:
    cont_aux = cont_aux + 1
    list_aux.append(numbers)
    if (cont_aux == 8):
        grouped_numbers.append(list_aux)
        list_aux=[]
        cont_aux=0
""" 
for i in grouped_numbers:
    print(i) """

bit_array=[]
bit_aux=[]
for nine_numbers in grouped_numbers:
    for number in nine_numbers:
        if number%2 ==0: #par
            bit_aux.append(1)
        else: #impar
            bit_aux.append(0)
    bit_array.append(bit_aux)
    bit_aux=[]

letter=[]
for nine_bits in bit_array:
    if nine_bits == [1, 1, 0, 1, 0, 1, 1, 1]:
    #=215
        letter.append('a')
    else:
        letter.append('')
print(letter)