import itertools
from TemplateWriter import *


def cartesianProduct(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 2'][start:finish]
    words = templateDf['Unnamed: 1'][start:start + 4]

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


def cartesianProduct2(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    words = templateDf['Unnamed: 2'][start:start + 4]

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


def cartesianProduct3(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    miscs = templateDf['Basic cases'][start:finish]
    words = templateDf['Unnamed: 1'][start:start + 3]
    words2 = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    generatedSentences = []
    for sentence in itertools.product(miscs, words, [words2]):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def cartesianProductWo(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Unnamed: 2'][start:finish]
    persons = templateDf['Unnamed: 1'][start:finish]
    words = templateDf['Basic cases'][start:start + 4]

    generatedSentences = []
    for sentence in itertools.product(words, persons, locations):
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
    locations = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start:finish]
    persons = templateDf['Unnamed: 1'][start:finish]
    words = templateDf['Basic cases'][start:start + 4]

    generatedSentences = []
    for sentence in itertools.product(words, persons, locations):
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
    miscs = templateDf['Unnamed: 3'][start:finish]
    words = templateDf['Unnamed: 2'][start:start + 3]
    words2 = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start]

    generatedSentences = []
    for sentence in itertools.product([words2], words, miscs):
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
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    words = templateDf['Unnamed: 2'][start:start + 4]

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
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    persons = templateDf['Unnamed: 4'][start:finish]
    words = templateDf['Unnamed: 3'][start:start + 4]

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


def cartesianProductNeg3(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    miscs = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    words = templateDf['Unnamed: 2'][start:start + 3]
    words2 = templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]

    generatedSentences = []
    for sentence in itertools.product(miscs, words, [words2]):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        actualSentences.append(sentence)
        for word in sentence.split():
            actualWords.append(word)

        for tag in tags:
            actualTags.append(tag)
        appendLine(actualTags, actualWords)


def processBasic():
    cartesianProduct(3, 10)
    cartesianProduct2(12, 19)
    cartesianProduct3(21, 26)

    saveSentences(actualSentences, 'Taxonomy', 'TaxonomyBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'Taxonomy', 'TaxonomyBasicTrue')


def processWordOder():
    cartesianProductWo(31, 38)
    cartesianProductWo2(40, 47)
    cartesianProductWo3(49, 54)

    saveSentences(actualSentences, 'Taxonomy', 'TaxonomyWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'Taxonomy', 'TaxonomyWordOrderVariationsTrue')


def processNeg():
    cartesianProductNeg(61, 68)
    cartesianProductNeg2(70, 77)
    cartesianProductNeg3(79, 84)

    saveSentences(actualSentences, 'Taxonomy', 'TaxonomyNegIn')
    saveWordsAndTags(actualWords, actualTags, 'Taxonomy', 'TaxonomyNegTrue')


if __name__ == '__main__':
    templateDf = pd.read_csv('Taxonomy/Checklist - taxonomy.csv', sep=';', encoding='utf-8')

    actualSentences = []
    actualWords = []
    actualTags = []

    processBasic()
    processWordOder()
    processNeg()
