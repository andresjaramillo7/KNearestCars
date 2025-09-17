"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Algoritmo KNN
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main_knn(training, trainingLabels, test, testLabels):

    #Apply the KNN approach over test samples using training data on scikit-learn
    print("Apply the KNN approach over test samples on scikit-learn")

    # Create the kNN classifier with k=3
    knn = KNeighborsClassifier(n_neighbors=5)

    # Fit the model to the training data
    knn.fit(training, trainingLabels)

    # Make predictions on the test data
    predictions = knn.predict(test)

    # Print each prediction with the real label
    print("Predictions vs. True Labels:")
    for i in range(len(predictions)):
        print("Predicted: "+str(predictions[i])+" realValue: "+testLabels[i])

    # Evaluate the models performance
    accuracy = accuracy_score(testLabels,predictions)
    print("Model accuracy:", accuracy)
