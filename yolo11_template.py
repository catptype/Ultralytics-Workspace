import os
from ultralytics import YOLO
from util.Config import TRAIN_CONFIG_PRESET
from util.Augmentation import AUGMENTATION_PRESET

TASK = 'classify'
DATASET = ''
AUGMENT_SELECTION = 'none'
APPLICATION = 'default'
SEED = 0

BASE_MODEL = {
    'classify': f'yolo11s-cls.pt',
    'detect': f'yolo11s.pt',
    'pose': f'yolo11n-pose.pt',
    'obb': f'yolo11n-obb.pt',
}

def main():
    # Print stdout
    print(f"Model: {BASE_MODEL[TASK]}")
    print(f"Dataset: {DATASET}")
    print(f"Augmentation configuration: {AUGMENT_SELECTION}")
    print("")

    # Initialize
    model = YOLO(BASE_MODEL[TASK])
    dataset = os.path.join(DATASET, 'data.yaml') if TASK in ['detect', 'pose', 'obb'] else DATASET
    config = TRAIN_CONFIG_PRESET[TASK]
    augmentation = AUGMENTATION_PRESET[AUGMENT_SELECTION]
    mixed_precision = 16 if config["amp"] else 32
    model_name = f"{BASE_MODEL[TASK].replace('.pt','')}_{APPLICATION}_SEED{SEED}_FP{mixed_precision}_V"

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
