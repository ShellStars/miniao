# coding:utf-8
"""
    author:Lindow
    date:2017/10/22
"""
from django.shortcuts import render_to_response, render
def test(request):
    return render(request, 'test.html')
