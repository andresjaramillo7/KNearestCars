"""
Andrés Jaramillo Barón - A01029079
Pedro Mauri Mtz - A01029143
Ricardo Calvo Pérez - A01028889

Preparación del data-set
"""
import codecs

# Load training and test data from dataset files
training = []
trainingLabels = []
test = []
testLabels = []

print("Load training samples")
with codecs.open("Data/training.txt", "r", "UTF-8") as file:
    for line in file:
        elements=(line.rstrip('\n')).split(",")
        training.append([float(elements[0]),float(elements[1])])
        trainingLabels.append(elements[2])

print("Load test samples")
with codecs.open("Data/test.txt", "r", "UTF-8") as file:
    for line in file:
        elements=(line.rstrip('\n')).split(",")
        test.append([float(elements[0]),float(elements[1])])
        testLabels.append(elements[2])
