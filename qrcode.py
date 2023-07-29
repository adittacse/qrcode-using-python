# pip install pypng
# pip install pyqrcode

from pyqrcode import QRCode

information = ["Aditta Chakraborty\n", "Dhaka, Bangladesh\n", "adittasarma@gmail.com\n"]

for i in information:
    myQRCode = QRCode(i)
    myQRCode.png("myQRCode2.png", scale=12)
    myQRCode.show()
