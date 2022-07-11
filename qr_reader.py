from tkinter import Image
from pyzbar.pyzbar import decode
from PIL import Image

# reading image
img=Image.open("myqr1.png")

content = decode(img)

print(content[0].data.decode())