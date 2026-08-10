from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolov8n.pt")

# Run inference
results = model("images/input.jpg")

# Get first result
result = results[0]

img = result.orig_img.copy()   

for box in result.boxes:

    class_id = int(box.cls[0])
    class_name = result.names[class_id]
    confidence = float(box.conf[0])

    if class_name != "person":
        continue

    if confidence < 0.50:
        continue

    label = f"{class_name} {confidence:.2f}"

    x1, y1, x2, y2 = box.xyxy[0]

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    print(f"Object      : {class_name}")
    print(f"Confidence  : {confidence:.2f}")
    print(f"Coordinates : ({x1:.1f}, {y1:.1f}) -> ({x2:.1f}, {y2:.1f})")
    print(f"Center      : ({center_x:.1f}, {center_y:.1f})")
    print("-------------------------------------")

    cv2.rectangle(
        img,
        (int(x1), int(y1)),
        (int(x2), int(y2)),
        (0,255,0),
        2
    )
    cv2.putText(
    img,
    label,
    (int(x1), int(y1) - 10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.6,
    (0, 255, 0),
    2
    )

    cv2.circle(
    img,
    (int(center_x), int(center_y)),
    5,
    (0, 0, 255),
    -1
    )


# Show image
cv2.imshow("Detection", img)

# Save image
cv2.imwrite("output/result.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()