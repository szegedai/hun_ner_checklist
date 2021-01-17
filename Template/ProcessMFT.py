import itertools
from TemplateReader import readLines
from TemplateWriter import *


def cartesianProduct(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    persons1 = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    persons2 = templateDf['Unnamed: 3'][start:finish] + ' ' + templateDf['Unnamed: 4'][start]

    cartesianSentence = []
    for sentence in itertools.product(persons1, persons2):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:

            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProduct2(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    orgs = templateDf['Basic cases'][start:finish]
    persons1 = templateDf['Unnamed: 3'][start:finish-1]
    persons2 = templateDf['Unnamed: 4'][start:finish - 1]
    words1 = templateDf['Unnamed: 1'][start:start+4] + ' ' + templateDf['Unnamed: 2'][start]
    words2 = templateDf['Unnamed: 5'][start] + ' ' + templateDf['Unnamed: 6'][start] + ' ' + templateDf['Unnamed: 7'][start] + ' ' + templateDf['Unnamed: 8'][start] + ' ' + templateDf['Unnamed: 9'][start]

    cartesianSentence = []
    for sentence in itertools.product(orgs, words1, persons1, persons2, [words2]):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProduct3(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    words = templateDf['Basic cases'][start:start+2]
    miscs = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]

    cartesianSentence = []
    for sentence in itertools.product(words, miscs):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProduct4(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    words = templateDf['Basic cases'][start:start+2]
    borgs = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    iorgs1 = templateDf['Unnamed: 3'][start:start+4]
    iorgs2 = templateDf['Unnamed: 4'][start:finish]

    cartesianSentence = []
    for sentence in itertools.product(words, borgs, iorgs1, iorgs2):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


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
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:

            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def processBasic():

    cartesianProduct(2, 9)
    cartesianProduct2(13, 23)
    readLines(27, 37, templateDf, actualWords, actualTags, actualSentences)
    readLines(40, 50, templateDf, actualWords, actualTags, actualSentences)
    cartesianProduct3(53, 68)
    cartesianProduct4(70, 77)
    cartesianProduct4(80, 87)
    cartesianProduct5(90, 95)
    cartesianProduct5(98, 102)

    saveSentences(actualSentences, 'MFT', 'MFTBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT', 'MFTBasicTrue')


if __name__ == '__main__':
    templateDf = pd.read_csv('MFT/Checklist - mft.csv', sep=';', encoding='utf-8')

    actualWords = []
    actualTags = []
    actualSentences = []

    processBasic()
