# Spam Detection System using Naive Bayes

This Python script is designed to demonstrate a simple spam detection system utilizing the Naive Bayes algorithm. It includes various functions to train the model, calculate probabilities, and classify text as either 'spam' or 'ham' based on a given dataset in CSV format.

## Prerequisites

- Python 3.x
- Required Python packages: `csv`

## File Structure

- `spam_detection.py`: The main Python script containing all necessary functions for the Naive Bayes spam detection.
- `SpamDetection.csv`: Sample CSV file containing labeled sentences to train and test the spam detection system.

## How to Use

1. **Prepare the Dataset:**
   - Ensure your dataset is in CSV format with labeled sentences (where 'Label' represents the category and 'Sentence' contains the text).

2. **Understanding the Functions:**

   - `getDataFromCSV(fileName)`: Reads the CSV file and splits the dataset into training and testing sets.
   - `getWordCount(trainingSet)`: Determines the number of unique words in the training set.
   - `calcProbabilities(trainingSet)`: Calculates the prior probabilities for 'spam' and 'ham'.
   - `trainingModel(trainingSet)`: Trains the model and constructs dictionaries for 'spam' and 'ham' words.
   - `classifyData(testingSet, priorSpamProb, priorHamProb, spamDict, hamDict, wordCount)`: Classifies the test data and computes posterior probabilities for 'spam' and 'ham'.
   - `main()`: Orchestrates the entire process by calling the functions in the correct order and displays the accuracy of the predictions.

3. **Run the Script:**
   - Update the `fileName` variable in the `main()` function to point to your CSV file.
   - Execute the script using Python (`python spam_detection.py`).

## Important Notes

- The `SpamDetection.csv` file must follow the specified format (Label, Sentence).
- The training and testing sets are segregated based on the 20-item threshold for the training set. Adjust this value as needed.
- The script calculates probabilities using the Naive Bayes algorithm and prints out predictions and their accuracies.

## Example Usage

```bash
python spam_detection.py
