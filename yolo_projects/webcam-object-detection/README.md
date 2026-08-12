# YOLOv8 Real-Time Webcam Person Detection

A real-time computer vision project using **YOLOv8, Ultralytics, Python, and OpenCV** to detect people through a webcam and determine their position and approximate relative distance from the camera.

This project is part of my learning journey toward **Computer Vision, AI, Robotics, and Autonomous Drone Navigation**.

## Features

- Real-time webcam video processing
- YOLOv8 object detection
- Person-only detection
- Confidence score filtering
- Bounding box visualization
- Person center calculation
- Horizontal position detection
- Vertical position detection
- Approximate distance estimation
- FPS calculation
- Target lost detection
- Real-time tracking state

## How It Works

The system follows this pipeline:

```text
Webcam
   ↓
Capture Frame
   ↓
YOLOv8 Detection
   ↓
Filter Person
   ↓
Confidence Filtering
   ↓
Bounding Box
   ↓
Calculate Person Center
   ↓
Calculate Position Error
   ↓
Horizontal Direction
   ↓
Vertical Direction
   ↓
Distance Estimate
   ↓
Tracking State


---

## Author

**Rishav Kumar Singh**

Computer Science & Design Engineering Student

Interested in:

- Computer Vision
- Artificial Intelligence
- Robotics
- Autonomous Drones