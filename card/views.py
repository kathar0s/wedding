# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    template_data = {
        'message': 'hello',
    }

    return render(request, 'index.html', template_data)


def userinfo(request):

    template_data = {
        'message': 'hello',
    }

    return render(request, 'userinfo.html', template_data)


def chat(request):

    template_data = {
        'message': 'hello',
    }

    return render(request, 'chat.html', template_data)
