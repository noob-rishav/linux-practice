from ultralytics import YOLO
import cv2
import time

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)
prev_time = 0

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to read camera")
        break

    results = model(frame)
    result = results[0]

    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    img = frame.copy()

    person_found = False
    tracking_state = "TARGET LOST"

    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = result.names[class_id]
        confidence = float(box.conf[0])

        if class_name != "person":
            continue

        if confidence < 0.50:
            continue

        person_found = True

        x1, y1, x2, y2 = box.xyxy[0]

        box_width = x2 - x1
        box_height = y2 - y1

        if box_height < 200:
            distance = "FAR"
        elif box_height > 400:
            distance = "CLOSE"
        else:
            distance = "GOOD"

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        frame_height, frame_width = frame.shape[:2]

        image_center_x = frame_width / 2
        image_center_y = frame_height / 2

        error_x = center_x - image_center_x
        error_y = center_y - image_center_y

        if error_x > 50:
            horizontal_direction = "RIGHT"
        elif error_x < -50:
            horizontal_direction = "LEFT"
        else:
            horizontal_direction = "CENTER"

        if error_y > 50:
            vertical_direction = "DOWN"
        elif error_y < -50:
            vertical_direction = "UP"
        else:
            vertical_direction = "CENTER"

        tracking_state = f"{horizontal_direction} | {vertical_direction} | {distance}"

        cv2.rectangle(
            img,
            (int(x1), int(y1)),
            (int(x2), int(y2)),
            (0, 0, 255),
            2
        )

        label = f"{class_name} {confidence:.2f}"

        cv2.putText(
            img,
            label,
            (int(x1), int(y1) - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

        cv2.circle(
            img,
            (int(center_x), int(center_y)),
            5,
            (0, 0, 255),
            -1
        )

    cv2.putText(
        img,
        f"FPS: {int(fps)}",
        (40, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    cv2.putText(
        img,
        tracking_state,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("YOLO Webcam Detection", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

