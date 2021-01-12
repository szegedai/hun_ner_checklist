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


def readLines(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].fillna(method='ffill').dropna(axis=1, how='all')

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
        actualSentences.append(' '.join(generatedSentence))
        appendLine()


def cartesianProduct(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    persons1 = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    persons2 = templateDf['Unnamed: 3'][start:finish] + ' ' + templateDf['Unnamed: 4'][start]

    cartesianSentence = []
    for sentence in itertools.product(persons1, persons2):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
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
    print(tags)
    print(df.head())
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
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProduct3(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    print(tags)
    print(df.head())
    words = templateDf['Basic cases'][start:start+2]
    miscs = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]

    cartesianSentence = []
    for sentence in itertools.product(words, miscs):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProduct4(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    print(tags)
    print(df.head())
    words = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start]
    borgs = templateDf['Unnamed: 2'][start:finish]
    iorgs1 = templateDf['Unnamed: 3'][start:start+4]
    iorgs2 = templateDf['Unnamed: 4'][start:finish]

    cartesianSentence = []
    for sentence in itertools.product([words], borgs, iorgs1, iorgs2):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
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
    print(tags)
    print(df.head())
    words = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start] \
            + ' ' + templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]
    borgs = templateDf['Unnamed: 4'][start:finish]
    iorgs1 = templateDf['Unnamed: 5'][start:start+4]
    iorgs2 = templateDf['Unnamed: 6'][start:finish]

    cartesianSentence = []
    for sentence in itertools.product([words], borgs, iorgs1, iorgs2):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProduct5(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    print(tags)
    print(df.head())
    words = templateDf['Unnamed: 4'][start]
    borgs = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    iorgs1 = templateDf['Unnamed: 2'][start:start+4]
    iorgs2 = templateDf['Unnamed: 3'][start:finish]

    cartesianSentence = []
    for sentence in itertools.product(borgs, iorgs1, iorgs2, [words]):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


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
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


def cartesianProduct7(start, finish):
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    print(tags)
    print(df.head())
    persons1 = templateDf['Basic cases'][start:finish]
    persons2 = templateDf['Unnamed: 1'][start:finish] + ' ' + templateDf['Unnamed: 2'][start]  + ' ' + templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]
    words = templateDf['Unnamed: 5'][start:start+4]

    cartesianSentence = []
    for sentence in itertools.product(persons1, persons2, words):
        cartesianSentence.append(' '.join(sentence) + ' .')

    for sentence in cartesianSentence:
        actualSentences.append(sentence)
        print(sentence)
        for word in sentence.split():
            # print(word)
            actualWords.append(word)

        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        appendLine()


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

