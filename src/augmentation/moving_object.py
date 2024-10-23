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

    def handle_object(self, frame: Frame, hand_pos: list) -> Frame:
        if not self.on_screen:
            frame = self.place_object(frame)
            self.on_screen = True
            return frame
        
        if hand_pos is not None and self.detect_collision(hand_pos):
            self.place_object(frame)
            return frame
        
        if self.picture.get_y() + self.speed <= self.stream_height:
            frame = self.move_object(frame)
        else:
            self.reached_bottom(hand_pos)


        return frame

    def place_object(self, frame: Frame) -> Frame:
        start_x = np.random.randint(0, self.stream_width - self.picture.width)
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

    def reached_bottom(self) -> None:
        print("You lost, better luck next time.")
        sys.exit()

    def detect_collision(self, hand_pos) -> bool:
        picture_range_x = (self.picture.get_x(), self.picture.get_x()+self.picture.width)
        picture_range_y = (self.picture.get_y(), self.picture.get_y()+self.picture.height)

        for pos in hand_pos:
            if ((picture_range_x[0] <= pos[1] and pos[1] <= picture_range_x[1]) 
                and (picture_range_y[0] <= pos[2] and pos[2] <= picture_range_y[1])):
                return True
            
        return False
