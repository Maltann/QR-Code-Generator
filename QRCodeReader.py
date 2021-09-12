import cv2

print("---Starting reading the qrcode---")

d = cv2.QRCodeDetector()

val, points, qrcode = d.detectAndDecode(cv2.imread("qrcode.png"))

print(f"---The link of the QR Code is : {val} . See you next time !---")