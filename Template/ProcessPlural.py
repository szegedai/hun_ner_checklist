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
            # print(word)
            actualWords.append(word)
            generatedSentence.append(word)
        for tag in tags:
            # print(tag)
            actualTags.append(tag)
        print(' '.join(generatedSentence))
        actSentences.append(' '.join(generatedSentence))
        appendLine()


def cartesianProduct(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 1'][start]

    actualSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
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
    locations = templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    word = templateDf['Unnamed: 2'][start]

    actualSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        actualSentences.append('A ' + ' '.join(sentence) + ' .')

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
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 1'][start:finish]
    word = templateDf['Unnamed: 2'][start]

    actualSentences = []
    for sentence in itertools.product(locations, persons, [str(word)]):
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
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 3'][start]

    actualSentences = []
    for sentence in itertools.product(locations, persons, [str(word)]):
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
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    word = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start]

    actualSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
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
    locations = 'A ' + templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 4'][start:finish]
    word = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    actualSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
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
    readLines(2, 7)
    readLines(9, 14)
    readLines(16, 21)
    readLines(23, 28)
    readLines(30, 40)
    readLines(42, 52)

    saveSentences(actSentences, 'Plural', 'PluralBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'Plural', 'PluralBasicTrue')


def processWordOder():
    readLines(57, 62)
    readLines(64, 69)
    readLines(71, 76)
    readLines(78, 83)
    readLines(85, 95)
    readLines(97, 107)

    saveSentences(actSentences, 'Plural', 'PluralWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'Plural', 'PluralWordOrderVariationsTrue')


def processNeg():
    readLines(112, 117)
    readLines(119, 124)
    readLines(126, 131)
    readLines(133, 138)
    readLines(140, 150)
    readLines(152, 162)

    saveSentences(actSentences, 'Plural', 'PluralNegIn')
    saveWordsAndTags(actualWords, actualTags, 'Plural', 'PluralNegTrue')


if __name__ == '__main__':

    templateDf = pd.read_csv('Plural/Checklist - plural.csv', sep=';', encoding='utf-8')

    actSentences = []
    actualWords = []
    actualTags = []

    processBasic()
    processWordOder()
    processNeg()



