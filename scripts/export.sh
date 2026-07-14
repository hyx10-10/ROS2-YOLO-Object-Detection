#!/bin/bash

echo "======================================"
echo " YOLOv8 Model Export"
echo "======================================"

echo "Exporting ONNX model..."

yolo export \
    model=models/best.pt \
    format=onnx

echo "ONNX model exported successfully."

echo "Exporting TensorRT engine..."

yolo export \
    model=models/best.pt \
    format=engine

echo "TensorRT engine exported successfully."