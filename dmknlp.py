# -*-coding=utf-8-*-

from QcloudApi.qcloudapi import QcloudApi
import json
import os

def dmknlp(dmk):
    module = "wenzhi"
    action = "TextSentiment"

    config = {
        "Region": "sh",
        "secretId": "AKID9RRAblEDahX6OPqmolZ7OO6Xgnlevjvr",
        "secretKey": "nWJr8WfZMt99tMiy3ra4HCYnmUxMVOCo",
        "method": "get"
    }

    params = {
        "content": dmk,
        "type": 4
    }
    
    service = QcloudApi(module, config)
    print service.generateUrl(action, params)
    s =  service.call(action, params)
    try:
        dejson =  json.loads(s)
        negative = dejson["negative"]
        positive = dejson["positive"]
        emotion  = (positive - negative)*5
        return emotion
    except Exception, e:
        print "exception:", e
        return 0

def getDmkEmotion(filename):
    n = 0
    dmk_emotion = 0
    for dmk in open(filename):
        dmk = dmk.strip('\n')
        dmk_emotion = dmk_emotion + float(dmknlp(dmk))
        n = n + 1
    return dmk_emotion/n
    
 
def ListFilesToTxt(dir,file,wildcard,recursion):  
    exts = wildcard.split(" ")  
    files = os.listdir(dir)
    for name in files:  
        fullname=os.path.join(dir,name)  
        if(os.path.isdir(fullname) & recursion):  
            ListFilesToTxt(fullname,file,wildcard,recursion)  
        else:  
            for ext in exts:  
                if(name.endswith(ext)):  
                    file.write(name )
                    file.write('\n')
                    break  
  
def loadDmk():  
    dir="C:\\Users\\zzkha\\Desktop\\dmkspider\\dmktxt"  
    outfile="list.txt"  
    wildcard = ".txt"
    bangumiData = []
    file = open(outfile,"w")  
    if not file:  
        print ("cannot open the file %s for writing" % outfile)   
    ListFilesToTxt(dir,file,wildcard, 1)      
    file.close()
    for filename in open("list.txt"):
        filename = filename.strip('\n')
        emotion = getDmkEmotion(filename)
        dic = {}
        dic['cid'] = filename
        dic['emotion'] = emotion
        bangumiData.append(dic)
    print bangumiData
  
    

if __name__ == "__main__":
    loadDmk()
        
