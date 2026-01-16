# 🏋️ Fitness Tracker ML Project (Exercise Classification + Rep Counting)

## 📌 Project Overview
This project builds an end-to-end Machine Learning pipeline to process and model **IMU sensor data (accelerometer + gyroscope)** collected from a **MetaMotion wearable device**.  
The goal is to classify barbell exercises and count workout repetitions using a custom algorithm.

This is a **Quantified Self** project where raw sensor signals are converted into meaningful insights for fitness tracking.

---

## 🎯 Goal
Create Python scripts to:
- Process and clean accelerometer + gyroscope time-series data
- Visualize exercise patterns and detect outliers
- Engineer features (time + frequency domain)
- Train ML models to classify exercises
- Count repetitions using a custom rep-counting algorithm

---

## 🧠 The Quantified Self
The quantified self is any individual engaged in the self-tracking of any kind of biological, physical, behavioral, or environmental information. The self-tracking is driven by a certain goal of the individual, with a desire to act upon the collected information.

**Reference:**  
Hoogendoorn, M., & Funk, B. (2018). *Machine learning for the quantified self: On the art of learning from sensory data.*

---

## 📡 Dataset & Sensor
The dataset consists of IMU sensor recordings collected using the **MetaMotion** sensor:
- **Accelerometer** (linear acceleration)
- **Gyroscope** (angular velocity)

The time-series signals represent multiple barbell exercises performed across repetitions.

---

## 🏋️ Exercises Covered
<p align="center">
  <img src="assets/exercises.png" alt="Barbell Exercises" width="900">
</p>

Examples:
- Bench Press
- Deadlift
- Overhead Press
- Barbell Row
- Squat

---

## 🧰 Tech Stack
- **Language:** Python  
- **Libraries:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn  
- **Techniques:** Time-series processing, Signal filtering, Feature Engineering, PCA, Clustering  
- **Models:** Naive Bayes, SVM, Random Forest, Neural Networks  

---

## 🔄 Project Workflow (7 Parts)

### Part 1 — Introduction & Setup
- Problem definition and project goal
- Quantified self concept
- MetaMotion sensor overview
- Dataset understanding

### Part 2 — Data Processing
- Converting raw sensor files
- Reading CSV files
- Splitting data by exercise and sets
- Cleaning and formatting signals

### Part 3 — Data Visualization
- Time-series plots for accelerometer and gyroscope signals
- Comparing movement patterns across exercises
- Understanding signal trends and variability

### Part 4 — Outlier Detection
- Outlier detection using:
  - **Chauvenet’s Criterion**
  - **Local Outlier Factor (LOF)**
- Improved data reliability by removing noisy / inconsistent samples

### Part 5 — Feature Engineering
- Feature extraction from sensor signals:
  - Low-pass filtering (noise reduction)
  - Frequency-domain features (FFT-based)
  - PCA for dimensionality reduction
  - Clustering-based patterns

### Part 6 — Predictive Modeling (Exercise Classification)
Trained and evaluated multiple classification models:
- Naive Bayes
- Support Vector Machine (SVM)
- Random Forest
- Neural Network

### Part 7 — Repetition Counting
- Built a custom rep-counting algorithm using:
  - filtered motion signals
  - peak detection logic
  - rep segmentation strategy
- Counts repetitions per exercise set from sensor signals

---

## 📊 Model Evaluation
Models were compared using standard classification metrics such as:
- Accuracy
- Precision / Recall / F1-score
- Confusion Matrix

---

## ▶️ How to Run the Project

#### 1) Clone the repository

git clone https://github.com/your-username/fitness-tracker-ml-project.git
cd fitness-tracker-ml-project

#### 2) Install dependencies

pip install -r requirements.txt

#### 3) Run notebooks / scripts

Run the project scripts/notebooks in order (Part 1 → Part 7)
View visualizations and model performance outputs

### 📁 Suggested Project Structure

Fitness Tracker ML Project/
│── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│── notebooks/
│── src/
│── assets/
│   └── exercises.png
│── requirements.txt
│── README.md

## 🚀 Future Improvements

- Deploy the classification + rep counting pipeline as a real-time application
- Stream live IMU data and run inference on-device or via API
- Improve rep counting using adaptive thresholds and smoothing
- Add model monitoring and experiment tracking with MLflow

## 👨‍💻 Author

Harsh Kumar
Data Science | Machine Learning | Quantified Self Projects

📩 Email: harshkumar04510@gmail.com

🔗 LinkedIn: [https://www.linkedin.com/in/harshku/]

🔗 GitHub: [https://github.com/harsh2kum/Fitness-Tracker-ML-Project-]
