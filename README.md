# Ultralytic Workspace

This repository contains Python scripts and configurations for training YOLOv11 models using [Ultralytics](https://docs.ultralytics.com/) framework.
The workspace is designed to handle specific tasks like **object detection**, **classification**, **oriented bounding box (OBB)**, and **pose estimation**.
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

Follow the steps below to set up and use the project.

#### **1. Clone the Repository**  
   Download the repository to your local machine:
   ```bash
   git clone https://github.com/catptype/Ultralytics-Workspace.git
   ```

#### **2. Install Dependencies**  
   Navigate to the project directory and install the required dependencies:
   ```bash
   cd anpr-training
   pip install -r requirements.txt
   ```
---

### Training a Model

#### **1. Prepare the Training Script**

1. **Start with the Template**  
   Use the provided [template.py](template.py) file as a starting point for your training script.

2. **Edit the Parameters**  
   Customize the following parameters in the script based on your requirements:
    - **`TASK`**: The YOLO task type. Choose one of the following:
        - `'classify'` for image classification
        - `'detect'` for object detection
        - `'pose'` for pose estimation
        - `'obb'` for oriented bounding box
    - **`MODEL_SIZE`**: Specify the YOLO model size: `'n'`, `'s'`, `'m'`, `'l'`, `'x'`.
    - **`DATASET`**: The name of the dataset in the [datasets](datasets) directory.
    - **`AUGMENT_SELECTION`**: Choose an augmentation preset (options available in `AUGMENTATION_PRESET` in [Augmentation.py](util/Augmentation.py)).
    - **`APPLICATION`**: The application name, used to name the model and save results in the [runs](runs) directory.
    - **`SEED`**: Set a random seed value to ensure reproducibility.

3. **Adjust Additional Training Arguments**  
   You can modify the following optional parameters in the `model.train()` method for enhanced performance:
   - **`device`**: Specify the device to use (e.g., `0` for GPU or `cpu`).
   - **`workers`**: Set the number of worker threads for data loading. Useful for better hardware or multiple GPUs.

   > **Note**: For more details on training settings, refer to Ultralytics's [documentation](https://docs.ultralytics.com/modes/train/#train-settings).

#### **2. Prepare the Dataset**
1. Organize your dataset following the task-specific directory structure.
2. Use annotation tools to label your dataset:
    - [**labelImg**](https://github.com/HumanSignal/labelImg): Suitable for `detect` tasks.
   - [**labelme**](https://github.com/wkentaro/labelme): Suitable for `detect` and `pose` tasks.
   - [**X-AnyLabeling**](https://github.com/CVHub520/X-AnyLabeling): Suitable for `detect` and `pose` tasks.

   > **Note 1**: `labelImg` does not support non-English label names and will crash if such labels are used.  

   > **Note 2**: `labelme` annotations are saved as **JSON** files. You will need to write a Python script to convert these annotations into YOLO-compatible `.txt` format.

   > **Note 3**: `X-AnyLabeling` is more **complex tool** but offers excellent label management. it also can directly export annotations in YOLO-compatible `.txt` format.

3. For tasks other than classification, include a `data.yaml` configuration file in your dataset with the following structure:
    ```yaml
    path: /path/to/anpr-training/datasets/dataset_name
    train: ./train/images
    val: ./valid/images
    test: ./test/images
    ```
    > **Note**: See an example configuration file [here](datasets/example_detect_pose/data.yaml).

#### **3. Run the Training Script**
Run the Python script you prepared in Step 1 to start training:
```bash
python edited_template.py
```

#### **4. View Training Results**
After training, explore the [runs](runs) directory for:
  - Model performance metrics (e.g., accuracy, loss curves).
  - Visualizations of the training process.
  - Model weight files:
    - `best.pt`: The best-performing model checkpoint.
    - `last.pt`: The final model checkpoint.

---

### 🔧 Training Configuration Presets

All training configuration presets are located in [Config.py](util/Config.py), covering the following tasks:
- **Classification** (`classify`)
- **Oriented Bounding Box** (`obb`)
- **Object Detection** (`detect`)
- **Pose Estimation** (`pose`)

#### Key Parameters:
- **`imgsz`**: Target image size for training.
- **`batch`**: Batch size.
- **`lr0`**: Initial learning rate.
- **`lrf`**: Final learning rate as a fraction of the initial rate.
- **`dropout`**: Dropout rate for regularization (specific to **classification** tasks).
- **`epochs`**: Total number of training epochs.
- **`warmup_epochs`**: Number of epochs for learning rate warmup.
- **`patience`**: Number of epochs to wait without improvement in validation metrics before early stopping.
- **`cache`**: Enables caching of dataset images in memory or on disk.
- **`amp`**: Enables Automatic Mixed Precision (AMP) training.
- **`time`**: Maximum training time (in hours).

> **Note 1**: For more details, refer to Ultralytics's [documentation](https://docs.ultralytics.com/modes/train/#train-settings).  

> **Note 2**: To create a custom training configuration, declare a new constant variable as a Python dictionary and save it in `TRAIN_CONFIG_PRESET`.

---

### 🖼️ Augmentation Presets

Predefined augmentation presets are available in [Augmentation.py](util/Augmentation.py).

#### Key Augmentation Parameters:
- **`hsv_h`**: Adjusts the **hue** of the image by a fraction.
- **`hsv_s`**: Adjusts the **saturation** of the image by a fraction.
- **`hsv_v`**: Adjusts the **value (brightness)** of the image by a fraction.
- **`degrees`**: Applies random rotation to the image.
- **`translate`**: Translates the image horizontally and vertically.
- **`scale`**: Scales the image by a gain factor.
- **`shear`**: Shears the image, simulating a tilted view.
- **`perspective`**: Applies a random 3D perspective transformation.
- **`flipud`**: Flips the image upside down with a specified probability.
- **`fliplr`**: Flips the image left to right with a specified probability.
- **`mosaic`**: Combines four training images into one.
- **`erasing`**: Randomly erases a portion of the image during **classification** training.

> **Note 1**: For more details, refer to Ultralytics's [documentation](https://docs.ultralytics.com/modes/train/#augmentation-settings-and-hyperparameters).  

> **Note 2**: To create a custom augmentation preset, declare a new constant variable as a Python dictionary and save it in `AUGMENTATION_PRESET`.

## 🛠️ Troubleshooting

### Issue: `RuntimeError: Dataset 'dataset_name/data.yaml' does not exist`
This error typically occurs due to an **incorrect global configuration** in the settings file. To resolve this issue, follow these steps:

1. **Locate the Configuration File**  
   Run the following command to find the directory path of the settings file:
   ```bash
   yolo settings
   ```
   This will display the location of the configuration file, which is usually found at: `../Ultralytics/settings.json`

2. **Update the `settings.json` File**  
    Open the `settings.json` file and update the value of the `datasets_dir` key to point to the **project's root directory**. For example:
    ```json
    {
        ...
        "datasets_dir": "path\\to\\anpr-training",
        ...
    }
    ```

## 📄 License

This repository is licensed under the [MIT License](LICENSE).


## 🤝 Acknowledgments

Thanks to the [Ultralytics](https://ultralytics.com/) for providing the YOLO framework, which serves as the backbone for this workspace.
