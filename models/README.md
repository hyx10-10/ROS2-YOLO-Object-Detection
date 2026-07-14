# Models

This directory is used to store trained YOLO models.

## Recommended Files

```text
models/

├── yolov8n.pt
├── best.pt
├── best.onnx
└── best.engine
```

## Notes

- Do not upload large model files to GitHub.
- Download the official pretrained models from Ultralytics if needed.
- Place your trained models in this directory before running the detector.
- Update the model path in `config/yolo.yaml` if a different model is used.