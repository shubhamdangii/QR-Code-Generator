import pyqrcode

content = "this is my content"

url = pyqrcode.create(content)

url.png("myqr.png",scale=5)

print("QR code is generated successfully")