import csv
import math

#Given the CSV is in the format (Label, Sentence
#                                Label, Sentence)
def getDataFromCSV(fileName):
    # Initialize an empty list to store the tuples
    training_set = []
    testing_set = []
    # Open and read the CSV file
    with open(fileName, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        # Skip the header row if it contains column names
        next(csv_reader, None)
        # Iterate through each row in the CSV
        for row in csv_reader:
            if len(training_set) < 20:
                training_set.append((row[0],row[1]))
            else:
                testing_set.append((row[0],row[1]))
    return training_set, testing_set

#Get number of unique words in training Set
def getWordCount(trainingSet):
    #initialize variables
    wordsDic = {}
    wordCount = 0
    for label, sentence in trainingSet:
        words = sentence.split()
        #iterate through words
        for word in words:
            #If word has not been seen yet, add it and increment word count
            if word not in wordsDic:
                wordCount+=1
                wordsDic[word] = wordCount

    return wordCount

#Prior probability calculations
def calcProbabilities(trainingSet):
    #Initialize counts to 0
    spamCount, hamCount = 0, 0
    #Iterate through training set and determine probabilites of spam / ham
    for set in trainingSet:
        if set[0] == 'spam':
            spamCount += 1 
        else: hamCount += 1
    priorSpam = spamCount / len(trainingSet)
    priorHam = hamCount / len(trainingSet)
    return  priorSpam, priorHam

#Conditional probabilities
def trainingModel(trainingSet):
    #Initialize dictionaries
    spamDict = {}
    hamDict = {}
    #Iterate through training set
    for label, sentence in trainingSet:
        words = sentence.split()
        #Add spam and ham words to dictionaries
        for word in words:
            if label == 'spam':
                spamDict[word] = spamDict.get(word, 0) + 1
            else:
                    hamDict[word] = hamDict.get(word, 0) + 1
    return spamDict, hamDict

#Posterior probabilites
def classifyData(testingSet, priorSpamProb, priorHamProb, spamDict, hamDict, wordCount):
    correct_predictions = 0
    #Iterate through each line of testing set
    for correctLabel, sentence in testingSet:
        #split sentence into words
        words = sentence.split()
        #Initialize from prior probabilites based on the training set
        spamProbability = priorSpamProb
        hamProbability = priorHamProb
        #Iterate through each word in the sentence
        for word in words:
            # *= number of times word appears in spam or ham / total number of words in spam or hame dict
            spamProbability *= ((spamDict.get(word, 0) + 1) / (sum(spamDict.values()) + wordCount))
            hamProbability *= ((hamDict.get(word, 0) + 1) / (sum(hamDict.values()) + wordCount))
        predicted_label = 'spam' if spamProbability > hamProbability else 'ham'
        print("Sentence:", sentence)
        print("Posterior Probability (Spam):", spamProbability)
        print("Posterior Probability (Ham):", hamProbability)
        print("Class:", predicted_label)
        print("Expected:", correctLabel)
        print()

        if predicted_label == correctLabel:
            correct_predictions += 1

    return correct_predictions

def main():
    trainingSet, testingSet = getDataFromCSV('SpamDetection.csv')
    wordCount = getWordCount(trainingSet)
    priorSpam, priorHam = calcProbabilities(trainingSet)
    spamDict, hamDict = trainingModel(trainingSet)
    predictions = classifyData(testingSet, priorSpam, priorHam, spamDict, hamDict, wordCount)
    print("Correct Prediction Percentage:", predictions / len(testingSet))

if __name__ == '__main__':
    main()


