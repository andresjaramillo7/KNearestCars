"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Main script para ejecutar todos los modelos de Machine Learning
"""
# Importar los modelos
from MachineLearningModels.KNN.knn import main_knn
from MachineLearningModels.LogisticRegresion.logistic_regresion import main_logistic
from MachineLearningModels.NaiveBayes.naive_bayes import main_naive_bayes

from Data.data_preparation import load_dataset
training, trainingLabels, test, testLabels = load_dataset("Data/WinLoseDataset.csv")

print("\n============================== KNN ==============================")
# Llamar modelo KNN
k = 31
dist_func = 'manhattan'
main_knn(training, trainingLabels, test, testLabels, k, dist_func)

print("\n============================== Regresión Logística ==============================")
# Llamar modelo Regresión Logística
p = 'l2'
lambda_ = 1
main_logistic(training, trainingLabels, test, testLabels, p, lambda_)

print("\n============================== Naive Bayes ==============================")
# Llamar modelo Naive Bayes
main_naive_bayes(training, trainingLabels, test, testLabels)
