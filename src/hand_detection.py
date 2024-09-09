import cv2
import mediapipe as mp


class HandDetector:
    def __init__(
        self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5
    ):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode,
            self.maxHands,
            self.modelComplex,
            self.detectionCon,
            self.trackCon,
        )
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, frame):
        frame = cv2.flip(frame, 1)
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(
                    frame, handlms, self.mpHands.HAND_CONNECTIONS
                )

        return frame

    def findPosition(self, frame, handNum=0):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNum]
        else:
            return

        for id, lm in enumerate(myHand.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmlist.append([id, cx, cy])

            cv2.circle(frame, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        return lmlist
