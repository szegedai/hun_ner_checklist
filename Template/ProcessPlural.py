from TemplateReader import readLines
from TemplateWriter import *


def processBasic():
    readLines(2, 7, templateDf, actualWords, actualTags, actualSentences)
    readLines(9, 14, templateDf, actualWords, actualTags, actualSentences)
    readLines(16, 21, templateDf, actualWords, actualTags, actualSentences)
    readLines(23, 28, templateDf, actualWords, actualTags, actualSentences)
    readLines(30, 40, templateDf, actualWords, actualTags, actualSentences)
    readLines(42, 52, templateDf, actualWords, actualTags, actualSentences)

    saveSentences(actualSentences, 'Plural', 'PluralBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'Plural', 'PluralBasicTrue')


def processWordOder():
    readLines(57, 62, templateDf, actualWords, actualTags, actualSentences)
    readLines(64, 69, templateDf, actualWords, actualTags, actualSentences)
    readLines(71, 76, templateDf, actualWords, actualTags, actualSentences)
    readLines(78, 83, templateDf, actualWords, actualTags, actualSentences)
    readLines(85, 95, templateDf, actualWords, actualTags, actualSentences)
    readLines(97, 107, templateDf, actualWords, actualTags, actualSentences)

    saveSentences(actualSentences, 'Plural', 'PluralWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'Plural', 'PluralWordOrderVariationsTrue')


def processNeg():
    readLines(112, 117, templateDf, actualWords, actualTags, actualSentences)
    readLines(119, 124, templateDf, actualWords, actualTags, actualSentences)
    readLines(126, 131, templateDf, actualWords, actualTags, actualSentences)
    readLines(133, 138, templateDf, actualWords, actualTags, actualSentences)
    readLines(140, 150, templateDf, actualWords, actualTags, actualSentences)
    readLines(152, 162, templateDf, actualWords, actualTags, actualSentences)

    saveSentences(actualSentences, 'Plural', 'PluralNegIn')
    saveWordsAndTags(actualWords, actualTags, 'Plural', 'PluralNegTrue')


if __name__ == '__main__':

    templateDf = pd.read_csv('Plural/Checklist - plural.csv', sep=';', encoding='utf-8')

    actualSentences = []
    actualWords = []
    actualTags = []

    processBasic()
    processWordOder()
    processNeg()



