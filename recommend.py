# -*-coding=utf-8-*-
import svd
import json
from compiler.ast import flatten


def UserRecommend(name):
    u = json.load(open("data.json"),"GB2312")
    i = 0
    try:
        for z in range(1,len(u['user'])):
            if u['user'][z]['name'] == name:
                i = z
    except: print 'err'
    temp = svd.svd()
    userDmkForm = temp[i]
    a = [abs(x - int(u['user'][i]['dmk_log'])) for x in userDmkForm]
    result1 = a.index(min(a))
    result1 = u['bangumi'][result1]['title']
    result2 = findmin(a,1)
    result2 = u['bangumi'][result2]['title'] 
    result3 = findmin(a,2)
    result3 = u['bangumi'][result3]['title']
    result4 = findmin(a,3)
    result4 = u['bangumi'][result4]['title']
    result = []
    result.append(result1)
    result.append(result2)
    result.append(result3)
    result.append(result4)
    return result
    
'''
def BangumiRecommend(bid):
    print bid
    u = json.load(open("data.json"),"GB2312")
    i = 0
    l = []
    for z in range(0,20):
        l.append(u['bangumi'][z]['emotion'])
        if u['bangumi'][z]['bid'] == int(bid):
            i = z
    print FindClose(l,float(u['bangumi'][i]['emotion']))
    a = [abs(x - float(u['bangumi'][i]['emotion'])) for x in l]
    result1 = findmin(a,2)
    result1 = u['bangumi'][result1]['title']
    result2 = findmin(a,3)
    result2 = u['bangumi'][result2]['title'] 
    result3 = findmin(a,4)
    result3 = u['bangumi'][result3]['title']
    result4 = findmin(a,5)
    result4 = u['bangumi'][result4]['title']
    result = []
    result.append(result1)
    result.append(result2)
    result.append(result3)
    result.append(result4)
    return result
'''

def BangumiRecommend(bid):
    print bid
    u = json.load(open("data.json"),"GB2312")
    i = 0
    k = 0
    l = []
    for z in range(0,20):
        l.append(u['bangumi'][z]['emotion'])
        if u['bangumi'][z]['bid'] == int(bid):
            i = z
            k = u['bangumi'][z]['emotion']
    print k,i
    foo = lambda s:s['emotion']  
    m = u['bangumi'][:]
    m = sorted(u['bangumi'], key=foo)  
    for z in range(0,20):
        if m[z]['emotion'] == u['bangumi'][i]['emotion']:
            print m[z]['emotion'],u['bangumi'][i]['emotion'],u['bangumi'][i]['title']
            k = z
    if k+1 < 20:
        result1 = m[k+1]['title']
    else:
        result1 = 'None'
    if k-1 > -1:
        result2 = m[k-1]['title']
    else:
        result2 = 'None'
    if k-2 > -1:
        result3 = m[k-2]['title']
    else:
        result3 = 'None'
    if k+2 < 20:
        result4 = m[k+2]['title']
    else:
        result4 = 'None'
    result = []
    result.append(result1)
    result.append(result2)
    result.append(result3)
    result.append(result4)
    return result
    
    
def DefineRecommend():
    u = json.load(open("data.json"),"GB2312")
    l = []
    l.append(u['bangumi'][0]['title'])
    l.append(u['bangumi'][1]['title'])
    l.append(u['bangumi'][2]['title'])
    l.append(u['bangumi'][3]['title'])
    return l

def FindClose(arr, e):
    low = 0
    high = len(arr) - 1
    idx = -1
    while low <= high:
        mid = (low + high) / 2
        if e == arr[mid] or mid == low:
            idx = mid
            break
        elif e > arr[mid]:
            low = mid
        elif e < arr[mid]:
            high = mid
    if idx + 1 < len(arr) and abs(e - arr[idx]) > abs(e - arr[idx + 1]):
        idx += 1
    return idx


def findmin(l,n):
    i = 0
    for i in range(0,n):
        del l[l.index(min(l))]
    return l.index(min(l))
        

#BangumiRecommend('5800')


