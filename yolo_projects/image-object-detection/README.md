# 📄 YOLOv8 Image Object Detection

A beginner-friendly computer vision project that performs **real-time object detection on images** using **YOLOv8** and **OpenCV**.

This project demonstrates how to:
- Load a pretrained YOLOv8 model
- Detect objects in an image
- Extract object information
- Draw custom bounding boxes
- Display class names and confidence scores
- Calculate object center coordinates
- Filter detections based on class and confidence

---

## 🚀 Features

- ✅ YOLOv8 Nano pretrained model
- ✅ Object detection on images
- ✅ Custom bounding boxes using OpenCV
- ✅ Class name extraction
- ✅ Confidence score extraction
- ✅ Bounding box coordinate extraction
- ✅ Object center calculation
- ✅ Detection filtering (by class and confidence)
- ✅ Save annotated output image

---

## 📂 Project Structure

```
image-object-detection/
│
├── images/
│   └── input.jpg
│
├── output/
│   └── result.jpg
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- Ultralytics YOLOv8
- PyTorch

---

## ⚙ Installation

### 1. Clone the repository

```bash
git clone https://github.com/noob-rishav/linux-practice.git
```

---

### 2. Navigate to the project

```bash
cd linux\ practice/yolo_projects/image-object-detection
```

---

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

---

### 4. Activate the virtual environment

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

Place your image inside the **images** folder.

Example:

```
images/
    input.jpg
```

Run:

```bash
python3 main.py
```

The detected image will be displayed and saved inside:

```
output/result.jpg
```

---

## 🧠 Workflow

```
Input Image
      │
      ▼
YOLOv8 Model
      │
      ▼
Object Detection
      │
      ▼
Extract:
• Class Name
• Confidence
• Bounding Box
• Object Center
      │
      ▼
OpenCV Visualization
      │
      ▼
Output Image
```

---

## 📌 Concepts Learned

During this project, the following concepts were implemented:

- Loading pretrained YOLOv8 models
- Running inference
- Understanding the Results object
- Working with the Boxes object
- Extracting class IDs
- Mapping class IDs to class names
- Confidence score extraction
- Bounding box coordinates (XYXY)
- Object center calculation
- Filtering detections
- Drawing custom bounding boxes
- Drawing custom labels
- Drawing object center points
- Saving processed images

---

## 📷 Sample Output

**Input Image**

```
images/input.jpg
```

**Output Image**

```
output/result.jpg
```

The output image contains:

- Green bounding boxes
- Class names
- Confidence scores
- Center point of detected objects

---

## 📈 Future Improvements

- Real-time webcam detection
- Video object detection
- Object tracking
- Custom dataset training
- Drone camera integration
- ROS2 integration
- PX4 / MAVLink integration

---

## 👨‍💻 Author

**Rishav Kumar Singh**

Computer Science & Design Engineering Student

Interested in:

- Computer Vision
- Artificial Intelligence
- Robotics
- Autonomous Drones
- YOLO
- OpenCV

---

## ⭐ Acknowledgements

- Ultralytics YOLOv8
- OpenCV
- PyTorch