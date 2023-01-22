import cv2

# grt webcam
video = cv2.VideoCapture(0)

# initialize qrcode detector
detector = cv2.QRCodeDetector()

while True:
    success, frame = video.read()
    if success:
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # try to decode
        url, coords, pixels = detector.detectAndDecode(frame)
        if url:
            print(f'{url=}')
            break
    else:
        break

