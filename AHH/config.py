import os

# Base directory configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data directories
TRAINING_DATA_DIR = os.path.join(BASE_DIR, "training_data")
MODELS_DIR = os.path.join(BASE_DIR, "models")
MODEL_WEIGHTS_DIR = os.path.join(BASE_DIR, "model_weights")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Training directories
PEACE_DIR = os.path.join(TRAINING_DATA_DIR, "peace")
NOT_PEACE_DIR = os.path.join(TRAINING_DATA_DIR, "not_peace")

# Model configuration
MODEL_INPUT_SHAPE = (63,)
NUM_CLASSES = 2

# Camera configuration
CAMERA_RESOLUTION = (640, 480)  # Can be adjusted based on performance needs
CAMERA_FPS = 30

# Training configuration
BATCH_SIZE = 32
EPOCHS = 50
VALIDATION_SPLIT = 0.2

# Ensure all directories exist
for directory in [TRAINING_DATA_DIR, MODELS_DIR, MODEL_WEIGHTS_DIR, DATA_DIR, 
                 PEACE_DIR, NOT_PEACE_DIR]:
    os.makedirs(directory, exist_ok=True) 