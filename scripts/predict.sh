#!/bin/bash

echo "======================================"
echo " YOLOv8 Prediction"
echo "======================================"

yolo detect predict \
    model=models/yolov8n.pt \
    source=0

echo "Prediction completed."