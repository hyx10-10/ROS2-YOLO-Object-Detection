# Model Training

## Dataset Structure

```
dataset/

├── images/
│   ├── train/
│   ├── val/
│   └── test/
│
├── labels/
│   ├── train/
│   ├── val/
│   └── test/
│
└── data.yaml
```

---

## Train the Model

```bash
yolo detect train \
model=yolov8n.pt \
data=dataset/data.yaml \
imgsz=640 \
epochs=100 \
batch=16
```

---

## Training Parameters

| Parameter | Description |
|-----------|-------------|
| model | Pretrained YOLO model |
| data | Dataset configuration file |
| imgsz | Input image size |
| epochs | Number of training epochs |
| batch | Batch size |

---

## Training Results

After training, the generated files are stored in:

```text
runs/detect/train/
```

The best model is located at:

```text
runs/detect/train/weights/best.pt
```

---

## Export the Model

### ONNX

```bash
yolo export model=best.pt format=onnx
```

### TensorRT

```bash
yolo export model=best.pt format=engine
```