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


def cartesianProductSpec1(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 4'][start:start+2]
    word = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

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


def cartesianProductSpec2(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    #print(df.head())
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 4'][start:start+2]
    word = templateDf['Unnamed: 1'][start:start+2]
    word2 = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    actualSentences = []
    for sentence in itertools.product(locations, word, [str(word2)], persons):
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
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:start+2]
    persons = templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]

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
    locations = templateDf['Basic cases'][start] + ' ' + templateDf['Unnamed: 1'][start:start+2]
    persons = templateDf['Unnamed: 2'][start:finish]
    word = templateDf['Unnamed: 3'][start:start+2]
    word2 = templateDf['Unnamed: 4'][start]

    actualSentences = []
    for sentence in itertools.product(locations, persons, word, [str(word2)]):
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
    persons = templateDf['Unnamed: 5'][start:start+2]
    word = templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]

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
    locations = templateDf['Basic cases'][start:finish]
    persons = templateDf['Unnamed: 5'][start:start+2]
    word = templateDf['Unnamed: 1'][start:start+2]
    word2 = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start]

    actualSentences = []
    for sentence in itertools.product(locations, word, [str(word2)], persons):
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

    cartesianProductSpec1(2, 9)
    cartesianProductSpec2(12, 19)

    saveSentences(actSentences, 'PostPositions', 'PostPositionsBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'PostPositions', 'PostPositionsBasicTrue')


def processWordOder():
    cartesianProductWo(25, 32)
    cartesianProductWo2(35, 42)

    saveSentences(actSentences, 'PostPositions', 'PostPositionsWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'PostPositions', 'PostPositionsWordOrderVariationsTrue')


def processNeg():
    cartesianProductNeg(47, 54)
    cartesianProductNeg2(57, 64)

    saveSentences(actSentences, 'PostPositions', 'PostPositionsNegIn')
    saveWordsAndTags(actualWords, actualTags, 'PostPositions', 'PostPositionsNegTrue')


if __name__ == '__main__':

    templateDf = pd.read_csv('PostPositions/Checklist - postpositions.csv', sep=';', encoding='utf-8')

    actSentences = []
    actualWords = []
    actualTags = []

    processBasic()
    processWordOder()
    processNeg()



