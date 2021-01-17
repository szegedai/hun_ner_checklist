import itertools
from TemplateWriter import *


def cartesianProduct5(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    persons1 = templateDf['Basic cases'][start:finish]
    persons2 = templateDf['Unnamed: 1'][start:finish] + ' ' + templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]
    words = templateDf['Unnamed: 4'][start:start+4]

    cartesianSentence = []
    for sentence in itertools.product(persons1, persons2, words):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProduct6(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    print(tags)
    print(df.head())
    persons1 = templateDf['Basic cases'][start:finish]
    persons2 = templateDf['Unnamed: 1'][start:finish] + ' ' + templateDf['Unnamed: 2'][start]
    words = templateDf['Unnamed: 3'][start:start+4] + ' ' + templateDf['Unnamed: 4'][start]

    cartesianSentence = []
    for sentence in itertools.product(persons1, persons2, words):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProduct7(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    persons1 = templateDf['Basic cases'][start:finish]
    persons2 = templateDf['Unnamed: 1'][start:finish] + ' ' + templateDf['Unnamed: 2'][start]  + ' ' + templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]
    words = templateDf['Unnamed: 5'][start:start+4]

    cartesianSentence = []
    for sentence in itertools.product(persons1, persons2, words):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def processBasic():

    cartesianProduct5(4, 9)
    cartesianProduct5(12, 17)

    saveSentences(actualSentences, 'MFT_adj', 'MFT_adjBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT_adj', 'MFT_adjBasicTrue')


def processWo():

    cartesianProduct6(22, 27)
    cartesianProduct6(30, 35)

    saveSentences(actualSentences, 'MFT_adj', 'MFT_adjWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT_adj', 'MFT_adjWordOrderVariationsTrue')


def processNeg():

    cartesianProduct7(40, 45)
    cartesianProduct7(48, 53)

    saveSentences(actualSentences, 'MFT_adj', 'MFT_adjNegIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT_adj', 'MFT_adjNegTrue')


if __name__ == '__main__':
    templateDf = pd.read_csv('MFT_adj/Checklist - mft_adj.csv', sep=';', encoding='utf-8')

    actualWords = []
    actualTags = []
    actualSentences = []

    processBasic()
    processWo()
    processNeg()
