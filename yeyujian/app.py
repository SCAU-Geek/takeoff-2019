#!/usr/bin/env python3
# coding:utf-8
# __author__ = 'YYJ'

from flask import Flask,jsonify
from flask import request, Response
from decorator import catch_error, check_url_params
from getClass import getNextCourse
import json

app = Flask(__name__,static_url_path='')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    # return "hello"
    return app.send_static_file("index.html")



@app.route('/getclass',methods=['POST'])
@catch_error
@check_url_params
def getClass():
    return jsonify(getNextCourse(request.form.get('name'),request.form.get('passwd')))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True, threaded=True)