import itertools
from TemplateReader import readLines
from TemplateWriter import *


def cartesianProduct(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 1'][start]

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


def cartesianProduct2(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    word = templateDf['Unnamed: 2'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        generatedSentences.append('A ' + ' '.join(sentence) + ' .')

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

    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 1'][start:finish]
    word = templateDf['Unnamed: 2'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, persons, [str(word)]):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)
        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductWo2(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start:finish]
    persons = 'a ' + templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 3'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, persons, [str(word)]):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductNeg(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    word = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductNeg2(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = 'A ' + templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 4'][start:finish]
    word = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            actualWords.append(word)
        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def processDetBasic():

    cartesianProduct(2, 8)
    cartesianProduct2(12, 19)
    readLines(21, 26, templateDf, actualWords, actualTags, actualSentences)
    readLines(28, 33, templateDf, actualWords, actualTags, actualSentences)
    readLines(35, 38, templateDf, actualWords, actualTags, actualSentences)
    readLines(41, 42, templateDf, actualWords, actualTags, actualSentences)
    readLines(44, 49, templateDf, actualWords, actualTags, actualSentences)
    readLines(51, 55, templateDf, actualWords, actualTags, actualSentences)
    readLines(57, 58, templateDf, actualWords, actualTags, actualSentences)
    readLines(61, 66, templateDf, actualWords, actualTags, actualSentences)
    readLines(68, 72, templateDf, actualWords, actualTags, actualSentences)
    readLines(74, 75, templateDf, actualWords, actualTags, actualSentences)

    saveSentences(actualSentences, 'Determiner', 'DeterminerBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'Determiner', 'DeterminerBasicTrue')


def processDetWordOder():

    cartesianProductWo(81, 88)
    cartesianProductWo2(91, 98)
    readLines(91, 98, templateDf, actualWords, actualTags, actualSentences)
    readLines(100, 105, templateDf, actualWords, actualTags, actualSentences)
    readLines(107, 112, templateDf, actualWords, actualTags, actualSentences)
    readLines(114, 118, templateDf, actualWords, actualTags, actualSentences)
    readLines(120, 121, templateDf, actualWords, actualTags, actualSentences)
    readLines(123, 128, templateDf, actualWords, actualTags, actualSentences)
    readLines(136, 137, templateDf, actualWords, actualTags, actualSentences)
    readLines(140, 145, templateDf, actualWords, actualTags, actualSentences)
    readLines(147, 151, templateDf, actualWords, actualTags, actualSentences)
    readLines(153, 154, templateDf, actualWords, actualTags, actualSentences)

    saveSentences(actualSentences, 'Determiner', 'DeterminerWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'Determiner', 'DeterminerWordOrderVariationsTrue')


def processDetNeg():
    cartesianProductNeg(160, 167)
    cartesianProductNeg2(170, 177)
    readLines(179, 184, templateDf, actualWords, actualTags, actualSentences)
    readLines(186, 191, templateDf, actualWords, actualTags, actualSentences)
    readLines(193, 197, templateDf, actualWords, actualTags, actualSentences)
    readLines(199, 200, templateDf, actualWords, actualTags, actualSentences)
    readLines(202, 207, templateDf, actualWords, actualTags, actualSentences)
    readLines(209, 213, templateDf, actualWords, actualTags, actualSentences)
    readLines(215, 216, templateDf, actualWords, actualTags, actualSentences)
    readLines(219, 224, templateDf, actualWords, actualTags, actualSentences)
    readLines(226, 230, templateDf, actualWords, actualTags, actualSentences)
    readLines(232, 233, templateDf, actualWords, actualTags, actualSentences)

    saveSentences(actualSentences, 'Determiner', 'DeterminerNegIn')
    saveWordsAndTags(actualWords, actualTags, 'Determiner', 'DeterminerNegTrue')


if __name__ == '__main__':

    templateDf = pd.read_csv('Determiner/Checklist - determiner.csv', sep=';',  encoding='utf-8')

    actualWords = []
    actualTags = []
    actualSentences = []

    processDetBasic()
    processDetWordOder()
    processDetNeg()
