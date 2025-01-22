# Read documents https://docs.ultralytics.com/modes/train/#augmentation-settings-and-hyperparameters

DEFAULT_AUGMENT = {
    "hsv_h": 0.015,
    "hsv_s": 0.7,
    "hsv_v": 0.4,
    "degrees": 0.0,
    "translate": 0.1,
    "scale": 0.5,
    "shear": 0.0,
    "perspective": 0.0,
    "flipud": 0.0,
    "fliplr": 0.5,
    "mosaic": 1.0,
    "erasing": 0.0,
}

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

LICENSE_PLATE_OCR = {
    "hsv_h": 0.0,
    "hsv_s": 0.05,
    "hsv_v": 0.05,
    "degrees": 5.0,
    "translate": 0.05,
    "scale": 0.1,
    "shear": 5.0,
    "perspective": 0.0001,
    "flipud": 0.0,
    "fliplr": 0.0,
    "mosaic": 0.0,
    "erasing": 0.05,
}

AUGMENTATION_PRESET = {
    "default": DEFAULT_AUGMENT,
    "none": NONE_AUGMENT,
    "basic": BASIC_AUGMENT,
    "license_plate_pose": LICENSE_PLATE_POSE,
    "license_plate_ocr": LICENSE_PLATE_OCR,
}
