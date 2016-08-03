# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:06:22 2016

@author: YI
"""

import numpy as np

def loaddataset():
    plist = [['my','dog','has','flea','problems','help','please'],
             ['maybe','not','take','him','to','dog','park','stupid'],
             ['my','dalmation','is','so','cute','I','love','him'],
             ['stop','posting','stupid','worthless','garbage'],
             ['mr','licks','ate','my','steak','how','to','stop','him'],
             ['quit','buying','worthless','dog','food','stupid']]
    classvec = [0,1,0,1,0,1]
    return plist, classvec

def createVocabList(dataset):
    vocabSet = set([])
    for i in dataset:
        vocabSet = vocabSet | set(i)
    return list(vocabSet)
    
def setOfWords2Vec(vocabList, inputset):
    vec = [0] * len(vocabList)
    for word in inputset:
        if word in vocabList:
            vec[vocabList.index(word)] = 1
        else:
            print 'the word: %s is not in my list.' % word
    return vec
    
def bagOfWords2Vec(vocabList, inputset):
    returnVec = [0] * len(vocabList)
    for word in inputset:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec
    
def createMatrix(dataset, vocablist):
    mat = []
    for inputset in dataset:
        mat.append(setOfWords2Vec(vocablist, inputset))
    return mat

def trainNB(mat, category):
    m, n= np.shape(mat)
    pClass1 = sum(category) / float(m)
    p0Num = np.zeros(n)
    p1Num = np.zeros(n)
    p0Denom = 0.0
    p1Denom = 0.0
    for i in range(m):
        if category[i] == 1:
            p1Num += mat[i]
            p1Denom += 1
        else:
            p0Num += mat[i]
            p0Denom += 1
    p1vec = np.log(p1Num / p1Denom)
    p0vec = np.log(p0Num / p0Denom)
    return p1vec, p0vec, pClass1
    
def classifyNB(vec2Classify, p1vec, p0vec, pClass1):
    p1 = sum(vec2Classify * p1vec) + log(pClass1)
    p0 = sum(vec2Classify * p0vec) + log(1-pClass1)
    if p1 > p0:
        return 1
    else:
        return 0
        

    


dataset, classvec=loaddataset()
vocablist=createVocabList(dataset)
mat=createMatrix(dataset,vocablist)
p1,p2,pc=trainNB(mat,classvec)

