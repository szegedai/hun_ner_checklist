import itertools
from TemplateReader import readLines
from TemplateWriter import *


def cartesianProduct(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]

    persons1 = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    persons2 = templateDf['Unnamed: 3'][start:finish] + ' ' + templateDf['Unnamed: 4'][start]

    generatedSentences = []
    for sentence in itertools.product(persons1, persons2):
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
    orgs = templateDf['Basic cases'][start:finish]
    persons1 = templateDf['Unnamed: 3'][start:finish-1]
    persons2 = templateDf['Unnamed: 4'][start:finish - 1]
    words1 = templateDf['Unnamed: 1'][start:start+4] + ' ' + templateDf['Unnamed: 2'][start]
    words2 = templateDf['Unnamed: 5'][start] + ' ' + templateDf['Unnamed: 6'][start] + ' ' + templateDf['Unnamed: 7'][start] + ' ' + templateDf['Unnamed: 8'][start] + ' ' + templateDf['Unnamed: 9'][start]

    generatedSentences = []
    for sentence in itertools.product(orgs, words1, persons1, persons2, [words2]):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
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

    generatedSentences = []
    for sentence in itertools.product(words, miscs):
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

    persons1 = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start]\
                + ' ' + templateDf['Unnamed: 2'][start]\
                + ' ' + templateDf['Unnamed: 3'][start:finish]
    persons2 = templateDf['Unnamed: 4'][start:finish]

    generatedSentences = []
    for sentence in itertools.product(persons1, persons2):
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
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    orgs = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    persons1 = templateDf['Unnamed: 5'][start:finish - 1]
    persons2 = templateDf['Unnamed: 6'][start:finish - 1]
    words1 = templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]
    words2 = templateDf['Unnamed: 7'][start] + ' ' + templateDf['Unnamed: 8'][start] + ' ' + templateDf['Unnamed: 9'][start]

    generatedSentences = []
    for sentence in itertools.product(orgs, [words1], persons1,  persons2, [words2]):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductWo3(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    words = templateDf['Unnamed: 2'][start:start+2]
    miscs = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]

    generatedSentences = []
    for sentence in itertools.product(miscs, words):
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
    persons1 = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start]  + ' ' + templateDf['Unnamed: 2'][start]  + ' ' + templateDf['Unnamed: 3'][start:finish]
    persons2 = templateDf['Unnamed: 4'][start:finish] + ' ' + templateDf['Unnamed: 5'][start]

    generatedSentences = []
    for sentence in itertools.product(persons1, persons2):
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

    orgs = templateDf['Basic cases'][start:finish]
    persons1 = templateDf['Unnamed: 3'][start:finish-1]
    persons2 = templateDf['Unnamed: 4'][start:finish - 1]
    words1 = templateDf['Unnamed: 1'][start:start+4] + ' ' + templateDf['Unnamed: 2'][start]
    words2 = templateDf['Unnamed: 5'][start] + ' ' + templateDf['Unnamed: 6'][start] + ' ' + templateDf['Unnamed: 7'][start] + ' ' + templateDf['Unnamed: 8'][start] + ' ' + templateDf['Unnamed: 9'][start] + ' ' + templateDf['Unnamed: 10'][start]

    generatedSentences = []
    for sentence in itertools.product(orgs, words1, persons1, persons2, [words2]):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductNeg3(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    words = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:start+2]
    miscs = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start:finish]

    generatedSentences = []
    for sentence in itertools.product(words, miscs):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
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

    saveSentences(actualSentences, 'MFT_voc', 'MFT_vocBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT_voc', 'MFT_vocBasicTrue')


def processWo():

    cartesianProductWo(73, 80)
    cartesianProductWo2(84, 94)
    readLines(98, 108, templateDf, actualWords, actualTags, actualSentences)
    readLines(111, 121, templateDf, actualWords, actualTags, actualSentences)
    cartesianProductWo3(124, 139)

    saveSentences(actualSentences, 'MFT_voc', 'MFT_vocWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT_voc', 'MFT_vocWordOrderVariationsTrue')


def processNeg():

    cartesianProductNeg(144, 151)
    cartesianProductNeg2(155, 165)
    readLines(169, 179, templateDf, actualWords, actualTags, actualSentences)
    readLines(182, 192, templateDf, actualWords, actualTags, actualSentences)
    cartesianProductNeg3(195, 210)

    saveSentences(actualSentences, 'MFT_voc', 'MFT_vocNegIn')
    saveWordsAndTags(actualWords, actualTags, 'MFT_voc', 'MFT_vocNegTrue')


if __name__ == '__main__':
    templateDf = pd.read_csv('MFT_voc/Checklist - mft_voc.csv', sep=';', encoding='utf-8')

    actualWords = []
    actualTags = []
    actualSentences = []

    processBasic()
    processWo()
    processNeg()
