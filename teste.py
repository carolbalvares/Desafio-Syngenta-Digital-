from PIL import Image

image = Image.open('HireMe.jpg')

red, green, blue = image.split()


new_image = Image.merge("RGB", (red, blue, green))
new_image.save('new_image.jpg')

print(new_image.mode) # Output: RGB