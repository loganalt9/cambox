from src import Manager, HandDetector, MovingObjects, Picture
import cv2

IMAGE_PATH = "assests/red_circle.png"

if __name__ == "__main__":
    hand_det = HandDetector()

    picture = Picture(IMAGE_PATH, 200, 200)
    moving_objects = MovingObjects(picture)
    manager = Manager(hand_det, moving_objects, 1)

    manager.start()
