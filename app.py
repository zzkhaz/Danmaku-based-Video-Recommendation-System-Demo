# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
import recommend
import json
app=Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index/')
def index():
    name=request.args.get('user')
    if name == 'guest':
        dic = recommend.DefineRecommend()
        return render_template('index.html',Data=dic)
    dic=recommend.UserRecommend(name)
    return render_template('index.html',Data=dic)

@app.route('/bangumi/<bangumiID>')
def BangumiRecommend(bangumiID):
    web = bangumiID + '.html'
    data=recommend.BangumiRecommend(bangumiID)
    return render_template(web,Data=data)

if __name__=="__main__":
    app.run(debug=True)