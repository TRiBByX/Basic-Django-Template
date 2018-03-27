# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.db import models
from django.contrib import messages


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


class DeactivateItem(View):

    def get(self, request):
        if not models.Project.objects.all():
            print 'no query'
            context = {
                'delete_project': models.DeactivateItem()
            }
        else:
            print 'with query'
            context = {
                'delete_project': models.DeactivateItem(),
                'projects': list(models.Project.objects.all())
            }
        return render(request, 'index/deactivateItemTemplate.html', context=context)


    def post(self, request):
        form = models.DeactivateItem(request.POST)
        if form.is_valid():
            id = form.clean().get('id')
            obj = models.Project.objects.get(id=id)
            if obj.active == False:
                messages.info(request, 'Project {} has already been deactivated'.format(obj.project_name))
            else:
                obj.active = False
                obj.save()
                
            context = {
                'delete_project': models.DeactivateItem(),
                'projects': list(models.Project.objects.all())
            }
            return render(request, 'index/deactivateItemTemplate.html', context=context)