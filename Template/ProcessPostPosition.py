import itertools
from TemplateWriter import *


def cartesianProductSpec1(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 4'][start:start+2]
    word = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductSpec2(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 4'][start:start+2]
    word = templateDf['Unnamed: 1'][start:start+2]
    word2 = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, word, [str(word2)], persons):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductWo(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:start+2]
    persons = templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, persons, [str(word)]):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductWo2(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:start+2]
    persons = templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 3'][start:start+2]
    word2 = templateDf['Unnamed: 4'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, persons, word, [str(word2)]):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductNeg(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 5'][start:start+2]
    word = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductNeg2(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 5'][start:start+2]
    word = templateDf['Unnamed: 1'][start:start+2]
    word2 = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, word, [str(word2)], persons):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        generatedSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def processBasic():

    cartesianProductSpec1(2, 9)
    cartesianProductSpec2(12, 19)

    saveSentences(actualSentences, 'PostPositions', 'PostPositionsBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'PostPositions', 'PostPositionsBasicTrue')


def processWordOder():
    cartesianProductWo(25, 32)
    cartesianProductWo2(35, 42)

    saveSentences(actualSentences, 'PostPositions', 'PostPositionsWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'PostPositions', 'PostPositionsWordOrderVariationsTrue')


def processNeg():
    cartesianProductNeg(47, 54)
    cartesianProductNeg2(57, 64)

    saveSentences(actualSentences, 'PostPositions', 'PostPositionsNegIn')
    saveWordsAndTags(actualWords, actualTags, 'PostPositions', 'PostPositionsNegTrue')


if __name__ == '__main__':

    templateDf = pd.read_csv('PostPositions/Checklist - postpositions.csv', sep=';', encoding='utf-8')

    actualSentences = []
    actualWords = []
    actualTags = []

    processBasic()
    processWordOder()
    processNeg()
