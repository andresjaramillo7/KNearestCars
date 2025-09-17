"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Algoritmo Naive Bayes
"""
import codecs
import operator
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import KFold, cross_validate

def main_naive_bayes(training, trainingLabels, test, testLabels):

    # #Create a dictionary that will contain all distinct topics/words from training samples
    # vocabulary = {}
    # #Open training file and extract all tokens
    # with codecs.open("training.txt", "r", "UTF-8") as file:
    #     for line in file:
    #         #Split label and text sample by using the special character @@@
    #         elements=line.split("@@@")
    #         #Split words by spaces
    #         for token in elements[0].split(" "):
    #             #if word in the vocabulary then increment the count
    #             if token in vocabulary:
    #                 vocabulary[token]+=1
    #             #Otherwise create a new dictionary entry with the first occurence
    #             else:
    #                 vocabulary[token]=1

    # #Eliminate any entry of the empy character
    # if "" in vocabulary:
    #     del vocabulary[""]

    # #Sort tokens by frequency (from most common to less common)
    # sortedVocabulary = sorted(vocabulary.items(), key = operator.itemgetter(1), reverse=True)

    # print("Top vocabulary tokens/words")
    # print(sortedVocabulary[:6])

    # print("Save vocabulary into a file")
    # #Save vocabulary in a txt file
    # with codecs.open("vocabulary.txt", "w", "UTF-8") as file:
    #     for token in sortedVocabulary[:]:
    #         file.write(token[0]+","+str(token[1])+"\n")

    # #Number of top features to select
    # featureNumber = 100
    # #Counter variable to help in the feature selection
    # count = 0
    # features = []
    # #Open the vocabulary file for extracting top features
    # with codecs.open("vocabulary.txt", "r", "UTF-8") as file:
    #     #Iterate over each file line
    #     for line in file:
    #         #Split line by comma
    #         elements=line.split(",")
    #         #If we reach the number of desired features then we break the for loop
    #         if (count == featureNumber):
    #             break
    #         features.append(elements[0].replace('\n', ''))
    #         count += 1
    #         print("Top 10 features for the classification algorithm:")
    #         print(features[:10])

    # #Training and test lists which will contain the vectors
    # trainingVectors=[]
    # trainingLabels=[]
    # testVectors=[]
    # testLabels=[]
    # #Open the training file to transform text to numbers
    # print("Create training vectors")
    # with codecs.open("training.txt", "r", "UTF-8") as file:
    #     for line in file:
    #         temporalVector=[]
    #         #Split label and text sample by using the special character @@@
    #         elements=line.split("@@@")
    #         8
    #         #Split words by spaces
    #         currentTokens=elements[0].split(" ")
    #         #Check if the feature is observed in the current training sample
    #         for feature in features:
    #             #If observed then add 1 to the current feature
    #             if feature in currentTokens:
    #                 temporalVector.append(1)
    #             #If not, add a 0
    #             else:
    #                 temporalVector.append(0)
    #         #Storage the current vector into a list of lists
    #         trainingVectors.append(temporalVector)
    #         #Storage the current label into a list
    #         trainingLabels.append(elements[1].replace('\n', ''))

    # print("Save training vectors into a file")
    # with codecs.open("trainingVectors.txt", "w", "UTF-8") as file:
    #     for vector,label in zip(trainingVectors,trainingLabels):
    #         file.write(",".join([str(x) for x in vector])+","+label+"\n")

    # print("Create test vectors")
    # #Open the test file to transfor text to numbers
    # with codecs.open("test.txt", "r", "UTF-8") as file:
    #     for line in file:
    #         temporalVector=[]
    #         #Split label and text sample by using the special character @@@
    #         elements=line.split("@@@")
    #         #Split words by spaces
    #         currentTokens=elements[0].split(" ")
    #         #Check if the feature is observed in the current training sample
    #         for feature in features:
    #             #If observed then add 1 to the current feature
    #             if feature in currentTokens:
    #                 temporalVector.append(1)
    #             #If not, add a 0
    #             else:
    #                 temporalVector.append(0)
    #         #Storage the current vector into a list of lists
    #         testVectors.append(temporalVector)
    #         #Storage the current label into a list
    #         testLabels.append(elements[1].replace('\n', ''))

    # print("Save test vectors into a file")
    # with codecs.open("testVectors.txt", "w", "UTF-8") as file:
    #     for vector,label in zip(testVectors,testLabels):
    #         file.write(",".join([str(x) for x in vector])+","+label+"\n")

    # #Create necessary Python list for saving vector information
    # training = []
    # trainingLabels = []
    # test = []
    # testLabels = []
    # #Open training vectors from a file
    # print("Load training vectors")

    # with codecs.open("trainingVectors.txt", "r", "UTF-8") as file:
    #     for line in file:
    #         #Eliminate the break line in each text line
    #         line=line.replace('\n', '')
    #         #Separate string elements by comma
    #         line=line.split(",")
    #         #Storage training labels into a Python list
    #         trainingLabels.append(line[-1])
    #         #Storage training vectors into a Python list
    #         training.append([int(x) for x in line[:-1]])

    # #Open test vectors from a file
    # print("Load test vectors")
    # with codecs.open("testVectors.txt", "r", "UTF-8") as file:
    #     for line in file:
    #         #Eliminate the break line in each text line
    #         line=line.replace('\n', '')
    #         #Separate string elements by comma
    #         line=line.split(",")
    #         #Storage training labels into a Python list
    #         testLabels.append(line[-1])
    #         #Storage training vectors into a Python list
    #         test.append([int(x) for x in line[:-1]])





    """
    Apply the Naive Bayes multinomial approach over test samples
    using training data on scikit-learn
    """
    print("--- Aplicando Naive Bayes usando scikit-learn ---")

    # Crear clasificador de Naive Bayes
    naive_bayes = MultinomialNB()

    # Entrenar modelo con data y etiquetas de entrenamiento
    print("Entrenando Naive Bayes...")
    naive_bayes.fit(training, trainingLabels)
    # Poner a prueba el modelo con test data y guardar las predicciones
    print("Probando Naive Bayes...")
    predictions = naive_bayes.predict(test)

    # Print comparación entre predicción y etiqueta real
    # print("Predictions vs. True Labels:")
    # for i in range(len(predictions)):
    #     print(f"Predicted: {str(predictions[i])} Real Value: {testLabels[i]}")

    # Definir etiqueta 'positiva' - Asumiendo que 'Present\r' es la clase 'positiva'
    positive_label = 'Present\r'

     # Evaluar 'Accuracy' del modelo
    accuracy = accuracy_score(testLabels, predictions)
    precision = precision_score(testLabels, predictions, pos_label = positive_label)
    recall = recall_score(testLabels, predictions, pos_label = positive_label)
    f1 = f1_score(testLabels, predictions, pos_label = positive_label)
   
    # Printear metricas
    print(f"--- Métricas de Naive Bayes ---")
    print(f"Model accuracy: {accuracy}")
    print(f"Model precision: {precision}")
    print(f"Model recall: {recall}")
    print(f"Model F1 score: {f1}")
