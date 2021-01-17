def readLines(start, finish, templateDf, actualWords, actualTags, actualSentences):
    tagsDf = templateDf[start-1:start].dropna(axis=1, how='all').values.tolist()
    tags = tagsDf[0]
    df = templateDf[start:finish].fillna(method='ffill').dropna(axis=1, how='all')

    for sentence in df.iloc:
        generatedSentence = []
        for word in sentence:
            actualWords.append(word)
            generatedSentence.append(word)
        for tag in tags:
            actualTags.append(tag)

        actualSentences.append(' '.join(generatedSentence))
        actualTags.append(' ')
        actualWords.append(' ')
