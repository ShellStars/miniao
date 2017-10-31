# coding:utf-8
"""
    author:Lindow
    date:2017/10/22
"""
from django.shortcuts import render_to_response, render
def index(request):
    return render(request, 'index.html')
