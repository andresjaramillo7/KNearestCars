"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Data-Set Preparation
"""
import pandas as pd
from sklearn.model_selection import train_test_split

def load_dataset(path: str):
    """
    Load and preprocess the dataset from a CSV file.

    Args:
        path (str): Path to the CSV dataset file.

    Returns:
        X_train (pd.DataFrame): Training feature set.
        y_train (pd.Series): Labels for the training set.
        X_test (pd.DataFrame): Test feature set.
        y_test (pd.Series): Labels for the test set.
    """

    # 1. Read CSV and remove the first column (likely an index column)
    df_raw = pd.read_csv(path)
    df_clean = df_raw.iloc[:, 1:].copy()
    df_clean.columns = df_clean.columns.str.strip()  # remove leading/trailing spaces

    # 2. Map "hours played before match" from ranges to ordinal numeric values
    HOURS_MAP = {
        "0 - 1 horas": 0,
        "1 - 2 horas": 1,
        "2 - 3 horas": 2,
        "3 - 4 horas": 3,
        "4 - 5 + horas": 4,
    }
    df_clean["Horas jugadas antes de la partida"] = (
        df_clean["Horas jugadas antes de la partida"].map(HOURS_MAP)
    )

    # 3. Group less frequent game types into "Otros"
    df_clean["Tipo de juego"] = df_clean["Tipo de juego"].replace(
        {"Shooter": "Otros", "Estrategia": "Otros", "Deportes": "Otros"}
    )

    # 4. Apply one-hot encoding to categorical columns
    categorical_cols = [
        "Hora del día en que jugaste",
        "Tipo de juego",
        "Jugaste con amigos o solo",
    ]
    df_clean = pd.get_dummies(df_clean, columns=categorical_cols, drop_first=False)

    # 5. Define features (X) and labels (y)
    # Map labels: "Gané" → 1, "Perdí" → 0
    y = df_clean["Ganaste o Perdiste la partida"].map({"Gané": 1, "Perdí": 0}).astype(int)
    X = df_clean.drop(columns=["Ganaste o Perdiste la partida"])

    # 6. Split dataset into training and test sets (80/20 split, stratified by label distribution)
    training, test, trainingLabels, testLabels = train_test_split(
        X, y, test_size=0.20, stratify=y, random_state=42
    )

    return training, trainingLabels, test, testLabels
