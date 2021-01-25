# -*- coding: utf-8 -*-

"""
Created on 1/24/21 6:43 PM
@Author  : Justin Jiang
@Email   : jw_jiang@pku.edu.com
"""

from flask import Flask

"""
Flask需要创建一个应用实例，将接受自客户端的所有请求都转交给这个对象处理
Web服务器使用一种名为Web服务器网关接口（WSGI，Web server gateway interface）的协议
Flask类的构造函数只有一个必须制定的参数，即应用主模块或者包的名字，大多数应用中Python的__name__变量就是所需的值
Flask用传参确定应用的位置，进而找到应用中其他文件的位置。
"""
app = Flask(__name__)  # 找到执行目录


# 路由：处理URL和函数之间关系的程序
# 可以直接使用Flask应用中提供的app.route装饰器
@app.route('/')
def index():
    return "<h1>Hello World!</h1>"


@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)
