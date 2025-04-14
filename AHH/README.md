# Gesture Recognition-Based Smart Lock System

This project presents a smart lock system that utilizes hand gesture recognition for secure and accessible unlocking mechanisms. By combining computer vision and deep learning techniques, we aim to provide a contactless, keyless security solution that enhances accessibility and security.

## Features

- **Gesture Recognition:** Primary authentication mechanism using hand gestures
- **Real-time Processing:** Efficient processing pipeline optimized for Raspberry Pi 5
- **Configurable:** Easy to configure and adapt to different environments

## Technical Components

- **Software & Models:** Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) networks for gesture recognition
- **Hardware:** Optimized for Raspberry Pi 5 with efficient memory management

## System Architecture

1. **Input Processing:** Captures camera input for gesture recognition
2. **Gesture Recognition:** Processes hand movements and classifies gestures
3. **Decision Making:** Determines access based on recognized gestures

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gesture-facial-unlock-system.git
cd gesture-facial-unlock-system
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the gesture collection script to gather training data:
```bash
python collect_data.py
```

2. Train the model:
```bash
python run_trainer.py
```

3. Run the gesture recognition system:
```bash
python pipeline.py
```

## Configuration

The system can be configured through `config.py`:
- Camera settings
- Model paths
- Training parameters
- Recognition thresholds

## License

This project is licensed under the MIT License - see the LICENSE file for details.
