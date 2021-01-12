"""
egy utófeldolgozó scripttel is átalakíthatod, az a szabály, hogy minden esetbe “B-“-t “I-“-re cserélünk, kivéve ha a megelöző szó címkéje ugyanaz volt
6:06
tehát most így nézne ki Vera jelölésében:
6:07
jelentette   0
be   0
Egerben B-LOC
India  B-LOC
budapesti    0
nagykövete   0
Jóska   B-PER
Piska    I-PER
6:07
ebből az kell legyen, hogy:
6:08
elentette   0
be   0
Egerben I-LOC
India B-LOC
budapesti   0
nagykövete   0
Jóska  I-PER
Piska   I-PER
6:08
azaz Eger és Jóska címkéjében B- cseréje I-re, Indiában nem, mert a megelöző címke szintén LOC volt
"""


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


if __name__ == '__main__':
    tags = ['0', '0', 'B-LOC', 'B-LOC', '0', '0', 'B-PER', 'I-PER']
    print(tagFixer(tags))

