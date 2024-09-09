import cv2
import numpy as np
from src.augmentation.picture import Picture


class MovingObjects:
    def __init__(self, img: Picture, width: int, height: int, speed=5):
        self.object = img
        self.speed = speed
        self.width = width
        self.height = height

    def place_object(
        self, x: int, y: int, frame: cv2.typing.MatLike
    ) -> cv2.typing.MatLike:
        frame[y : y + self.height, x : x + self.height] = self.img
        return frame
