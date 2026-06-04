import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score

# --- Step 1: Load Dataset ---
print("Loading Olivetti Faces dataset...")
data = fetch_olivetti_faces(shuffle=True, random_state=42)
X = data.images.reshape(len(data.images), -1)  # flatten images to 1D
y = data.target

print(f"Total images: {X.shape[0]}")
print(f"Image size (flattened): {X.shape[1]} pixels")
print(f"Number of people: {len(np.unique(y))}")

# --- Step 2: Feature Scaling ---
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- Step 3: Train-Test Split ---
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\nTraining samples: {len(X_train)}, Testing samples: {len(X_test)}")

# --- Step 4: Train KNN Model ---
print("\nTraining KNN model...")
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# --- Step 5: Predictions ---
y_pred = model.predict(X_test)

# --- Step 6: Evaluation ---
print("\n--- Model Evaluation ---")
print(f"F1 Score (weighted): {f1_score(y_test, y_pred, average='weighted'):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# --- Step 7: Confusion Matrix ---
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(12, 10))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix - Face Recognition KNN")
plt.xlabel("Predicted Person")
plt.ylabel("Actual Person")
plt.tight_layout()
plt.savefig("confusion_matrix.png")
plt.show()
print("\nConfusion matrix saved!")

# --- Step 8: Visual Face Prediction Grid ---
print("\nGenerating face prediction grid...")
fig, axes = plt.subplots(4, 5, figsize=(14, 12))
axes = axes.ravel()

for i in range(20):
    # get original unscaled image
    original_image = data.images[len(X_train) + i]
    actual = y_test[i]
    predicted = y_pred[i]
    correct = "✓" if actual == predicted else "✗"
    color = "green" if actual == predicted else "red"

    axes[i].imshow(original_image, cmap='gray')
    axes[i].set_title(f"A:{actual} P:{predicted} {correct}", 
                       color=color, fontsize=9)
    axes[i].axis('off')

plt.suptitle("Face Recognition Results\nA=Actual, P=Predicted", fontsize=14)
plt.tight_layout()
plt.savefig("face_predictions.png")
plt.show()
print("Face prediction grid saved!")
