import cv2
import numpy as np

from flask import Flask, render_template, Response

DEBUG = False


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def get_frame(video):
    while True:
        success: bool
        frame: np.ndarray
        success, frame = video.read()
        dprint(f'{success=}, {frame.shape=}')

        success, encoded_image = cv2.imencode('.jpg', frame)
        dprint(f'{success=}, {encoded_image=}')

        byte_frame = encoded_image.tobytes()
        dprint(f'{byte_frame=}')

        header = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n'
        footer = b'\r\n'

        output = header + byte_frame + footer
        yield output


video = cv2.VideoCapture(0)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(get_frame(video), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
    # video.release()
