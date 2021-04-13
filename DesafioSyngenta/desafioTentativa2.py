from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography

output_path = "C:\\Users\\carol\\OneDrive\\Documents\\Programação\\DesafioSyngenta\\HireMe.jpg"
# read secret text from image
secret_text = Steganography.decode(output_path)
print(secret_text)
#Tentativa 2 usando pip install steganography fonte: https://pypi.org/project/steganography/
      
