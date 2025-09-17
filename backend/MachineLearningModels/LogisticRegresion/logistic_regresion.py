"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Algoritmo Regresión Logística
"""
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def main_logistic(training, trainingLabels, test, testLabels):

    # Apply the logistic regression approach over test samples using training data on scikit-learn
    print("Apply the logistic regression approach over test samples on scikit-learn")

    # Create the logistic regression classifier
    logistic = LogisticRegression()

    # Fit the model to the training data
    logistic.fit(training, trainingLabels)

    # Make predictions on the test data
    predictions = logistic.predict(test)

    # Print each prediction with the real label
    print("Predictions vs. True Labels:")
    for i in range(len(predictions)):
        print("Predicted: " + str(predictions[i]) + " Real Value: " + testLabels[i])

    # Evaluate the model's performance
    accuracy = accuracy_score(testLabels, predictions)
    print("Model accuracy:", accuracy)
