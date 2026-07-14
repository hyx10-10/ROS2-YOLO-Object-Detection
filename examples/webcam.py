import cv2
from ultralytics import YOLO


def main():
    model = YOLO("../models/yolov8n.pt")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Failed to open camera.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame, verbose=False)

        annotated = results[0].plot()

        cv2.imshow("YOLOv8 Webcam Demo", annotated)

        key = cv2.waitKey(1)

        if key == 27 or key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()