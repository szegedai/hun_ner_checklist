import itertools
from TemplateWriter import *


def cartesianProduct4(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    words = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start]
    borgs = templateDf['Unnamed: 2'][start:finish]
    iorgs1 = templateDf['Unnamed: 3'][start:start+4]
    iorgs2 = templateDf['Unnamed: 4'][start:finish]

    generatedSentences = []
    for sentence in itertools.product([words], borgs, iorgs1, iorgs2):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProduct5(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    words = templateDf['Unnamed: 4'][start]
    borgs = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    iorgs1 = templateDf['Unnamed: 2'][start:start+4]
    iorgs2 = templateDf['Unnamed: 3'][start:finish]

    generatedSentences = []
    for sentence in itertools.product(borgs, iorgs1, iorgs2, [words]):
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
    df = templateDf[start:finish].dropna(axis=1, how='all')
    print(tags)
    print(df.head())
    words = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]
    borgs = templateDf['Unnamed: 4'][start:finish]
    iorgs1 = templateDf['Unnamed: 5'][start:start+4]
    iorgs2 = templateDf['Unnamed: 6'][start:finish]

    generatedSentences = []
    for sentence in itertools.product([words], borgs, iorgs1, iorgs2):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def processBasic():

    cartesianProduct4(3, 10)
    cartesianProduct4(13, 20)
    cartesianProduct4(24, 31)
    cartesianProduct4(34, 41)

    saveSentences(actualSentences, 'MFT_mwe', 'MFT_mweBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT_mwe', 'MFT_mweBasicTrue')


def processWo():

    cartesianProduct5(47, 54)
    cartesianProduct5(57, 64)
    cartesianProduct5(68, 75)
    cartesianProduct5(78, 85)

    saveSentences(actualSentences, 'MFT_mwe', 'MFT_mweWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT_mwe', 'MFT_mweWordOrderVariationsTrue')


def processNeg():

    cartesianProductNeg(91, 98)
    cartesianProductNeg(101, 108)
    cartesianProductNeg(111, 118)
    cartesianProductNeg(121, 128)

    saveSentences(actualSentences, 'MFT_mwe', 'MFT_mweNegIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT_mwe', 'MFT_mweNegTrue')


if __name__ == '__main__':
    templateDf = pd.read_csv('MFT_mwe/Checklist - mft_mwe.csv', sep=';', encoding='utf-8')

    actualWords = []
    actualTags = []
    actualSentences = []

    processBasic()
    processWo()
    processNeg()
