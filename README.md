# ROS2-YOLO-Object-Detection

> A real-time object detection system based on ROS2 Humble, YOLOv8, and OpenCV.

<p align="center">

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-red)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

---

# Introduction

This project implements a real-time object detection system using **ROS2 Humble**, **YOLOv8**, and **OpenCV**. The detector subscribes to ROS2 image topics, performs object detection with the YOLOv8 model, and publishes annotated images back to ROS2 topics. It is suitable for robotics perception, object recognition, and related research applications.

---

# Features

- Developed with ROS2 Humble
- Real-time object detection using YOLOv8
- OpenCV-based image processing
- ROS Image and OpenCV image conversion via cv_bridge
- USB camera support
- Modular project structure
- Support for custom dataset training
- Easy deployment and extension

---

# Project Structure

```text
ROS2-YOLO-Object-Detection/

├── README.md
├── README_CN.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── package.xml
├── setup.py
├── setup.cfg

├── launch/
├── config/
├── my_yolo_detector/
├── msg/
├── docs/
├── assets/
├── models/
├── scripts/
├── examples/
├── test/
└── screenshots/
```

---

# System Architecture

```
USB Camera
      │
      ▼
/image_raw
      │
      ▼
YOLO Detector Node
      │
      ├────────────► YOLOv8 Inference
      │
      ▼
Annotated Image
      │
      ▼
/yolo/image_annotated
      │
      ▼
rqt_image_view
```

---

# Development Environment

| Software | Version |
|----------|---------|
| Ubuntu | 22.04 |
| ROS2 | Humble |
| Python | 3.10+ |
| OpenCV | 4.x |
| Ultralytics | Latest |
| NumPy | <2.0 |

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/YourName/ROS2-YOLO-Object-Detection.git
```

```bash
cd ROS2-YOLO-Object-Detection
```

---

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Install ROS2 Dependencies

```bash
sudo apt update
sudo apt install ros-humble-cv-bridge
sudo apt install ros-humble-image-transport
sudo apt install ros-humble-sensor-msgs
```

---

# Build the Workspace

```bash
cd ~/dev_ws
colcon build --symlink-install
source install/setup.bash
```

---

# Run the Project

## Terminal 1

Start the USB camera node.

```bash
ros2 run usb_cam usb_cam_node_exe
```

---

## Terminal 2

Launch the YOLO detector node.

```bash
ros2 run my_yolo_detector yolo_detector_node
```

---

## Terminal 3

Open the image viewer.

```bash
ros2 run rqt_image_view rqt_image_view
```

Select the topic:

```
/yolo/image_annotated
```

---

# Detection Pipeline

```
USB Camera

↓

ROS Image

↓

cv_bridge

↓

OpenCV Image

↓

YOLOv8

↓

Detection Result

↓

Annotated Image

↓

ROS Publisher
```

---

# Model Training

```bash
yolo detect train \
model=yolov8n.pt \
data=data.yaml \
imgsz=640 \
epochs=100 \
batch=16
```

---

# Model Inference

```bash
yolo detect predict \
model=best.pt \
source=0
```

---

# Project Components

| Module | Description |
|---------|-------------|
| Camera | Captures image data |
| ROS2 | Image communication |
| cv_bridge | Image format conversion |
| OpenCV | Image processing |
| YOLOv8 | Object detection |
| Publisher | Publishes annotated images |

---

# Demonstration

```
yolo_result.png
```

---

# Documentation

Detailed documentation is available in:

```
docs/

installation.md

training.md

deployment.md

architecture.md
```

---

# License

This project is released under the MIT License.

---
