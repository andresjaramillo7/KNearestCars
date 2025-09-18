"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Logistic Regression Algorithm
"""
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import cross_val_score, cross_validate, KFold

def main_logistic(training, trainingLabels, test, testLabels, p, lambda_):

    print("--- Applying Logistic Regression using scikit-learn ---")

    # Create Logistic Regression classifier
    logistic = LogisticRegression(penalty = p, C = lambda_)

    # Train model with training data and labels
    print("Training Logistic Regression...")
    logistic.fit(training, trainingLabels)
    # Test the model with test data and save predictions
    print("Testing Logistic Regression...")
    predictions = logistic.predict(test)

    # Print comparison between predictions and true labels
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

    # Penalty Conversion
    if p == 'l1':
        penalty = 'Lasso (L1)'
    elif p == 'l2':
        penalty = 'Ridge (L2)'
    
    # Print metrics
    print(f"--- Logistic Regression Metrics (lambda = {lambda_}) | {penalty} ---")
    print(f"Model accuracy: {accuracy}")
    print(f"Model precision: {precision}")
    print(f"Model recall: {recall}")
    print(f"Model F1 score: {f1}")
    print(f"Model ROC / AUC: {roc_auc}")

    """
    K-Fold Cross Validation implemenatation:
    """
    # import pandas as pd

    # # Combine all data and all labels
    # all_data = pd.concat([training, test], ignore_index = True)
    # all_labels = pd.concat([trainingLabels, testLabels], ignore_index = True)
    # # Define the number of folds
    # kfold = KFold(n_splits = 5, shuffle = True, random_state = 42)
    # # Define scoring metrics
    # metrics = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']
    # # Apply cross-validation
    # results = cross_validate(logistic, all_data, all_labels, cv = kfold, scoring = metrics, return_train_score = False)
    # # Print scores for each fold
    # print("--- Cross-Validation metrics (for each fold) ---")
    # print("Accuracy:", results['test_accuracy'])
    # print("Precision:", results['test_precision_macro'])
    # print("Recall:", results['test_recall_macro'])
    # print("F1 Score:", results['test_f1_macro'])
