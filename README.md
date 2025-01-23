# Ultralytic Workspace

This repository contains Python scripts and configurations for training YOLOv11 models using [Ultralytics](https://docs.ultralytics.com/) framework.
The workspace is designed to handle specific tasks like **object detection**, **classification**, **object bounding box (OBB)**, and **pose estimation**.
It is intended for various applications, including **license plate detection**, **license plate number recognition**, and more.

## ✨ Features

1. **Task-Specific Training Configurations**:
    - Includes predefined configurations for different tasks such as classification, object detection, bounding box, and pose estimation.

2. **Ready-to-use Augmentation Presets**:
    - License Plate Detection with Keypoints
    - License Plate Number Recognition

3. **Flexible and Modular Code**:
    - Easily adapt scripts for custom datasets.
    - Scalable for additional YOLO model tasks or applications

## 📂 Directory Structure

```plaintext
Ultralytic-Workspace/
├── util/
│   ├── Augmentation.py                 # Augmentation presets as Python dictionaries.
│   └── Config.py                       # Training configuration presets as Python dictionaries.
├── datasets/
│   ├── dataset_non_classification/     # Example datasets for non-classification tasks.
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

1. **Copy the template file**:   
    Copy the [yolo11_template.py](yolo11_template.py) file or edit following parameters:
    - `TASK`: YOLO task type: `'classify'`, `'detect'`, `'pose'`, `'obb'`
    - `MODEL_SIZE`: YOLO model size: `'n'`, `'s'`, `'m'`, `'l'`, `'x'`
    - `DATASET`: Name of the dataset in the 'datasets' directory
    - `AUGMENT_SELECTION`: Select augmentation preset (see `AUGMENTATION_PRESET` in [Augmentation.py](util/Augmentation.py) for options)
    - `APPLICATION`: Application name, used for naming the model in the 'runs' directory
    - `SEED`: Random seed value for reproducibility

2. **Dataset preparation**:   
    Organize your dataset according to the task-specific directory structure in the [datasets](datasets) directory.

3. **Run the training script**:   
   Simply run the Python file from the previous step, and everything will execute automatically:
   ```bash
   python yolo11_template.py
   ```

4. **View Training Results**:   
   Check `runs/<TASK>/` directory for model performance metrics and visualizations.

## 🔧 Training Config Presets

All training configuration presets are located in [Config.py](util/Config.py), covering the following tasks:
- Classification (`classify`)
- Object Bounding Box (`obb`)
- Object Detection (`detect`)
- Pose Estimation (`pose`)

## 🖼️ Augmentation Presets

This repository provides ready-to-use augmentation presets in [Augmentation.py](util/Augmentation.py) for specific use cases:  
- **No Augmentation**: Disables all augmentation techniques.  
- **Basic Augmentation**: Applies slight transformations, including rotation, random horizontal flipping, and partial image erasing.  
- **License Plate Detection**: Emphasizes brightness adjustments and orientation changes with minor transformations.  
- **License Plate Number Recognition**: Similar to the License Plate Detection preset but with reduced hyperparameter values.

## 🛠️ Troubleshooting

If you encounter the error:  
`RuntimeError: Dataset 'dataset_name/data.yaml' does not exist`  
this usually occurs due to a misconfiguration in the settings file.

To resolve this issue:

1. Locate the configuration file by running the following command:  
   ```bash
   yolo setting
   ```
   This command returns the directory path to the configuration file located at `../Ultralytics/settings.json`.

2. Open the `settings.json` file and update the value of the `datasets_dir` key to the correct directory path.

## 📄 License

This repository is licensed under the [MIT License](LICENSE).


## 🤝 Acknowledgments

Thanks to the [Ultralytics](https://ultralytics.com/) team for providing the YOLO framework, which serves as the backbone for this workspace.












Here’s the revised README.md with improved clarity, corrected grammar, and an emoji added to the "Troubleshooting" section:

```markdown
## 🖼️ Augmentation Presets

This repository provides ready-to-use augmentation presets in [Augmentation.py](util/Augmentation.py) for specific use cases:  
- **No Augmentation**: Disables all augmentation techniques.  
- **Basic Augmentation**: Applies slight transformations, including rotation, random horizontal flipping, and partial image erasing.  
- **License Plate Detection**: Focuses on brightness adjustments and orientation changes with minor transformations.  
- **License Plate Number Recognition**: Similar to the License Plate Detection preset but with reduced hyperparameter values.


```

Let me know if you need any further modifications!