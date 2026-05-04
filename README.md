# Traffic Monitoring System using YOLO & DeepSORT

## Overview

This project implements a traffic monitoring system using computer vision techniques to detect, track, and analyze vehicles from video input.
The system estimates **vehicle speed** and **safe distance** between vehicles using camera-based calculations.

---

## Features

* Vehicle detection using YOLO
* Multi-object tracking using DeepSORT
* Speed estimation across video frames
* Distance estimation using camera calibration
* OCR module for text extraction (e.g., license plates)

---

## Pipeline

```id="4v2h6j"
Video Input 
   → YOLO Detection 
   → DeepSORT Tracking 
   → Distance Estimation 
   → Speed & Safe Distance Calculation 
   → Output Visualization
```

---

## Main Components

* `DeepSORT_tracking_with_YOLO.py`
  → Detect and track vehicles using YOLO + DeepSORT

* `Speed_and_Safe_distance.py`
  → Calculate vehicle speed and safe distance between objects

* `Distance_esimation.py`
  → Estimate real-world distance using camera calibration

* `OCR.py`
  → Perform text recognition from detected regions

* `helper.py`
  → Utility functions for processing and calculations

---

## Tech Stack

* Python
* OpenCV
* YOLO
* DeepSORT
* NumPy

---

## Project Structure
```
traffic-monitoring-ai/
│
├── src/
│   ├── detection/
│   ├── tracking/
│   ├── speed_distance/
│   ├── ocr/
│   └── utils/
│
├── data/
│   └── sample/
│
├── outputs/
│
├── notebooks/
│
├── main.py
├── requirements.txt
└── README.md
```
---
## Run Project

```bash id="kz61z6"
pip install -r requirements.txt
python DeepSORT_tracking_with_YOLO.py
```

---

## Output

* Tracked vehicles with unique IDs
* Estimated speed of each vehicle
* Distance between vehicles visualized on video

---

## Dataset

Dataset is not included due to size limitations.
Sample data can be added in the `data/` folder.

---

## My Contribution

* Developed **vehicle tracking pipeline** using YOLO + DeepSORT
* Implemented **speed and distance estimation algorithms**
* Integrated multiple modules into a complete traffic analysis system
* Cleaned and organized project structure for reproducibility

---



