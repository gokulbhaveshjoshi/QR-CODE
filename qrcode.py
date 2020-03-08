import pyqrcode
from pyqrcode import QRCode
link = "THE STYLISH CODER"
uri = pyqrcode.create(link)
uri.png("filename.png",scale=8)
print("Your qr code is ready")