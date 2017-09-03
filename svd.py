#!/usr/bin/python2.7
# -*-coding=utf-8-*-
import numpy as np  
from scipy.sparse.linalg import svds  
from scipy import sparse  
import matplotlib.pyplot as plt
import json

def getData():
    j = open("dmk.json")
    a = json.load(j)
    j = open("data.json") 
    b = json.load(j,"GB2312")
    multilist = [[0 for col in range(20)] for row in range(10)]
    for i in range(0,10):
        for m in range(0,len(a['data'][i]['dmk_log'])):
            for n in range(0,20):
                x = str(a['data'][i]['dmk_log'][m]['video'])
                y = str(b['bangumi'][n]['bid'])
                if  x == y:
                    multilist[i][n] = a['data'][i]['dmk_log'][m]['dmkEmotion']
    return multilist

def vector_to_diagonal(vector):  
    if (isinstance(vector, np.ndarray) and vector.ndim == 1) or \
            isinstance(vector, list):
        length = len(vector)
        diag_matrix = np.zeros((length, length))
        np.fill_diagonal(diag_matrix, vector)
        return diag_matrix
    return None
def svd():
    RATE_MATRIX = np.array(getData())
    '''
    RATE_MATRIX = np.array(
        [[4.56,0,0,0,0,2.65,0,-1.58,0,-0.89],
         [0,1.22,0,1.78,0,0,0,0,0,3.45],
         [0,0,-4.22,0,0,0,0.66,0,0,0],
         [0,0.89,-3.13,0,0,0,0,0,0.06,0],
         [-3.56,0,0,-2.35,0,0,1.58,0,0,-0.12],
         [0,-0.76,-0.58,0,0,0,0,0,1.05,0],
         [0,0.13,0,0.88,2.33,-1.79,0,0,0,-2.22],
         [0,2.35,0.69,0,3.45,0,0,0,2.18,0]]
        )
    '''
    RATE_MATRIX = RATE_MATRIX.astype('float')  
    U, S, VT = svds(sparse.csr_matrix(RATE_MATRIX),  k=2, maxiter=200) 
    S = vector_to_diagonal(S)
    X = np.dot(np.dot(U, S), VT) * (RATE_MATRIX < 1e-6)
#    print '用户-弹幕分部'
#    print RATE_MATRIX
#    print '用户的主题分部：'  
#    print U  
#    print '奇异值：'  
#    print S  
#    print '弹幕的主题分部：'  
#    print VT  
#    print '重建评分矩阵，并过滤掉已经评分的物品：'  
#    print X
    return X