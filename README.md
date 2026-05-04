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

```text
traffic-monitoring-ai/
│
├── src/
│   ├── deepsort_tracking.py          # YOLO + DeepSORT tracking
│   ├── speed_and_safe_distance.py    # Speed + safe distance calculation
│   ├── distance_estimation.py        # Distance estimation (camera calibration)
│   ├── ocr.py                        # OCR module
│   ├── glare_reduction.py            # Image preprocessing
│   └── utils.py                      # Helper functions
│
├── configs/
│   ├── camera_matrix.pkl
│   └── object_and_image_points.pkl
│
├── data/
│   └── sample/
│
├── outputs/
│   └── demo_results/
│
├── main.py
├── requirements.txt
└── README.md
```
---
## Run Project

```bash id="kz61z6"
pip install -r requirements.txt
python main.py --input data/sample/video.mp4
```

---

## Output

* Tracked vehicles with unique IDs
* Estimated speed of each vehicle
* Distance between vehicles visualized on video

---

## Dataset

The original dataset used in this project is not publicly available.
To run the project:
- Provide your own traffic video input
- Or use webcam input

---

## My Contribution

* Developed **vehicle tracking pipeline** using YOLO + DeepSORT
* Implemented **speed and distance estimation algorithms**
* Integrated multiple modules into a complete traffic analysis system
* Cleaned and organized project structure for reproducibility

---



