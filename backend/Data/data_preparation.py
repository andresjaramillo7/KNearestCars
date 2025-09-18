"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Data-Set Preparation
"""
import pandas as pd
from sklearn.model_selection import train_test_split

def load_dataset(path):
    # Leer CSV
    df_raw = pd.read_csv(path)
    df = df_raw.iloc[:, 1:].copy()
    df.columns = df.columns.str.strip()

    # Mapear horas (ordinal)
    MAP_HORAS = {
        "0 - 1 horas": 0,
        "1 - 2 horas": 1,
        "2 - 3 horas": 2,
        "3 - 4 horas": 3,
        "4 - 5 + horas": 4
    }

    df["Horas jugadas antes de la partida"] = df["Horas jugadas antes de la partida"].map(MAP_HORAS)

    # Agrupar clases con menos datos en "Otros"
    df["Tipo de juego"] = df["Tipo de juego"].replace({
        "Shooter": "Otros",
        "Estrategia": "Otros",
        "Deportes": "Otros",
    })

    # One-hot encoding
    cat_cols = ["Hora del día en que jugaste", "Tipo de juego", "Jugaste con amigos o solo"]
    df = pd.get_dummies(df, columns = cat_cols, drop_first = False)

    # 'y' y 'X'
    y = df["Ganaste o Perdiste la partida"].map({"Gané": 1, "Perdí": 0}).astype(int)
    X = df.drop(columns = ["Ganaste o Perdiste la partida"])

    # Split 80/20
    training, test, trainingLabels, testLabels = train_test_split(
        X, y, test_size = 0.20, stratify = y, random_state = 42
    )

    return training, trainingLabels, test, testLabels
