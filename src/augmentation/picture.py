import cv2


class Picture:
    def __init__(self, img: str, width: int, height: int):
        self.img = cv2.imread(img)
        self.img = cv2.resize(self.img, (width, height))
        
        self.width = width
        self.height = height
        self.x = None
        self.y = None

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y
