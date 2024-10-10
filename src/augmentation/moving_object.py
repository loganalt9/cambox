import cv2
import numpy as np
import typing as t
from src.augmentation.picture import Picture
import sys

Frame: t.TypeAlias = cv2.typing.MatLike


class MovingObjects:
    def __init__(
        self, picture: Picture, speed=5
    ):
        self.speed = speed
        self.picture = picture
        self.on_screen = False

    def set_stream_values(self, width, height):  # TODO see manager.py line 24
        self.stream_width = width
        self.stream_height = height

    def handle_object(self, frame: Frame) -> Frame:
        if not self.on_screen:
            frame = self.place_object(frame)
            self.on_screen = True
            return frame
        
        if self.picture.get_y() + self.speed <= self.stream_height:
            frame = self.move_object(frame)
        else:
            self.reached_bottom()

        return frame

    def place_object(self, frame: Frame) -> Frame:
        start_x = np.random.randint(0, self.stream_width)
        start_y = 0

        self.picture.set_x(start_x)
        self.picture.set_y(start_y)

        frame[start_y : self.picture.height, start_x : start_x + self.picture.width] = (
            self.picture.img
        )
        return frame

    def move_object(self, frame: Frame) -> Frame:
        new_y = self.picture.get_y() + self.speed
        unchanged_x = self.picture.get_x()

        frame[new_y : new_y + self.picture.height, unchanged_x : unchanged_x + self.picture.width] = (
            self.picture.img
        )

        self.picture.set_y(new_y)

        return frame

    def reached_bottom(self):
        print("You lost, better luck next time.")
        sys.exit()
