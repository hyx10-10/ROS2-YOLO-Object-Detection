#!/bin/bash

echo "======================================"
echo " YOLOv8 Training"
echo "======================================"

yolo detect train \
    model=yolov8n.pt \
    data=dataset/data.yaml \
    imgsz=640 \
    epochs=100 \
    batch=16

echo "Training completed."