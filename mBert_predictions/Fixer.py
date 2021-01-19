def tagFixer(tags):
    if tags[0] != '0':
        newTag = tags[0].replace('B', 'I')
        tags[0] = newTag

    for i in range(1, len(tags)):
        if tags[i][0] == 'B' and tags[i-1] == 'O':
            newTag = tags[i].replace('B', 'I')
            tags[i] = newTag
        elif tags[i][0] == 'B' and tags[i-1] != 'O':
            if tags[i][1:4] != tags[i-1][1:4]:
                newTag = tags[i].replace('B', 'I')
                tags[i] = newTag

    return tags


def tagFixer2(tags):
    for i in range(0, len(tags)):
        if tags[i] != 'O':
            if tags[i][0:2] == 'E-':
                newTag = 'I' + tags[i][1:len(tags[i])]
                tags[i] = newTag
            elif tags[i][0:2] == '1-':
                newTag = tags[i].replace('1', 'B')
                tags[i] = newTag

    return tags

