from seqeval.metrics import accuracy_score
from seqeval.metrics import classification_report
from seqeval.metrics import f1_score
import pandas as pd
import os
import shutil
from Fixer import tagFixer, tagFixer2


def getF1Score(name, variation):

    print("Beginning {} {}".format(name, variation))

    dfTrue = pd.read_csv('Texts/{0}/{0}{1}True.txt'.format(name, variation), delimiter='\s+', index_col=False, encoding='utf-8', header=None).dropna()
    dfTrue.columns = ['word', 'tag']
    dfPred = pd.read_csv('Texts/{0}/{0}{1}Out.txt'.format(name, variation), sep='\t', engine='python', encoding='utf-8', header=None).dropna()
    dfPred.columns = ['word', 'tag']

    y_true = dfTrue['tag']
    y_pred = tagFixer(tagFixer2(dfPred['tag']))
    print(y_true[0:5])
    print(y_pred[0:5])

    open('Texts/{0}/{0}{1}Report.txt'.format(name, variation), "w").close()
    f = open('Texts/{0}/{0}{1}Report.txt'.format(name, variation), 'w')
    f.write('f1-score: {}'.format(f1_score(y_true, y_pred)))
    f.write('\n')
    f.write(classification_report(y_true, y_pred))
    f.close()
    print("{} {} done!".format(name, variation))


def runEvals():
    testCases = ['Determiner', 'Plural', 'PostPositions', 'SLR', 'Suffix', 'Taxonomy', 'MFT_adj', 'MFT_mwe', 'MFT_voc']
    variations = ['Basic', 'Neg', 'WordOrderVariations']

    for testCase in testCases:
        for variation in variations:
            getF1Score(testCase, variation)


def copyFiles():
    testCases = ['Determiner', 'Plural', 'PostPositions', 'SLR', 'Suffix', 'Taxonomy', 'MFT_adj', 'MFT_mwe', 'MFT_voc']
    variations1 = ['Basic', 'Neg', 'WordOrderVariations']
    variations2 = ['Out', 'True', 'Report']

    for testCase in testCases:
        os.makedirs('Results/{}'.format(testCase))
        for variation1 in variations1:
            for variation2 in variations2:
                shutil.copy('Texts/{0}/{0}{1}{2}.txt'.format(testCase, variation1, variation2), 'Results/{}/'.format(testCase), follow_symlinks=True)


def renameFiles():
    path = 'E:\\Projects\\Szakdoga\\CRF3\\all_true_hubert'
    for count, filename in enumerate(os.listdir(path)):
        dst = filename[0:-8] + 'Out.txt'
        src = filename

        os.rename(path + '\\' + src, path + '\\' + dst)


if __name__ == '__main__':
    runEvals()
    copyFiles()
