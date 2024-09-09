import cv2

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

    frame = cv2.resize(frame, (width, height))  # for saving video
    output.write(frame)  # for saving video
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord("q"):  # press q to quit, ord casts q to int with ASCII
        break

stream.release()  # Clean up: release webcam
cv2.destroyAllWindows()