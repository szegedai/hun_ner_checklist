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
    persons = templateDf['Unnamed: 4'][start:start+4]
    word = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        generatedSentences.append(templateDf['Basic variations'][start] + ' ' + ' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProduct3(start, finish, taxNum):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic variations'][start:finish]
    persons = templateDf['Unnamed: 2'][start:finish]
    words = templateDf['Unnamed: 1'][start:start+taxNum]

    generatedSentences = []
    for sentence in itertools.product(locations, words, persons):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProduct32(start, finish, taxNum):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic variations'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    words = templateDf['Unnamed: 2'][start:start+taxNum]

    generatedSentences = []
    for sentence in itertools.product(locations, words, persons):
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
    locations = templateDf['Basic variations'][start:start+4]
    persons = templateDf['Unnamed: 1'][start:finish]
    word = templateDf['Unnamed: 2'][start:finish]

    generatedSentences = []
    for sentence in itertools.product(locations, persons, word):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductWo2(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Unnamed: 4'][start:finish]
    persons = templateDf['Unnamed: 1'][start:start + 4]
    word = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    generatedSentences = []
    for sentence in itertools.product(persons, [str(word)], locations):
        generatedSentences.append(templateDf['Basic variations'][start] + ' ' + ' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductWo3(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic variations'][start:start+4]
    persons = templateDf['Unnamed: 1'][start:finish]
    word = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start:finish]

    generatedSentences = []
    for sentence in itertools.product(locations, persons, word):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductNeg(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic variations'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    words = templateDf['Unnamed: 2'][start:start+4]

    generatedSentences = []
    for sentence in itertools.product(locations, words, persons):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductNeg2(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic variations'][start] + ' ' + templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    persons = templateDf['Unnamed: 4'][start:finish]
    words = templateDf['Unnamed: 3'][start:start+4]

    generatedSentences = []
    for sentence in itertools.product(locations, words, persons):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductNeg3(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic variations'][start] \
                + ' ' + templateDf['Unnamed: 1'][start:finish] + ' ' + templateDf['Unnamed: 2'][start] \
                + ' ' + templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start] \
                + ' ' + templateDf['Unnamed: 5'][start]
    persons = templateDf['Unnamed: 6'][start:start+4]

    generatedSentences = []
    for sentence in itertools.product(locations, persons):
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
    cartesianProduct2(12, 19)
    cartesianProduct3(21, 28, 4)
    cartesianProduct32(30, 37, 4)
    readLines(40, 45, templateDf, actualWords, actualTags, actualSentences)
    readLines(47, 52, templateDf, actualWords, actualTags, actualSentences)

    saveSentences(actualSentences, 'SLR', 'SLRBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'SLR', 'SLRBasicTrue')


def processWordOder():
    cartesianProductWo2(57, 64)
    cartesianProductWo2(67, 74)
    cartesianProductWo(76, 83)
    cartesianProductWo3(85, 92)
    readLines(95, 100, templateDf, actualWords, actualTags, actualSentences)
    readLines(102, 107, templateDf, actualWords, actualTags, actualSentences)

    saveSentences(actualSentences, 'SLR', 'SLRWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'SLR', 'SLRWordOrderVariationsTrue')


def processNeg():

    cartesianProductNeg3(112, 119)
    cartesianProductNeg3(122, 129)
    cartesianProductNeg(131, 138)
    cartesianProductNeg2(140, 147)
    readLines(150, 155, templateDf, actualWords, actualTags, actualSentences)
    readLines(157, 161, templateDf, actualWords, actualTags, actualSentences)
    
    saveSentences(actualSentences, 'SLR', 'SLRNegIn')
    saveWordsAndTags(actualWords, actualTags, 'SLR', 'SLRNegTrue')


if __name__ == '__main__':

    templateDf = pd.read_csv('SLR/Checklist - slr.csv', sep=';', encoding='utf-8')

    actualSentences = []
    actualWords = []
    actualTags = []

    processBasic()
    processWordOder()
    processNeg()
