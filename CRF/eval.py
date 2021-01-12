from seqeval.metrics import accuracy_score
from seqeval.metrics import classification_report
from seqeval.metrics import f1_score
import pandas as pd
import os
import shutil


def getF1Score(name, variation):

    dfTrue = pd.read_csv('Texts/{0}/{0}{1}True.txt'.format(name, variation), delimiter='\s+', index_col=False, header=None).dropna()
    dfTrue.columns = ['word', 'tag']

    dfPred = pd.read_csv('Texts/{0}/{0}{1}Out.txt'.format(name, variation), delimiter='\s+', index_col=False, header=None).dropna()
    dfPred.columns = ['word', 'tag']

    y_true = dfTrue['tag']
    y_pred = dfPred['tag']

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
            print("Beginning {} {}".format(testCase, variation))
            os.system('cmd /c "java -Xmx3G -jar ner.jar -mode predicate '
                      '-input Texts/{0}/{0}{1}In.txt '
                      '-output Texts/{0}/{0}{1}Out.txt"'.format(testCase, variation))
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


if __name__ == '__main__':
    runEvals()
    copyFiles()