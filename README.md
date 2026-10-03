# 🚀 Python Development & Computer Vision Portfolio

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg?logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://peps.python.org/pep-0008/)

> A curated portfolio showcasing real-time **Computer Vision applications**, **interactive 2D game development**, **LeetCode algorithm solutions**, and **academic data structure implementations**.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Key Highlights](#-key-highlights)
  - [1. Featured Project: OpenCV Falling Items Catcher](#1-featured-project-opencv-falling-items-catcher)
  - [2. Computer Vision Experiments](#2-computer-vision-experiments)
  - [3. Algorithms & LeetCode Challenges](#3-algorithms--leetcode-challenges)
  - [4. Academic Coursework & Labs](#4-academic-coursework--labs)
- [Repository Structure](#-repository-structure)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Author & Contact](#-author--contact)

---

## 📖 Overview

This repository represents core programming and algorithmic projects developed during my university Computer Science / Engineering studies. It highlights:
- Practical application of **computer vision primitives** and **matrix manipulation** using OpenCV and NumPy.
- Algorithm design adhering to optimal **Time and Space complexity ($O(N)$ Big-O)** standards.
- Strong software engineering fundamentals: modular code organization, type annotations, automated assertions, and comprehensive documentation.

---

## 🌟 Key Highlights

### 1. Featured Project: OpenCV Falling Items Catcher
📂 [`01_featured_project_catcher_game/`](01_featured_project_catcher_game/)

An arcade-style 2D interactive desktop game built directly on top of OpenCV's image rendering pipeline:
- **Game Engine & Mechanics:** Dynamic frame-by-frame rendering loop running at high refresh rates with real-time HUD overlays.
- **Difficulty Curve:** Automated multi-stage speed multipliers ($1\times \to 2\times \to 3\times$) scaling over 5 minutes of survival gameplay.
- **Collision & Power-ups:** Axis-aligned bounding box collision detection handling positive score items, paddle expanders, paddle shrinkers, and instant-loss bombs.
- **Audio Integration:** Multi-channel background music loop and explosion SFX via `winsound`.

---

### 2. Computer Vision Experiments
📂 [`02_computer_vision/`](02_computer_vision/)

- **`hand_finger_counter.py`**: Real-time hand contour isolation and convex hull geometry analysis to detect and count extended fingers via webcam.
- **`webcam_blur_filter.py`**: Real-time webcam frame acquisition and 2D spatial Gaussian convolution filtering.

---

### 3. Algorithms & LeetCode Challenges
📂 [`03_algorithms_and_leetcode/`](03_algorithms_and_leetcode/)

Self-contained algorithmic solutions with type hints, docstrings, and automated unit test assertions:

| # | Problem | Difficulty | Category | Time | Space | Solution |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| 0001 | **Two Sum** | `Easy` | Hash Table | $O(N)$ | $O(N)$ | [`0001_two_sum.py`](03_algorithms_and_leetcode/0001_two_sum.py) |
| 0003 | **Longest Substring Without Repeating** | `Medium` | Sliding Window | $O(N)$ | $O(\min(N, M))$ | [`0003_longest_substring_without_repeating.py`](03_algorithms_and_leetcode/0003_longest_substring_without_repeating.py) |
| 0005 | **Longest Palindromic Substring** | `Medium` | Two Pointers | $O(N^2)$ | $O(1)$ | [`0005_longest_palindromic_substring.py`](03_algorithms_and_leetcode/0005_longest_palindromic_substring.py) |
| 0007 | **Reverse Integer** | `Medium` | Math / 32-bit Guard | $O(\log N)$ | $O(1)$ | [`0007_reverse_integer.py`](03_algorithms_and_leetcode/0007_reverse_integer.py) |
| 0014 | **Longest Common Prefix** | `Easy` | Vertical Scan | $O(S)$ | $O(1)$ | [`0014_longest_common_prefix.py`](03_algorithms_and_leetcode/0014_longest_common_prefix.py) |
| 0020 | **Valid Parentheses** | `Easy` | Stack | $O(N)$ | $O(N)$ | [`0020_valid_parentheses.py`](03_algorithms_and_leetcode/0020_valid_parentheses.py) |
| 0056 | **Merge Intervals** | `Medium` | Sorting / Interval | $O(N \log N)$ | $O(N)$ | [`0056_merge_intervals.py`](03_algorithms_and_leetcode/0056_merge_intervals.py) |
| 0202 | **Happy Number** | `Easy` | Cycle Detection | $O(\log N)$ | $O(\log N)$ | [`0202_happy_number.py`](03_algorithms_and_leetcode/0202_happy_number.py) |
| - | **Frequency Counter** | `Fundamental` | Hash Map | $O(N)$ | $O(K)$ | [`element_frequency_counter.py`](03_algorithms_and_leetcode/element_frequency_counter.py) |

---

### 4. Academic Coursework & Labs
📂 [`04_academic_coursework/`](04_academic_coursework/)

Structured laboratory modules covering core computer science principles:
- **`special_assignments/`**: Connect-3 board game engine with gravity mechanics and Chebyshev distance proximity grid modeling.
- **`lab_06_string_and_lists/`**: List comprehensions, recursion, and custom sorting algorithms without built-in libraries.
- **`lab_06_1_data_structures/`**: Slicing, recursive string inversion, and student ranking leaderboards.
- **`lab_07_dictionaries/`**: Nested key-value records, GPA aggregations, and database collection mutations.
- **`lab_08_matrix_and_grids/`**: 2D coordinate systems, board marking, and matrix character scanning.
- **`final_exam/`**: Prime number sieve generation and integer factor pair decomposition.

---

## 📁 Repository Structure

```
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
│
├── 01_featured_project_catcher_game/     # Featured OpenCV 2D arcade game
│   ├── README.md
│   ├── main.py
│   └── assets/
│       ├── images/
│       └── sounds/
│
├── 02_computer_vision/                  # Real-time computer vision scripts
│   ├── README.md
│   ├── hand_finger_counter.py
│   └── webcam_blur_filter.py
│
├── 03_algorithms_and_leetcode/          # Algorithm solutions with unit tests
│   ├── README.md
│   ├── 0001_two_sum.py
│   ├── 0003_longest_substring_without_repeating.py
│   ├── ...
│   └── element_frequency_counter.py
│
└── 04_academic_coursework/              # Academic labs and special assignments
    ├── README.md
    ├── special_assignments/
    ├── lab_06_string_and_lists/
    ├── lab_06_1_data_structures/
    ├── lab_07_dictionaries/
    ├── lab_08_matrix_and_grids/
    └── final_exam/
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Computer Vision & Graphics:** OpenCV (`opencv-python`), NumPy
- **Audio Processing:** `winsound` (Windows Multimedia API)
- **Tooling:** Git, GitHub, VS Code

---

## ⚡ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/KNIGHTKRUBPOM/Programming_Fundamentals.git
cd Programming_Fundamentals
```

### 2. Set up virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Projects
- **Launch Catcher Game:**
  ```bash
  python 01_featured_project_catcher_game/main.py
  ```
- **Run Hand & Finger Counter:**
  ```bash
  python 02_computer_vision/hand_finger_counter.py
  ```
- **Run LeetCode Unit Tests:**
  ```bash
  python 03_algorithms_and_leetcode/0001_two_sum.py
  ```

---

## 👨‍💻 Author

**Athichanan**  
- GitHub: [@KNIGHTKRUBPOM](https://github.com/KNIGHTKRUBPOM)  
- Email: your.email@example.com  


---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
