import cv2


def draw_detections(image, results):
    """
    Draw YOLO detection results on the image.

    Args:
        image: OpenCV image.
        results: YOLO inference results.

    Returns:
        Annotated image.
    """
    annotated_image = image.copy()

    for result in results:
        boxes = result.boxes

        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            confidence = float(box.conf[0])

            class_id = int(box.cls[0])

            label = result.names[class_id]

            text = f"{label} {confidence:.2f}"

            cv2.rectangle(
                annotated_image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2,
            )

            cv2.putText(
                annotated_image,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
            )

    return annotated_image