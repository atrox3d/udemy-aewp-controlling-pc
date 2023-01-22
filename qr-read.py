import cv2


image = cv2.imread('qr.png')

detector = cv2.QRCodeDetector()

url, coords, pixels = detector.detectAndDecode(image)

print(f'{url=}, {coords=}')
print(f'{pixels=}')
