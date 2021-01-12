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
    actualSentences.clear()


def readLines(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    # print(tags)
    df = templateDf[start:finish].fillna(method='ffill').dropna(axis=1, how='all')
    # print(df.head())

    for sentence in df.iloc:
        generatedSentence = []
        # print(sentence)
        for word in sentence:
            # print(word)
            actualWords.append(word)
            generatedSentence.append(word)
        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        print(' '.join(generatedSentence))
        actualSentences.append(' '.join(generatedSentence))
        appendLine()


def cartesianProduct(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(tags)
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 1'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        generatedSentences.append(' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        print(sentence)
        actualSentences.append(sentence)
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
    locations = templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    word = templateDf['Unnamed: 2'][start]

    generatedSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        generatedSentences.append('A ' + ' '.join(sentence) + ' .')

    for sentence in generatedSentences:
        print(sentence)
        actualSentences.append(sentence)
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
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 1'][start:finish]
    word = templateDf['Unnamed: 2'][start]

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
        appendLine()


def cartesianProductWo2(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic cases'][start:finish]
    persons = 'a ' +templateDf['Unnamed: 2'][start:finish]
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
        appendLine()


def cartesianProductNeg(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
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
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def processDetBasic():

    cartesianProduct(2, 8)
    cartesianProduct2(12, 19)
    readLines(21, 26)
    readLines(28, 33)
    readLines(35, 38)
    readLines(41, 42)
    readLines(44, 49)
    readLines(51, 55)
    readLines(57, 58)
    readLines(61, 66)
    readLines(68, 72)
    readLines(74, 75)

    saveSentences(actualSentences, 'Determiner', 'DeterminerBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'Determiner', 'DeterminerBasicTrue')


def processDetWordOder():

    cartesianProductWo(81, 88)
    cartesianProductWo2(91, 98)
    readLines(91, 98)
    readLines(100, 105)
    readLines(107, 112)
    readLines(114, 118)
    readLines(120, 121)
    readLines(123, 128)
    readLines(136, 137)
    readLines(140, 145)
    readLines(147, 151)
    readLines(153, 154)

    saveSentences(actualSentences, 'Determiner', 'DeterminerWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'Determiner', 'DeterminerWordOrderVariationsTrue')


def processDetNeg():
    cartesianProductNeg(160, 167)
    cartesianProductNeg2(170, 177)
    readLines(179, 184)
    readLines(186, 191)
    readLines(193, 197)
    readLines(199, 200)
    readLines(202, 207)
    readLines(209, 213)
    readLines(215, 216)
    readLines(219, 224)
    readLines(226, 230)
    readLines(232, 233)

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



