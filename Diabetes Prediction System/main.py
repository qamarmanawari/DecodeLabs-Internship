# ===================PROJECT 2=================================
# PROJECT 2: Diabetes Prediction Using KNN
# DecodeLabs Internship | Batch 2026 | Powered by DecodeLabs
# ============================================================
from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    precision_score, recall_score, f1_score
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def main():
    # ================== 1. LOAD DATASET ==================
    df = pd.read_csv(ROOT / "diabetes_prediction_dataset.csv")

    print("=" * 65)
    print("DECODELABS AI PROJECT 2 — DIABETES PREDICTION (KNN)")
    print("=" * 65)
    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print("\nFirst five rows:")
    print(df.head().to_string(index=False))

    # ================== 2. HANDLE MISSING VALUES ==================
    missing = df.isnull().sum().sum()
    if missing > 0:
        print(f"\nMissing values found ({missing}) — dropping rows.")
        df = df.dropna()
    else:
        print("\nNo missing values — dataset is clean.")

    # ================== 3. ENCODE TEXT COLUMNS ==================
    text_cols = df.select_dtypes(include=["object"]).columns.tolist()
    print(f"\nText columns to encode: {text_cols}")

    encoders = {}
    for col in text_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
        print(f"  {col}: {list(le.classes_)}")

    # ================== 4. SEPARATE FEATURES & TARGET ==================
    TARGET = "diabetes"
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    class_names = ["No Diabetes", "Diabetes"]

    print(f"\nFeatures used ({X.shape[1]}): {X.columns.tolist()}")
    print(f"Classes: {class_names}")

    print("\nClass distribution:")
    print(y.value_counts().to_string())

    print("\nClass imbalance (%):")
    print((y.value_counts(normalize=True) * 100).round(2).to_string())

    # ================== 5. TRAIN / TEST SPLIT ==================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    print(f"\nTraining samples: {len(X_train)} ({len(X_train)/len(X):.0%})")
    print(f"Testing samples:  {len(X_test)} ({len(X_test)/len(X):.0%})")

    # ================== 6. CHOOSE K VIA CROSS-VALIDATION ==================
    print("\nTuning k (1-15) using 5-fold CV — this may take a few minutes...")
    cv_results = []
    for k in range(1, 16):
        candidate = Pipeline([
            ("scaler", StandardScaler()),
            ("knn", KNeighborsClassifier(n_neighbors=k))
        ])
        scores = cross_val_score(
            candidate, X_train, y_train,
            cv=5, scoring="accuracy", n_jobs=-1
        )
        cv_results.append({
            "k": k,
            "mean_cv_accuracy": scores.mean(),
            "std_cv_accuracy": scores.std()
        })
        print(f"  k={k:2d}  →  mean accuracy = {scores.mean():.4f}  (± {scores.std():.4f})")

    cv_df = pd.DataFrame(cv_results)
    cv_df.to_csv(OUT / "k_selection_results.csv", index=False)

    best_k = int(cv_df.loc[cv_df["mean_cv_accuracy"].idxmax(), "k"])
    print(f"\n>>> Best k selected: {best_k} "
          f"(mean CV accuracy = {cv_df['mean_cv_accuracy'].max():.4f})")

    # ================== 7. TRAIN FINAL MODEL ==================
    print("\nTraining final model on full training set...")
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=best_k))
    ])
    model.fit(X_train, y_train)

    print("Predicting on test set...")
    y_pred = model.predict(X_test)

    # ================== 8. EVALUATE ==================
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average="weighted", zero_division=0)
    recall = recall_score(y_test, y_pred, average="weighted", zero_division=0)
    f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)
    report = classification_report(
        y_test, y_pred, target_names=class_names, zero_division=0
    )
    cm = confusion_matrix(y_test, y_pred)

    print("\n" + "=" * 65)
    print("TEST RESULTS")
    print("=" * 65)
    print(f"Accuracy:           {accuracy:.4f} ({accuracy:.1%})")
    print(f"Weighted precision: {precision:.4f}")
    print(f"Weighted recall:    {recall:.4f}")
    print(f"Weighted F1-score:  {f1:.4f}")
    print("\nClassification report:")
    print(report)
    print("Confusion matrix (rows = actual, columns = predicted):")
    print(cm)

    # ================== 9. SAVE METRICS ==================
    metrics = {
        "dataset": "Diabetes Prediction",
        "algorithm": "K-Nearest Neighbors (KNN)",
        "selected_k": best_k,
        "train_samples": int(len(X_train)),
        "test_samples": int(len(X_test)),
        "accuracy": float(accuracy),
        "weighted_precision": float(precision),
        "weighted_recall": float(recall),
        "weighted_f1_score": float(f1),
        "class_names": class_names,
        "confusion_matrix": cm.tolist(),
        "classification_report": classification_report(
            y_test, y_pred, target_names=class_names,
            output_dict=True, zero_division=0
        )
    }
    (OUT / "metrics.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )

    # Per-sample predictions
    predictions = X_test.copy()
    predictions["actual_species"] = y_test.map(
        {0: "No Diabetes", 1: "Diabetes"}
    ).values
    predictions["predicted_species"] = pd.Series(
        y_pred, index=X_test.index
    ).map({0: "No Diabetes", 1: "Diabetes"})
    predictions.to_csv(OUT / "test_predictions.csv", index=False)

    # ================== 10. PLOT 1 — CONFUSION MATRIX ==================
    plt.figure(figsize=(7, 5))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=class_names, yticklabels=class_names
    )
    plt.title("Confusion Matrix — Diabetes KNN Classifier")
    plt.xlabel("Predicted class")
    plt.ylabel("Actual class")
    plt.tight_layout()
    plt.savefig(OUT / "confusion_matrix.png", dpi=180)
    plt.close()

    # ================== 11. PLOT 2 — K SELECTION ==================
    plt.figure(figsize=(7, 5))
    plt.plot(cv_df["k"], cv_df["mean_cv_accuracy"], marker="o")
    plt.fill_between(
        cv_df["k"],
        cv_df["mean_cv_accuracy"] - cv_df["std_cv_accuracy"],
        cv_df["mean_cv_accuracy"] + cv_df["std_cv_accuracy"],
        alpha=0.15
    )
    plt.xticks(range(1, 16))
    plt.xlabel("Number of neighbors (k)")
    plt.ylabel("Mean 5-fold CV accuracy")
    plt.title("K Selection Using Training Data Only")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / "k_selection.png", dpi=180)
    plt.close()

    # ================== 12. DONE ==================
    print("\n" + "=" * 65)
    print(f"All outputs saved in: {OUT}")
    print("Project completed successfully!")
    print("=" * 65)


if __name__ == "__main__":
    main()