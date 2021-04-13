from PIL import Image, ImageEnhance

image = Image.open('HireMe.jpg')

red, green, blue = image.split()
count = 0
factor = 10.5
enhancer = ImageEnhance.Contrast(image)
im_output = enhancer.enhance(factor)
im_output.save('imagemContrasteMaior.png')
      
print(im_output)

#Tentativa 1: tentativa de aumentar o contraste entre os pixels que não eram pretos e ver se havia uma imagem escondida. Tentativa falha.
    

