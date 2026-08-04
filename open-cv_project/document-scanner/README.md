# 📄 Document Scanner using OpenCV

A Python-based Document Scanner built using OpenCV. This project detects the largest document in an image, extracts its boundaries, and applies a perspective transformation to generate a top-down scanned view.

---

## 🚀 Features

- Read and resize images
- Convert image to grayscale
- Apply Gaussian Blur for noise reduction
- Detect edges using Canny Edge Detection
- Perform Dilation and Erosion
- Detect external contours
- Identify the largest rectangular contour
- Apply Perspective Transformation
- Generate a scanned document image

---

## 🛠️ Technologies Used

- Python 3
- OpenCV
- NumPy

---

## 📂 Project Structure

```
document-scanner/
│
├── images/
│   └── input.jpeg
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🔄 Processing Pipeline

```
Input Image
      │
      ▼
Resize Image
      │
      ▼
Grayscale Conversion
      │
      ▼
Gaussian Blur
      │
      ▼
Canny Edge Detection
      │
      ▼
Dilation
      │
      ▼
Erosion
      │
      ▼
Find Contours
      │
      ▼
Detect Largest Quadrilateral
      │
      ▼
Reorder Corner Points
      │
      ▼
Perspective Transform
      │
      ▼
Scanned Document
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/noob-rishav/linux-practice.git
```

### Navigate to the project

```bash
cd linux-practice/open-cv_project/document-scanner
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the program

```bash
python3 main.py
```

---

## 📸 Demo

### Input Image

Place your input image inside the `images/` folder as:

```
images/input.jpeg
```

### Output

The program displays:

- Original Image
- Grayscale Image
- Blurred Image
- Edge Detection
- Dilated Image
- Eroded Image
- Detected Contours
- Final Scanned Document

---

## 📚 Concepts Practiced

This project helped me understand:

- Image Processing
- Computer Vision Basics
- Contour Detection
- Morphological Operations
- Perspective Transformation
- OpenCV Functions
- Python Functions and Modular Programming

---

## 🚧 Future Improvements

- Real-time webcam document scanner
- Automatic brightness enhancement
- Adaptive Thresholding
- Automatic document cropping
- PDF export
- Multi-page document scanning
- Better detection under different lighting conditions

---

## 📌 Learning Outcome

This project was built as part of my Computer Vision learning journey. The objective was to understand the complete classical computer vision pipeline before moving on to deep learning-based object detection (YOLO) for autonomous drone applications.

---

## 👨‍💻 Author

**Rishav Kumar Singh**

GitHub: https://github.com/noob-rishav

---

## ⭐ If you found this project interesting, consider giving the repository a star.