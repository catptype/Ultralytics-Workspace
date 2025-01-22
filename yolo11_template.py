import os
from ultralytics import YOLO
from util.Config import TRAIN_CONFIG_PRESET
from util.Augmentation import AUGMENTATION_PRESET

# EDIT HERE
TASK = 'classify'           # YOLO task type: ['classify', 'detect', 'pose', 'obb']
MODEL_SIZE = 'n'            # YOLO model size: ['n', 's', 'm', 'l', 'x']
DATASET = ''                # Name of the dataset in the 'datasets' directory
AUGMENT_SELECTION = 'none'  # Select augmentation preset (see AUGMENTATION_PRESET for options)
APPLICATION = 'application' # Application name, used for naming the model in the 'runs' directory
SEED = 0                    # Random seed value for reproducibility

# -------------------------
BASE_MODEL = {
    'classify': f'yolo11{MODEL_SIZE}-cls.pt',
    'detect': f'yolo11{MODEL_SIZE}.pt',
    'pose': f'yolo11{MODEL_SIZE}-pose.pt',
    'obb': f'yolo11{MODEL_SIZE}-obb.pt',
}

def main():
    # Print stdout
    print(f"Model: {BASE_MODEL[TASK]}")
    print(f"Task: {TASK}")
    print(f"Dataset: {DATASET}")
    print(f"Augmentation: {AUGMENT_SELECTION}")
    print("")

    # Initialize
    model = YOLO(BASE_MODEL[TASK])
    dataset = os.path.join(DATASET, 'data.yaml') if TASK in ['detect', 'pose', 'obb'] else DATASET
    config = TRAIN_CONFIG_PRESET[TASK]
    augmentation = AUGMENTATION_PRESET[AUGMENT_SELECTION]
    mixed_precision = 16 if config["amp"] else 32
    model_name = f"{BASE_MODEL[TASK].replace('.pt','')}_{APPLICATION}_SEED{SEED}_FP{mixed_precision}_Ver"

    # Training
    model.train(
        data=dataset,
        name=model_name,
        exist_ok=False,
        seed=SEED,
        device=0,
        worker=1,
        **config,
        **augmentation,
    )

if __name__ == "__main__":
    main()
