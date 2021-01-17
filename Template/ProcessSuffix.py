import itertools
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
    persons = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 3'][start]

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
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def processBasic():

    cartesianProduct2(2, 9)
    cartesianProduct2(11, 18)
    cartesianProduct2(20, 27)
    cartesianProduct(29, 36)
    cartesianProduct(38, 45)
    cartesianProduct(47, 54)

    saveSentences(actualSentences, 'Suffix', 'SuffixBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'Suffix', 'SuffixBasicTrue')


def processWordOder():
    cartesianProductWo2(58, 65)
    cartesianProductWo2(67, 74)
    cartesianProductWo2(76, 83)
    cartesianProductWo(85, 92)
    cartesianProductWo(94, 101)
    cartesianProductWo(103, 110)

    saveSentences(actualSentences, 'Suffix', 'SuffixWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'Suffix', 'SuffixWordOrderVariationsTrue')


def processNeg():
    cartesianProductNeg2(115, 122)
    cartesianProductNeg2(124, 131)
    cartesianProductNeg2(133, 140)
    cartesianProductNeg(142, 149)
    cartesianProductNeg(151, 158)
    cartesianProductNeg(160, 167)

    saveSentences(actualSentences, 'Suffix', 'SuffixNegIn')
    saveWordsAndTags(actualWords, actualTags, 'Suffix', 'SuffixNegTrue')


if __name__ == '__main__':

    templateDf = pd.read_csv('Suffix/Checklist - suffix.csv', sep=';', encoding='utf-8')

    actualSentences = []
    actualWords = []
    actualTags = []

    processBasic()
    processWordOder()
    processNeg()
