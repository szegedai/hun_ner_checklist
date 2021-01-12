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
    persons = templateDf['Unnamed: 4'][start:start+4]
    word = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    actualSentences = []
    for sentence in itertools.product(locations, [str(word)], persons):
        actualSentences.append(templateDf['Basic variations'][start] + ' ' + ' '.join(sentence) + ' .')

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


def cartesianProduct3(start, finish, taxNum):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic variations'][start:finish]
    persons = templateDf['Unnamed: 2'][start:finish]
    words = templateDf['Unnamed: 1'][start:start+taxNum]

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


def cartesianProduct32(start, finish, taxNum):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    #print(tags)
    # print(df.head())
    locations = templateDf['Basic variations'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
    persons = templateDf['Unnamed: 3'][start:finish]
    words = templateDf['Unnamed: 2'][start:start+taxNum]

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


def cartesianProductWo(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic variations'][start:start+4]
    persons = templateDf['Unnamed: 1'][start:finish]
    word = templateDf['Unnamed: 2'][start:finish]

    actualSentences = []
    for sentence in itertools.product(locations, persons, word):
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


def cartesianProductWo22(start, finish):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic variations'][start:start+4]
    persons = templateDf['Unnamed: 1'][start:finish]
    word = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start:finish]

    actualSentences = []
    for sentence in itertools.product(locations, persons, word):
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
    tagsDf = templateDf[start - 1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Unnamed: 4'][start:finish]
    persons = templateDf['Unnamed: 1'][start:start + 4]
    word = templateDf['Unnamed: 2'][start] + ' ' + templateDf['Unnamed: 3'][start]

    actualSentences = []
    for sentence in itertools.product(persons, [str(word)], locations):
        actualSentences.append(templateDf['Basic variations'][start] + ' ' + ' '.join(sentence) + ' .')

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
    locations = templateDf['Basic variations'][start] + ' ' + templateDf['Unnamed: 1'][start:finish]
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
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].dropna(axis=1, how='all')
    # print(df.head())
    locations = templateDf['Basic variations'][start] + ' ' + templateDf['Unnamed: 1'][start] + ' ' + templateDf['Unnamed: 2'][start:finish]
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
    locations = templateDf['Basic variations'][start] \
                + ' ' + templateDf['Unnamed: 1'][start:finish] + ' ' + templateDf['Unnamed: 2'][start] \
                + ' ' + templateDf['Unnamed: 3'][start] + ' ' + templateDf['Unnamed: 4'][start] \
                + ' ' + templateDf['Unnamed: 5'][start]
    persons = templateDf['Unnamed: 6'][start:start+4]

    actualSentences = []
    for sentence in itertools.product(locations, persons):
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
    cartesianProduct2(2, 9)
    cartesianProduct2(12, 19)
    cartesianProduct3(21, 28, 4)
    cartesianProduct32(30, 37, 4)
    readLines(40, 45)
    readLines(47, 52)

    saveSentences(actSentences, 'SLR', 'SLRBasicIn')
    saveWordsAndTags(actualWords, actualTags, 'SLR', 'SLRBasicTrue')


def processWordOder():
    cartesianProductWo2(57, 64)
    cartesianProductWo2(67, 74)
    cartesianProductWo(76, 83)
    cartesianProductWo22(85, 92)
    readLines(95, 100)
    readLines(102, 107)

    saveSentences(actSentences, 'SLR', 'SLRWordOrderVariationsIn')
    saveWordsAndTags(actualWords, actualTags, 'SLR', 'SLRWordOrderVariationsTrue')


def processNeg():

    cartesianProductNeg3(112, 119)
    cartesianProductNeg3(122, 129)
    cartesianProductNeg(131, 138)
    cartesianProductNeg2(140, 147)
    readLines(150, 155)
    readLines(157, 161)
    saveSentences(actSentences, 'SLR', 'SLRNegIn')
    saveWordsAndTags(actualWords, actualTags, 'SLR', 'SLRNegTrue')


if __name__ == '__main__':

    templateDf = pd.read_csv('SLR/Checklist - slr.csv', sep=';', encoding='utf-8')

    actSentences = []
    actualWords = []
    actualTags = []

    processBasic()
    processWordOder()
    processNeg()



