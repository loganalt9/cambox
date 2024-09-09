import cv2

class Picture:
    def __init__(self, img: str, x: int, y: int):
        self.img = cv2.imread(img)
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y
