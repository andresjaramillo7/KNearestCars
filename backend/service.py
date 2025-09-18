from pathlib import Path
import numpy as np
from joblib import load
from Data.data_receiver_prep import transform_input

ARTIFACTS = {
    "knn":    Path("artifacts/knn_model.joblib"),
    "logreg": Path("artifacts/logreg_model.joblib"),
    "nb":     Path("artifacts/nb_model.joblib"),
}

MODELS = {name: load(path) for name, path in ARTIFACTS.items()}

def _binary_proba(model, X_df):
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(X_df)[0]
        classes = getattr(model, "classes_", [0, 1])
        pm = {int(c): float(p) for c, p in zip(classes, proba)}
        p1 = pm.get(1, 0.0); p0 = pm.get(0, 0.0)
    elif hasattr(model, "decision_function"):
        score = float(model.decision_function(X_df)[0])
        p1 = 1.0 / (1.0 + np.exp(-score))
        p0 = 1.0 - p1
    else:
        pred = int(model.predict(X_df)[0])
        p1 = 1.0 if pred == 1 else 0.0
        p0 = 1.0 - p1
    return round(p1 * 100, 2), round(p0 * 100, 2)

def predict_all(values: list) -> dict:
    X = transform_input(values)
    out = {}
    for name, model in MODELS.items():
        p1, p0 = _binary_proba(model, X)
        out[name] = {"p_1": p1, "p_0": p0}
    return out
