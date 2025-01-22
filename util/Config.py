# Read documents https://docs.ultralytics.com/modes/train/#train-settings

TIMEOUT = 12.0 # Default None
WARMUP = 5.0 # Default 3.0

CLASSIFY_CONFIG = {
    "imgsz": 320,
    "batch": 32,
    "lr0": 0.0005, # Default 0.01
    "lrf": 0.01, # Default 0.01 
    "dropout": 0.0, # Default 0.0
    "epochs": 300, # Default 100
    "warmup_epochs": WARMUP, # Default 3.0
    "patience": 10, 
    "cache": False, # Set True if train with super computer
    "amp": True, # Mixed precision
    "time": TIMEOUT, # Default None
}

DETECT_CONFIG = {
    "imgsz": 640,
    "batch": 32,
    "lr0": 0.0005, # Default 0.01
    "lrf": 0.01, # Default 0.01 
    "dropout": 0.0, # Default 0.0
    "epochs": 300, # Default 100
    "warmup_epochs": WARMUP, # Default 3.0
    "patience": 10, 
    "cache": False, # Set True if train with super computer
    "amp": True, # Mixed precision
    "time": TIMEOUT, # Default None
}

POSE_CONFIG = {
    "imgsz": 640,
    "batch": 32,
    "lr0": 0.0005, # Default 0.01
    "lrf": 0.01, # Default 0.01 
    "dropout": 0.0, # Default 0.0
    "epochs": 300, # Default 100
    "warmup_epochs": WARMUP, # Default 3.0
    "patience": 20, 
    "cache": False, # Set True if train with super computer
    "amp": True, # Mixed precision
    "time": TIMEOUT, # Default None
}

OBB_CONFIG = {
    "imgsz": 1024,
    "batch": 16,
    "lr0": 0.0005, # Default 0.01
    "lrf": 0.01, # Default 0.01 
    "dropout": 0.0, # Default 0.0
    "epochs": 300, # Default 100
    "warmup_epochs": WARMUP, # Default 3.0
    "patience": 20, 
    "cache": False, # Set True if train with super computer
    "amp": True, # Mixed precision
    "time": TIMEOUT, # Default None
}

TRAIN_CONFIG_PRESET = {
    'classify': CLASSIFY_CONFIG,
    'detect': DETECT_CONFIG,
    'pose': POSE_CONFIG,
    'obb': OBB_CONFIG,
}
