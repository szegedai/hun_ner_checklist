def readfile(filename):
    '''
    read file
    '''
    f = open(filename)
    data = []
    sentence = []
    label= []
    for line in f:
        line = line.lstrip()
        if len(line)==0 or line.startswith('-DOCSTART') or line[0]=="\n":
            if len(sentence) > 0:
                data.append((sentence,label))
                sentence = []
                label = []
            continue
        splits = line.split()
        sentence.append(splits[0].lower())
        label.append(splits[1])
    if len(sentence) >0:
        data.append((sentence,label))
        sentence = []
        label = []
    return data

def inv_test(Cap, InvTest):
    gs    = readfile(BASEDIR+Cap+'/'+Cap+'BasicTrue.txt')
    basic = readfile(BASEDIR+Cap+'/'+Cap+'BasicOut.txt')
    inv   = readfile(BASEDIR+Cap+'/'+Cap+InvTest+'Out.txt')
    if len(basic) != len(gs):
        print('Hiba:',Cap,InvTest)
        return

    n=fail=0
    for sent in inv:
        s = base_sentence(gs, sent[0])
        if s<0:
            print('base pár nem található')
            continue
        for i in range(len(gs[s][0])):
            if gs[s][1][i] != 'O':
                base_label = basic[s][1][i]
                #if base_label[-3:] != gs[s][1][i][-3:]:
                #    continue
                ne = gs[s][0][i]
                try:
                    inv_label = sent[1][ sent[0].index(ne) ]
                except ValueError:
                    print(ne, 'nincs', gs[s][0], sent[0])
                    continue
                n=n+1
                if base_label != inv_label:
                    fail=fail+1

    print(Cap,InvTest, fail/n, fail, '/', n)

def base_match_check(Cap, InvTest):
    gs    = readfile(BASEDIR+Cap+'/'+Cap+'BasicTrue.txt')
    inv   = readfile(PREDDIR+Cap+'/'+Cap+InvTest+'Out.txt')
    for s in inv:
        base_sentence(gs, s[0])

def base_sentence(gs, sent):
    min = 999999
    for i in range(len(gs)):
        s = gs[i][0]
        if len(s) > len(sent):
            continue
        d = len( set(sent) - set(s) )
        if len( set(s) - set(sent) ) == 1:
            sub=0
            for w in set(sent) - set(s):
                if w in list(set(s) - set(sent))[0]:
                    sub =sub+1
            if sub == 2:
                d = d-2
        if d < min :
            min = d
            arg_min = i
    if min>1:
        print(sent, gs[arg_min][0])
        return -1
    return arg_min

BASEDIR='./NEresults/'
PREDDIR='./all_true_mbert/'
#inv_test('Suffix','Neg')
for c in ['Determiner','Plural','PostPositions','SLR','Suffix','Taxonomy','MFT_voc','MFT_mwe','MFT_adj']:
  for inv in ['WordOrderVariations', 'Neg']:
      print(c,inv)
      inv_test(c,inv)
