# Read documents https://docs.ultralytics.com/modes/train/#augmentation-settings-and-hyperparameters

NONE_AUGMENT = {
    "hsv_h": 0.0,
    "hsv_s": 0.0,
    "hsv_v": 0.0,
    "degrees": 0.0,
    "translate": 0.0,
    "scale": 0.0,
    "shear": 0.0,
    "perspective": 0.0,
    "flipud": 0.0,
    "fliplr": 0.0,
    "mosaic": 0.0,
    "erasing": 0.0,
}

BASIC_AUGMENT = {
    "hsv_h": 0.0,
    "hsv_s": 0.0,
    "hsv_v": 0.0,
    "degrees": 3.0,
    "translate": 0.05,
    "scale": 0.05,
    "shear": 0.0,
    "perspective": 0.0,
    "flipud": 0.0,
    "fliplr": 0.5,
    "mosaic": 0.0,
    "erasing": 0.05,
}

LICENSE_PLATE_POSE = {
    "hsv_h": 0.05,
    "hsv_s": 0.05,
    "hsv_v": 0.05,
    "degrees": 10.0,
    "translate": 0.1,
    "scale": 0.05,
    "shear": 5.0,
    "perspective": 0.0001,
    "flipud": 0.0,
    "fliplr": 0.25,
    "mosaic": 0.0,
    "erasing": 0.05,
}

AUGMENTATION_PRESET = {
    "none": NONE_AUGMENT,
    "basic": BASIC_AUGMENT,
    "license_plate_pose": LICENSE_PLATE_POSE,
}