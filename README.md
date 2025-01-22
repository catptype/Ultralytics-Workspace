# Ultralytic Workspace

This repository contains Python scripts and configurations for training YOLOv11 models using [Ultralytics](https://docs.ultralytics.com/) framework.
The workspace is designed to handle specific tasks like **object detection**, **classification**, **object bounding box (OBB)**, and **pose estimation**.
It is intended for various applications, including **license plate detection**, **license plate number recognition**, and more.

---

## 🔧 Features

1. **Task-Specific Training Configuration**:
    - Classification (`classify`)
    - Object Bounding Box (`obb`)
    - Object Detection (`detect`)
    - Pose Estimation (`pose`)

2. **Ready-to-use Augmentation Presets**:
    - License Plate Detection
    - OCR (Optical Character Recognition)
    - Other domain-specific applications.

3. **Flexible and Modular Code**:
    - Easily adapt scripts for custom datasets.
    - Scalable for additional YOLO model tasks or applications.

---

## 📂 Directory Structure

```plaintext
Ultralytic-Workspace/
├── util/
│   ├── Augmentation.py                 # Contains augmentation presets stored as Python dictionaries.
│   └── Config.py                       # Contains training configuration presets stored as Python dictionaries.
├── datasets/
│   ├── dataset_non_classification/     # Example datasets for detection, object bounding box (OBB), and pose estimation tasks.
│   │   ├── train/
│   │   │   ├── images/                 # Training images.
│   │   │   │   ├── train.jpg/
│   │   │   │   └── ...
│   │   │   └── labels/                 # Training labels in text format.
│   │   │       ├── train.txt/
│   │   │       └── ...
│   │   ├── valid/
│   │   │   ├── images/                 # Validation images.
│   │   │   │   ├── valid.jpg/
│   │   │   │   └── ...
│   │   │   └── labels/                 # Validation labels in text format.
│   │   │       ├── valid.txt/
│   │   │       └── ...
│   │   └── data.yaml                   # Configuration file for non-classification datasets.
│   ├── dataset_classify/               # Example dataset for classification tasks.
│   │   ├── train/
│   │   │   ├── class_name/             # Training images, grouped by class name.
│   │   │   └── ...
│   │   └── val/
│   │       ├── class_name/             # Validation images, grouped by class name.
│   │       └── ...
│   └── ...                             # Placeholder for additional datasets.
├── runs/
│   ├── detect/                         # Training results for detection tasks.
│   ├── classify/                       # Training results for classification tasks.
│   ├── obb/                            # Training results for object bounding box tasks.
│   └── pose/                           # Training results for pose estimation tasks.
├── yolo_template.py                    # Template script for YOLOv11 training.
└── README.md                           # Repository documentation.
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
  ```bash
  pip install -r requirements.txt
  ```

### Training a Model

1. **Set up the configuration file**:
   Update task-specific YAML files in the `configs/` directory to match your dataset paths, augmentation needs, and model settings.

2. **Run the training script**:
   For example, to train a license plate detection model:
   ```bash
   python scripts/train_detect.py --config configs/detect_license_plate.yaml
   ```

3. **View Training Results**:
   Check `results/` for model performance metrics and visualizations.

---

## 🖼️ Augmentation Presets

Custom augmentation presets ensure optimal performance for specific use cases:
- **License Plate Detection**: Focus on brightness and occlusion scenarios.
- **OCR**: Handle perspective and scaling changes to mimic real-world document scans.

To apply these presets, modify the configuration file accordingly.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).

---

## 🤝 Acknowledgments

Thanks to the [Ultralytics](https://ultralytics.com/) team for providing the YOLO framework, which serves as the backbone for this workspace.

---