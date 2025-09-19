"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Main script to run all Machine Learning models
"""
# Import Models
from MachineLearningModels.KNN.knn import main_knn
from MachineLearningModels.LogisticRegresion.logistic_regresion import main_logistic
from MachineLearningModels.NaiveBayes.naive_bayes import main_naive_bayes
# Import Data-Set
from Data.data_preparation import load_dataset
training, trainingLabels, test, testLabels = load_dataset("backend/Data/WinLoseDataset.csv")

print("\n============================== KNN ==============================")
# Run KNN Model
k = 17
dist_func = 'cosine'
w = "uniform"
save_path = "backend/artifacts/knn_model.joblib"
main_knn(training, trainingLabels, test, testLabels, k, dist_func, w, save = save_path)

print("\n============================== Logistic Regression ==============================")
# Run Logistic Regression Model
p = 'l2'
lambda_ = 1
save_path = "backend/artifacts/logreg_model.joblib"
main_logistic(training, trainingLabels, test, testLabels, p, lambda_, save = save_path)

print("\n============================== Naive Bayes ==============================")
# Run Naive Bayes Model
save_path = "backend/artifacts/nb_model.joblib"
main_naive_bayes(training, trainingLabels, test, testLabels, save = save_path)
