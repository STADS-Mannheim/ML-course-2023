import cv2
import os
import uuid
import numpy as np
from matplotlib import pyplot as plt

POS_PATH = os.path.join("data", "positive")
NEG_PATH = os.path.join("data", "negative")
ANC_PATH = os.path.join("data", "anchor")


def read_image(path: str) -> np.ndarray:
    img = plt.imread(path)
    return cv2.resize(img, (105,105)) / 255

def resize_images(dir_path: str, size: int) -> None:
    for file in os.listdir(dir_path):
        if file.endswith(".jpg"):
            file_path = os.path.join(dir_path, file)
            img = plt.imread(file_path)
            img = cv2.resize(img, (size,size))
            cv2.imwrite(file_path, img)

if __name__ == "main":
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.flip(frame[150:150+400, 475:475+400, :], 1)
        frame = cv2.resize(frame, (250, 250))
        cv2.imshow("Image Collection", frame)

        # Collect anchors
        if cv2.waitKey(1) & 0XFF == ord("a"):
            imgname = os.path.join(ANC_PATH, f"{uuid.uuid1()}.jpg")
            cv2.imwrite(imgname, frame)

        if cv2.waitKey(1) & 0XFF == ord("p"):
            imgname = os.path.join(POS_PATH, f"{uuid.uuid1()}.jpg")
            cv2.imwrite(imgname, frame)

        if cv2.waitKey(1) & 0XFF == ord("q"):
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            break

    print(frame.shape)

    cap.release()
    cv2.destroyAllWindows()