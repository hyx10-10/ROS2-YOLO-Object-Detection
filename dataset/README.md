# Dataset

This directory is used to store datasets for training and evaluation.

## Recommended Structure

```text
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

## Notes

- Do not upload large datasets to GitHub.
- Only include sample images if necessary.
- Add `data.yaml` for dataset configuration.
- Keep the dataset structure consistent with the YOLO format.