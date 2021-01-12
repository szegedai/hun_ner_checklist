import pandas as pd
import itertools
import numpy as np
from Fixer import tagFixer


def appendLine():
    actualTags.append(' ')
    actualWords.append(' ')


def saveWordsAndTags(words, tags, name, name2):
    outDf = pd.DataFrame()
    outDf['Words'] = words
    outDf['Tags'] = tagFixer(tags)
    np.savetxt(r'{}/{}.txt'.format(name, name2), outDf.values, fmt='%s', encoding='utf-8')
    words.clear()
    tags.clear()


def saveSentences(sentences, name, name2):
    crfInDf = pd.DataFrame()
    crfInDf['Sentences'] = sentences
    np.savetxt(r'{}/{}.txt'.format(name, name2), crfInDf.values, fmt='%s', encoding='utf-8')
    actSentences.clear()


def readLines(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    #print(tags)
    df = templateDf[start:finish].fillna(method='ffill').dropna(axis=1, how='all')
    #print(df.head())

    for sentence in df.iloc:
        generatedSentence = []
        # print(sentence)
        for word in sentence:
            print(word)
            actualWords.append(word)
            generatedSentence.append(word)
        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        # print(' '.join(generatedSentence))
        actSentences.append(' '.join(generatedSentence))
        appendLine()


def cartesianProduct(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 2'][start:finish]
    words = templateDf['Unnamed: 1'][start:start+4]

    actualSentences = []
    for sentence in itertools.product(locations, words, persons):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in actualSentences:
        actSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProduct2(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    words = templateDf['Unnamed: 2'][start:start+4]

    actualSentences = []
    for sentence in itertools.product(locations, words, persons):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in actualSentences:
        actSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProduct3(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    miscs = templateDf['Basic cases'][start:finish]
    words = templateDf['Unnamed: 1'][start:start+3]
    words2 = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    actualSentences = []
    for sentence in itertools.product(miscs, words, [words2]):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in actualSentences:
        actSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProductWo(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Unnamed: 2'][start:finish]
    persons = templateDf['Unnamed: 1'][start:finish]
    words = templateDf['Basic cases'][start:start+4]

    actualSentences = []
    for sentence in itertools.product(words, persons, locations):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in actualSentences:
        actSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProductWo2(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start:finish]
    persons = templateDf['Unnamed: 1'][start:finish]
    words = templateDf['Basic cases'][start:start+4]

    actualSentences = []
    for sentence in itertools.product(words, persons, locations):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in actualSentences:
        actSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProductWo3(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    miscs = templateDf['Unnamed: 3'][start:finish]
    words = templateDf['Unnamed: 2'][start:start+3]
    words2 = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start]

    actualSentences = []
    for sentence in itertools.product([words2], words, miscs):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in actualSentences:
        actSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProductNeg(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    words = templateDf['Unnamed: 2'][start:start+4]

    actualSentences = []
    for sentence in itertools.product(locations, words, persons):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in actualSentences:
        actSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProductNeg2(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    persons = templateDf['Unnamed: 4'][start:finish]
    words = templateDf['Unnamed: 3'][start:start+4]

    actualSentences = []
    for sentence in itertools.product(locations, words, persons):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in actualSentences:
        actSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProductNeg3(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    miscs = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    words = templateDf['Unnamed: 2'][start:start+3]
    words2 = templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]

    actualSentences = []
    for sentence in itertools.product(miscs, words, [words2]):
        actualSentences.append(' '.join(sentence) + ' .')

    for sentence in actualSentences:
        actSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def processBasic():
    cartesianProduct(3, 10)
    cartesianProduct2(12, 19)
    cartesianProduct3(21, 26)

    saveSentences(actSentences, 'Taxonomy', 'TaxonomyBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'Taxonomy', 'TaxonomyBasicTrue')


def processWordOder():

    cartesianProductWo(31, 38)
    cartesianProductWo2(40, 47)
    cartesianProductWo3(49, 54)

    saveSentences(actSentences, 'Taxonomy', 'TaxonomyWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'Taxonomy', 'TaxonomyWordOrderVariationsTrue')


def processNeg():
    cartesianProductNeg(61, 68)
    cartesianProductNeg2(70, 77)
    cartesianProductNeg3(79, 84)
    saveSentences(actSentences, 'Taxonomy', 'TaxonomyNegIn')
    saveWordsAndTags(actualWords, actualTags, 'Taxonomy', 'TaxonomyNegTrue')


if __name__ == '__main__':

    templateDf = pd.read_csv('Taxonomy/Checklist - taxonomy.csv', sep=';', encoding='utf-8')

    actSentences = []
    actualWords = []
    actualTags = []

    processBasic()
    processWordOder()
    processNeg()



