"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Main script para ejecutar todos los modelos de Machine Learning
"""

from MachineLearningModels.KNN.knn import main_knn
from MachineLearningModels.LogisticRegresion.logistic_regresion import main_logistic
from MachineLearningModels.NaiveBayes.naive_bayes import main_naive_bayes

from Data.data_preparation import training, trainingLabels, test, testLabels

main_knn(training, trainingLabels, test, testLabels)
main_logistic(training, trainingLabels, test, testLabels)
# main_naive_bayes()
