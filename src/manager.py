import cv2

from src.hand_detection import HandDetector
from src.augmentation.picture import Picture
from src.augmentation.moving_object import MovingObjects

# My personal stream for my mac webcam. May be different on different devices
STREAM = 1


class Manager:
    def __init__(
        self, handDetection: HandDetector, movingObjects: MovingObjects, difficulty: int | None = 5
    ) -> None:
        self.handDetector = handDetection
        self.difficulty = difficulty
        self.movingObjects = movingObjects

    def start(self):
        stream = cv2.VideoCapture(STREAM)
        if not stream.isOpened():
            raise ConnectionError("Stream failed to open")

        width = int(stream.get(3))
        height = int(stream.get(4))

        self.movingObjects.set_stream_values(
            width, height
        )  # TODO: This is a terrible way of implementing this fix this

        while True:
            ret, frame = stream.read()
            if not ret:
                print("No more stream")
                exit

            frame = cv2.resize(frame, (width, height))

            frame = self.handDetector.findHands(frame)
            frame = self.movingObjects.handle_object(frame)
            hand_pos = self.handDetector.findPosition(frame)

            cv2.imshow("Webcam", frame)
            if cv2.waitKey(1) == ord("q"):
                break

        stream.release()
        cv2.destroyAllWindows()
