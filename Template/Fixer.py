def tagFixer(tags):
    if tags[0] != '0':
        newTag = tags[0].replace('B', 'I')
        tags[0] = newTag

    for i in range(1, len(tags)):
        if tags[i][0] == 'B' and tags[i-1] == '0':
            newTag = tags[i].replace('B', 'I')
            tags[i] = newTag
        elif tags[i][0] == 'B' and tags[i-1] != '0':
            if tags[i][1:4] != tags[i-1][1:4]:
                newTag = tags[i].replace('B', 'I')
                tags[i] = newTag

    return tags
