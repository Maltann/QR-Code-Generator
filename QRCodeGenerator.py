import qrcode

link = str = input("---write the link for the QR Code---\n")
qrCodeColor = str = input("---write the color you want for the QR Code---\n")
qrCodeComplexity = int = input("---select the QR Code complexity (between 1 and 40)---\n")
boxSize = int = input("---select the QR Code size (between 1 and 40)---\n")
borderSize = int = input("---select the borders size of the QR Code (between 1 and 40)---\n")

qr = qrcode.QRCode(
    version=qrCodeComplexity,
    box_size=boxSize,
    border=borderSize,
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color=qrCodeColor, back_color="white")
img.save('qrcode.png')
print('QR Code saved as "qrcode.png" ! See you next time !')