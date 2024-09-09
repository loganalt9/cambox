import cv2

from src.hand_detection import HandDetector
from src.augmentation.picture import Picture
from src.augmentation.moving_object import MovingObjects

class Manager:
    def __init__(self, handDetection: HandDetector, img: str, difficulty: int) -> None:
        self.handDetector = handDetection
        self.img = img
        self.difficulty = difficulty
    
    def start(self):
        stream = cv2.VideoCapture(1)
        if not stream.isOpened():
            raise ConnectionError("Stream failed to open")
        
        width = int(stream.get(3))
        height = int(stream.get(4))

        while True:
            ret, frame = stream.read()
            if not ret:
                print("No more stream")
                exit
            
            frame = cv2.resize(frame, (width, height))

            frame = self.handDetector.findHands(frame)
            hand_pos = self.handDetector.findPosition(frame)

            

            cv2.imshow("Webcam", frame)
            if cv2.waitKey(1) == ord("q"):
                break
        
        stream.release()
        cv2.destroyAllWindows()
    
