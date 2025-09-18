"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Dataset Frontend Receiver Preparation
"""
import pandas as pd

# Fixed order of columns (must match the dataset used in training)
# This ensures that the DataFrame we generate for predictions
# has the exact same structure and column order as the training data.
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
    Convert raw frontend input values into a pandas DataFrame
    with the exact one-hot encoded structure used in training.

    Parameters:
        values: list
            Expected order:
            [horas, hora_dia, tipo, amigos, cansancio, racha]

            - horas: string (e.g., "2 - 3 horas")
            - hora_dia: string (e.g., "Noche (6pm–12am)")
            - tipo: string (e.g., "MOBA" or "Otros")
            - amigos: string (e.g., "Con amigos" or "Solo")
            - cansancio: int/str (numeric level of tiredness before playing)
            - racha: int/str (number of consecutive wins before this game)

    Returns:
        pd.DataFrame
            A single-row DataFrame with columns aligned to FEATURE_COLUMNS.
    """
    # Unpack values into variables
    horas, hora_dia, tipo, amigos, cansancio, racha = values

    # Initialize all features as 0
    # This way we can "turn on" only the corresponding one-hot features
    features = {col: 0 for col in FEATURE_COLUMNS}

    # Numeric features
    # Convert "horas" text into a numeric code
    features["Horas jugadas antes de la partida"] = HOURS_MAP[horas]
    # Cansancio and racha are already numeric (cast to int for safety)
    features["Nivel de cansancio antes de jugar"] = int(cansancio)
    features["Número de victorias consecutivas que llevabas antes de esta partida"] = int(racha)

    # One-hot: Hora del día
    # Example: "Hora del día en que jugaste_Noche (6pm–12am)" -> 1
    col_hora = f"Hora del día en que jugaste_{hora_dia}"
    if col_hora in features:
        features[col_hora] = 1

    # One-hot: Tipo de juego
    # Only one of MOBA or Otros will be active
    if tipo == "MOBA":
        features["Tipo de juego_MOBA"] = 1
    else:
        features["Tipo de juego_Otros"] = 1

    # One-hot: Amigos/Solo
    # Detect if input string contains "amig" (to handle variations like "Con amigos")
    if "amig" in amigos.lower():
        features["Jugaste con amigos o solo_Con amigos"] = 1
    else:
        features["Jugaste con amigos o solo_Solo"] = 1

    # Convert dict into a single-row DataFrame,
    # making sure the column order matches FEATURE_COLUMNS
    return pd.DataFrame([features], columns=FEATURE_COLUMNS)