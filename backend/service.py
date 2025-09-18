"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Service to utilize
"""
from pathlib import Path
import numpy as np
from joblib import load
from Data.data_receiver_prep import transform_input

# Paths to trained model artifacts (.joblib files)
# Each key is a model identifier, and the value is the file path.
ARTIFACTS = {
    "knn":    Path("artifacts/knn_model.joblib"),
    "logreg": Path("artifacts/logreg_model.joblib"),
    "nb":     Path("artifacts/nb_model.joblib"),
}

# Load all models at import time so they are ready for inference.
# MODELS is a dict: { "model_name": trained_model_object }
MODELS = {name: load(path) for name, path in ARTIFACTS.items()}

def _get_binary_probabilities(model, features_df):
    """
    Compute probability estimates (as percentages) for binary classification.

    Parameters:
        model: sklearn-like model
            A trained scikit-learn model with methods such as predict_proba,
            decision_function, or predict.
        features_df: pd.DataFrame
            Single-row DataFrame with feature values.

    Returns:
        tuple
            (p1, p0) where:
            - p1 is the probability (%) of class 1
            - p0 is the probability (%) of class 0
    """
    if hasattr(model, "predict_proba"):
        # Preferred method: use predict_proba
        probabilities = model.predict_proba(features_df)[0]
        classes = getattr(model, "classes_", [0, 1])
        # Map class labels (0/1) to their probabilities
        probability_map = {int(c): float(p) for c, p in zip(classes, probabilities)}
        p1 = probability_map.get(1, 0.0)
        p0 = probability_map.get(0, 0.0)

    elif hasattr(model, "decision_function"):
        # Some linear models expose decision_function instead of predict_proba
        score = float(model.decision_function(features_df)[0])
        p1 = 1.0 / (1.0 + np.exp(-score))
        p0 = 1.0 - p1

    else:
        # Fallback: only hard prediction available
        prediction = int(model.predict(features_df)[0])
        p1 = 1.0 if prediction == 1 else 0.0
        p0 = 1.0 - p1
    return round(p1 * 100, 2), round(p0 * 100, 2)

def predict_all(input_values: list) -> dict:
    """
    Run predictions with all loaded models.

    Parameters:
        input_values: list
            List of raw frontend values in the order expected by transform_input:
            [horas, hora_dia, tipo, amigos, cansancio, racha]

    Returns:
        dict
            Dictionary with model names as keys, each containing a dict with probabilities:
            {
                "logreg": {"p_1": 63.27, "p_0": 36.73},
                "knn": {"p_1": 55.00, "p_0": 45.00},
                "nb": {"p_1": 60.50, "p_0": 39.50}
            }
    """
    # Convert raw values to feature DataFrame
    features_df = transform_input(input_values)

    # Collect predictions from each model
    predictions = {}
    for model_name, model in MODELS.items():
        p1, p0 = _get_binary_probabilities(model, features_df)
        predictions[model_name] = {"p_1": p1, "p_0": p0}

    return predictions
