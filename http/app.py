# -*- coding: utf-8 -*-
"""
@File    :  app.py
@Time    :  2022/5/13 7:50
@Author  :  TangToChild
@Version :  1.0
@Contact :  mayitrust@gmail.com
@Desc    :  None
"""
import random

from flask import Flask
from flask import request
from flask import jsonify
import torch

import model.mocha
from model.model import ChatBot

import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False # 配置编码显示中文

chatBot = ChatBot('../modelGenshin.pkl', device=torch.device('cuda'))


@app.route('/', methods=['GET', 'POST'])
def index():
    msg = request.values.get('msg')
    print('msg = ', msg)
    # 先检索
    outputSeq, len_ans = model.mocha.get_retrieval_ans(msg, 5)
    if len_ans > 0:
        reply = random.choice(outputSeq)
    else:
        reply = chatBot.predictByBeamSearch(msg, isRandomChoose=True, allRandomChoose=False, showInfo=False)
    print('reply = ', reply)
    return jsonify({'reply': str(reply)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)