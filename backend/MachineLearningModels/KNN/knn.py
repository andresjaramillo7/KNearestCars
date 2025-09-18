"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

KNN (K Nearest Neighbors) Algorithm
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import KFold, cross_validate

def main_knn(training, trainingLabels, test, testLabels, k, dist_func):

    print("--- Applying KNN using scikit-learn ---")

    # Create KNN classifier with k and distance function
    knn = KNeighborsClassifier(n_neighbors = k, metric = dist_func)

    # Train model with training data and labels
    print("Training KNN...")
    knn.fit(training, trainingLabels)
    # Test the model with test data and save predictions
    print("Testing KNN...")
    predictions = knn.predict(test)

    # Print comparation beetween predictions and true labels
    # print("Predictions vs. True Labels:")
    # for i in range(len(predictions)):
    #     print(f"Predicted: {str(predictions[i])} Real Value: {testLabels[i]}")

    # Define 'positive' label
    positive_label = 1
    # Evaluate model performance metrics
    accuracy = accuracy_score(testLabels, predictions)
    precision = precision_score(testLabels, predictions, pos_label = positive_label)
    recall = recall_score(testLabels, predictions, pos_label = positive_label)
    f1 = f1_score(testLabels, predictions, pos_label = positive_label)
    roc_auc = roc_auc_score(testLabels, predictions)

    # Print metrics
    print(f"--- KNN Metrics (k = {k} | {dist_func}) ---")
    print(f"Model accuracy: {accuracy}")
    print(f"Model precision: {precision}")
    print(f"Model recall: {recall}")
    print(f"Model F1 score: {f1}")
    print(f"Model ROC / AUC: {roc_auc}")
