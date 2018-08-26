#!usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, make_response, jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)

@app.route('book/search/<q>/<page>')
def search(q,page):
    """
    q : 普通关键字 isbn
    page：
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if is_isbn_or_key() == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
        # API
    return jsonify(result)