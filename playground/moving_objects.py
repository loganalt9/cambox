import cv2
import numpy as np

IMAGE_PATH = "./assests/red_circle.png"
WEB_CAM_NUM = 1
PROPID_WIDTH = 3
PROPID_HEIGHT = 4

red_circle = cv2.imread(IMAGE_PATH)

x, y, w, h = 720, 100, 200, 200  # 720 is height
red_circle = cv2.resize(red_circle, (w, h))


def draw_circle(frame, x, y):
    frame[y : y + h, x : x + w] = red_circle
    return frame


stream = cv2.VideoCapture(WEB_CAM_NUM)
if not stream.isOpened():
    print("No stream")
    exit

width = int(stream.get(PROPID_WIDTH))
height = int(stream.get(PROPID_HEIGHT))

while True:
    ret, frame = stream.read()
    frame = cv2.flip(frame, 1)

    if not ret:
        print("No more stream")
        break

    if y + h == height:
        y = 0
    else:
        y += 5

    frame = draw_circle(frame, x, y)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord("q"):
        break

stream.release()
cv2.destroyAllWindows()
