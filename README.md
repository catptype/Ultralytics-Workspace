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
    - License Plate Detection with Keypoints
    - License Plate Number Recognition

3. **Flexible and Modular Code**:
    - Easily adapt scripts for custom datasets.
    - Scalable for additional YOLO model tasks or applications

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

1. Clone the repository:
    ```bash
    git clone https://github.com/catptype/Ultralytics-Workspace.git
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Training a Model

1. **Copy the template file**
    Copy the `yolo11_template.py` file and edit the following parameters:
    - `TASK`: YOLO task type: ['classify', 'detect', 'pose', 'obb']
    - `MODEL_SIZE`: YOLO model size: ['n', 's', 'm', 'l', 'x']
    - `DATASET`: Name of the dataset in the 'datasets' directory
    - `AUGMENT_SELECTION`: Select augmentation preset (see `AUGMENTATION_PRESET` in [Augmentation.py](util/Augmentation.py) for options)
    - `APPLICATION`: Application name, used for naming the model in the 'runs' directory
    - `SEED`: Random seed value for reproducibility

2. **Run the training script**:
   Simply run the Python file from the previous step, and everything will execute automatically
   ```bash
   python yolo11_template.py
   ```

3. **View Training Results**:
   Check `runs/<TASK>/` directory for model performance metrics and visualizations.

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