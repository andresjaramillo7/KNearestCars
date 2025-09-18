"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Algoritmo KNN
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import KFold, cross_validate

def main_knn(training, trainingLabels, test, testLabels, k, dist_func):

    print("--- Aplicando KNN usando scikit-learn ---")

    # Crear el clasificador KNN con k
    knn = KNeighborsClassifier(n_neighbors = k, metric = dist_func)

    # Entrenar modelo con data y etiquetas de entrenamiento
    print("Entrenando KNN...")
    knn.fit(training, trainingLabels)
    # Poner a prueba el modelo con test data y guardar las predicciones
    print("Probando KNN...")
    predictions = knn.predict(test)

    # Print comparación entre predicción y etiqueta real
    # print("Predictions vs. True Labels:")
    # for i in range(len(predictions)):
    #     print(f"Predicted: {str(predictions[i])} Real Value: {testLabels[i]}")

    # Definir etiqueta 'positiva' - Asumiendo que 'Gané\r' es la clase 'positiva'
    positive_label = 1
    # Evaluar métricas de rendimiento del modelo
    accuracy = accuracy_score(testLabels, predictions)
    precision = precision_score(testLabels, predictions, pos_label = positive_label)
    recall = recall_score(testLabels, predictions, pos_label = positive_label)
    f1 = f1_score(testLabels, predictions, pos_label = positive_label)
   
    # Printear metricas
    print(f"--- Métricas de KNN (k = {k}) ---")
    print(f"Model accuracy: {accuracy}")
    print(f"Model precision: {precision}")
    print(f"Model recall: {recall}")
    print(f"Model F1 score: {f1}")
