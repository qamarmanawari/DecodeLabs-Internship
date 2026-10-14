# DecodeLabs AI Project 2 — Diabetes Prediction Using KNN

A complete machine learning project that predicts whether a patient has diabetes
based on 8 medical features using the **K-Nearest Neighbors (KNN)** algorithm.

---

## 📌 Project Overview

- **Dataset:** `diabetes_prediction_dataset.csv` (100,000 samples, 8 features, 2 classes)
- **Algorithm:** K-Nearest Neighbors (KNN)
- **Task:** Binary Classification (Diabetes: Yes / No)
- **Goal:** Build, tune, and evaluate a KNN classifier with proper ML practices
  (stratified split, cross-validation, pipeline-based scaling).

---

## 📊 Dataset

| Feature | Type | Description |
|---------|------|-------------|
| `gender` | Categorical | Male / Female / Other |
| `age` | Numeric | Patient age |
| `hypertension` | Binary | 0 = No, 1 = Yes |
| `heart_disease` | Binary | 0 = No, 1 = Yes |
| `smoking_history` | Categorical | never / former / current / etc. |
| `bmi` | Numeric | Body Mass Index |
| `HbA1c_level` | Numeric | Avg. blood sugar (3 months) |
| `blood_glucose_level` | Numeric | Current blood sugar |
| **`diabetes`** | **Target** | **0 = No, 1 = Yes** |

**Note:** Dataset is imbalanced (~91.5% No, ~8.5% Yes).

---

## ⚙️ Workflow

1. **Load & explore** the dataset
2. **Encode** categorical columns (`gender`, `smoking_history`) using `LabelEncoder`
3. **Split** data: 80% train / 20% test (stratified)
4. **Tune `k`** (1–15) using 5-fold cross-validation on training data only
5. **Train final model** using the best `k`
6. **Evaluate** using accuracy, precision, recall, F1, and confusion matrix
7. **Save** metrics, predictions, and plots

---

## 🗂️ Project Structure

```
Week 2/
├── main.py                            # Main script
├── diabetes_prediction_dataset.csv    # Dataset
├── README.md                          # This file
└── outputs/                           # Generated after running
    ├── k_selection_results.csv
    ├── metrics.json
    ├── test_predictions.csv
    ├── confusion_matrix.png
    └── k_selection.png
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install pandas scikit-learn matplotlib seaborn
```

### 2. Run the script

```bash
python main.py
```

Runtime: **~3–6 minutes** (mostly k-tuning via cross-validation).

---
