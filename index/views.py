# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.db import models


from . import models, dbhelper, forms


class Index(View):

    def get(self, request):
        if not models.Project.objects.all():
            print 'no query'
            context = {
                'project': models.ProjectForm()
            }
        else:
            print 'with query'
            context = {
                'project': models.ProjectForm(),
                'projects': list(models.Project.objects.all())
            }
        return render(request, 'index/indextemplate.html', context=context)

    def post(self, request):
        form = models.ProjectForm(request.POST)
        if form.is_valid() and dbhelper.does_project_exist(form.clean()):
            form.save()
        else:
            return HttpResponse(500)

        context = {
            'project': models.ProjectForm(),
            'projects': list(models.Project.objects.all())
        }
        return render(request, 'index/indextemplate.html', context=context)


class DeleteItem(View):

    def get(self, request):
        if not models.Project.objects.all():
            print 'no query'
            context = {
                'delete_project': forms.Delete_Project()
            }
        else:
            print 'with query'
            context = {
                'delete_project': forms.Delete_Project(),
                'projects': list(models.Project.objects.all())
            }
        return render(request, 'index/deltemplate.html', context=context)


    # def post(self, request):