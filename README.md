# ✋ PalmPilot – Control Your Mouse with Hand Gestures

PalmPilot is a Python-based computer vision project that lets you control your mouse with **just your hands**! Using **MediaPipe** and **OpenCV**, this tool detects your hand gestures via webcam and maps them to mouse actions like move, click, right-click, and drag using **PyAutoGUI**.

---

## 🚀 Features

- 🖱️ **Move Cursor** — Use your index finger to move the mouse across the screen.
- 👆 **Left Click** — Touch your index finger and thumb together.
- 👉 **Right Click** — Touch your middle finger and thumb together.
- ✊ **Mouse Drag** — Bring your index and middle fingers close to start a drag-and-drop action.

> Press `q` to quit the program.
---

## 🧠 Tech Stack

- **Python**
- [MediaPipe](https://google.github.io/mediapipe/) – Hand tracking
- [OpenCV](https://opencv.org/) – Webcam frame processing
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) – Mouse control

---

## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/handymouse.git
   cd PalmPilot
2. **Install dependencies**:
   ```bash
   pip install opencv-python mediapipe pyautogui
3. **Run the program**:
   ```bash
   python handymouse.py

**Notes**
1. Make sure you have a webcam connected.

2. The app works best under good lighting.

3. Cursor behavior may vary slightly based on resolution and frame rate.
