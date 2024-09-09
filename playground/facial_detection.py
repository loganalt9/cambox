import cv2

# this will detect face smile nose
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


def detect_features(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(
            frame, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=5
        )
        face = frame[y : y + h, x : x + w]
        gray_face = gray[y : y + h, x : x + w]
        smiles = smile_cascade.detectMultiScale(gray_face, 2.5, minNeighbors=9)

        for xp, yp, wp, hp in smiles:
            face = cv2.rectangle(
                face, (xp, yp), (xp + wp, yp + hp), color=(255, 0, 0), thickness=5
            )

        eyes = eye_cascade.detectMultiScale(gray_face, 2.5, minNeighbors=7)

        for xp, yp, wp, hp in eyes:
            face = cv2.rectangle(
                face, (xp, yp), (xp + wp, yp + hp), color=(0, 0, 255), thickness=5
            )

    return frame


stream = cv2.VideoCapture(
    1
)  # zero for webcam (this opened up my phone for some reason) trying 1: 1 worked

if not stream.isOpened():
    print("No Stream")
    exit

# all of this is to save the video
fps = stream.get(cv2.CAP_PROP_FPS)
width = int(stream.get(3))
height = int(stream.get(4))
output = cv2.VideoWriter(
    "assests/4_stream.mp4",
    cv2.VideoWriter_fourcc("m", "p", "4", "v"),
    fps=fps,
    frameSize=(width, height),
)
# Infinite while loop while we display frame by frame
while True:
    ret, frame = stream.read()

    if not ret:
        print("No more stream")
        break

    frame = detect_features(frame)
    # output.write(frame) # for saving video
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord("q"):  # press q to quit, ord casts q to int with ASCII
        break

stream.release()  # Clean up: release webcam
cv2.destroyAllWindows()