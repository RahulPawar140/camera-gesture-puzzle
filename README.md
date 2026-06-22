# 📸 Gesture-Controlled Camera Puzzle 🖐️🧩

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![Status](https://img.shields.io/badge/Status-Working-success)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

---

## 🔍 Overview
The **Gesture-Controlled Camera Puzzle** is a **computer vision–based interactive application** that allows users to solve a puzzle using **hand gestures** captured via a webcam.

The puzzle is rendered **directly on the live camera feed**, enabling a **touch-free and intuitive user experience** without using a keyboard or mouse.

---

## 🎯 Objectives
- 🎥 Capture real-time video using a webcam  
- ✋ Detect and track hand gestures  
- 🧩 Display an interactive puzzle on the camera feed  
- 👉 Solve the puzzle using finger movements  
- 🎉 Show a success message after puzzle completion  

---

## 🛠️ Tech Stack
| Technology | Purpose |
|----------|--------|
| **Python** | Core programming language |
| **OpenCV** | Camera access & image processing |
| **MediaPipe** | Hand & finger landmark detection |
| **NumPy** | Fast numerical operations |
| **Pygame** | Puzzle logic & interaction |

---

## ⚙️ How It Works
1. Webcam captures live video frames  
2. MediaPipe detects hand landmarks in real time  
3. Puzzle is drawn on top of the camera feed  
4. User interacts using finger gestures  
5. Puzzle logic validates moves  
6. On success → **“PUZZLE SOLVED 🎉”** is displayed  
7. Camera continues running  

---

## ✨ Features
- 🖐️ Gesture-based interaction  
- 🪟 Single camera window  
- ⚡ Real-time processing  
- ❌ No keyboard or mouse required  
- 🧠 Interactive puzzle logic  

---

## 🚀 Installation & Run

### 📌 Prerequisites
- Python **3.11+**
- Working webcam

### 📦 Install Dependencies
```bash
pip install mediapipe opencv-python numpy pygame pillow
