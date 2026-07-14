# ROS2-YOLO-Object-Detection

> 基于 ROS2 Humble、YOLOv8 和 OpenCV 的实时目标检测系统。

<p align="center">

![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-red)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

---

# 项目简介

本项目基于 ROS2 Humble、YOLOv8 和 OpenCV 构建了一个实时目标检测系统。系统通过订阅 ROS2 相机图像话题获取图像数据，利用 YOLOv8 模型完成目标检测，并将检测结果以带标注图像的形式重新发布到 ROS2 网络中，可直接应用于机器人视觉感知、目标识别及相关研究。

---

# 项目特点

- 基于 ROS2 Humble 开发
- 基于 YOLOv8 实时目标检测
- OpenCV 图像处理
- 使用 cv_bridge 实现 ROS 图像与 OpenCV 图像转换
- 支持 USB 摄像头
- 模块化工程结构
- 支持自定义数据集训练
- 易于部署与扩展

---

# 项目目录

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

# 系统架构

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

# 开发环境

| 软件 | 版本 |
|------|------|
| Ubuntu | 22.04 |
| ROS2 | Humble |
| Python | 3.10+ |
| OpenCV | 4.x |
| Ultralytics | Latest |
| NumPy | <2.0 |

---

# 安装

## 克隆仓库

```bash
git clone https://github.com/YourName/ROS2-YOLO-Object-Detection.git
```

```bash
cd ROS2-YOLO-Object-Detection
```

---

## 安装 Python 依赖

```bash
pip install -r requirements.txt
```

---

## 安装 ROS2 依赖

```bash
sudo apt update
sudo apt install ros-humble-cv-bridge
sudo apt install ros-humble-image-transport
sudo apt install ros-humble-sensor-msgs
```

---

# 编译工作空间

```bash
cd ~/dev_ws
colcon build --symlink-install
source install/setup.bash
```

---

# 运行项目

## 终端一

启动 USB 摄像头

```bash
ros2 run usb_cam usb_cam_node_exe
```

---

## 终端二

启动目标检测节点

```bash
ros2 run my_yolo_detector yolo_detector_node
```

---

## 终端三

启动图像查看工具

```bash
ros2 run rqt_image_view rqt_image_view
```

选择话题：

```
/yolo/image_annotated
```

---

# 检测流程

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

---

# 模型训练

```bash
yolo detect train \
model=yolov8n.pt \
data=data.yaml \
imgsz=640 \
epochs=100 \
batch=16
```

---

# 模型预测

```bash
yolo detect predict \
model=best.pt \
source=0
```

---

# 项目组成

| 模块 | 功能 |
|------|------|
| Camera | 获取图像数据 |
| ROS2 | 图像通信 |
| cv_bridge | 图像格式转换 |
| OpenCV | 图像处理 |
| YOLOv8 | 目标检测 |
| Publisher | 发布检测结果 |

---

# 运行效果
```
yolo_result.png
```

# 文档

详细文档位于：

```
docs/

installation.md

training.md

deployment.md

architecture.md
```

---

# License

本项目采用 MIT License 开源协议。

---
