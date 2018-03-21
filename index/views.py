# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
from django.views import View


class Index(View):

    def get(self, request):
        context = {
            'project': models.Project()
        }
        print render(request, 'index/indextemplate.html', context=context)
        return render(request, 'index/indextemplate.html', context=context)

    def post(self, request):
        return render(request, 'indextemplate.html', context=context)
