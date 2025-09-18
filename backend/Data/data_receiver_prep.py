import pandas as pd

# Fixed order of columns (must match your training dataset)
FEATURE_COLUMNS = [
    "Horas jugadas antes de la partida",
    "Nivel de cansancio antes de jugar",
    "Número de victorias consecutivas que llevabas antes de esta partida",
    "Hora del día en que jugaste_Madrugada (12am–6am)",
    "Hora del día en que jugaste_Mañana (6 am - 12 pm)",
    "Hora del día en que jugaste_Noche (6pm–12am)",
    "Hora del día en que jugaste_Tarde (12pm–6pm)",
    "Tipo de juego_MOBA",
    "Tipo de juego_Otros",
    "Jugaste con amigos o solo_Con amigos",
    "Jugaste con amigos o solo_Solo"
]

HOURS_MAP = {
    "0 - 1 horas": 0,
    "1 - 2 horas": 1,
    "2 - 3 horas": 2,
    "3 - 4 horas": 3,
    "4 - 5 + horas": 4,
}

def transform_input(values: list) -> pd.DataFrame:
    """
    Convert raw frontend list into a DataFrame with the same
    one-hot encoded features used in training.
    """
    # Unpack values
    horas, hora_dia, tipo, amigos, cansancio, racha = values

    # Base dict with all zeros
    features = {col: 0 for col in FEATURE_COLUMNS}

    # Numeric
    features["Horas jugadas antes de la partida"] = HOURS_MAP[horas]
    features["Nivel de cansancio antes de jugar"] = int(cansancio)
    features["Número de victorias consecutivas que llevabas antes de esta partida"] = int(racha)

    # One-hot: Hora del día
    col_hora = f"Hora del día en que jugaste_{hora_dia}"
    if col_hora in features:
        features[col_hora] = 1

    # One-hot: Tipo de juego
    if tipo == "MOBA":
        features["Tipo de juego_MOBA"] = 1
    else:
        features["Tipo de juego_Otros"] = 1

    # One-hot: Amigos/Solo
    if "amig" in amigos.lower():
        features["Jugaste con amigos o solo_Con amigos"] = 1
    else:
        features["Jugaste con amigos o solo_Solo"] = 1

    # Convert to DataFrame with correct column order
    return pd.DataFrame([features], columns=FEATURE_COLUMNS)