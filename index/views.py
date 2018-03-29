# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.db import models
from django.contrib import messages


from . import models, dbhelper, forms, testmodels


class Index(View):

    def get(self, request):
        if not models.Project.objects.all():
            context = {
                'project': models.ProjectForm()
            }
        else:
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


class DBtest(View):

    def get(self, request):
        '''
        c1 = testmodels.Company(company_name='c1')
        c1.save()
        u1 = testmodels.Us3r(name='user1', email='email@email.com', company=c1)
        u2 = testmodels.Us3r(name='user2', email='email@email.com', company=c1)
        u3 = testmodels.Us3r(name='user3', email='email@email.com', company=c1)
        u1.save()
        u2.save()
        u3.save()
        g1 = testmodels.Gr0up(company=c1)
        g1.save()
        g1.users.add(u1, u2, u3)
        g1.save()
        p1 = testmodels.Pr0ject(project_name='Icarus', company=c1)
        p1.save()
        p1.groups.add(g1)
        p1.save()
        '''
        print len(list(testmodels.Pr0ject.objects.all()))

        context = {
            'companies': list(testmodels.Company.objects.all()),
            'users': list(testmodels.Us3r.objects.all()),
            'groups': list(testmodels.Gr0up.objects.all()),
            'projects': list(testmodels.Pr0ject.objects.all()),
            'indent': ' ',
        }

        return render(request, 'index/testtemplate.html', context=context)


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
        return render(request, 'index/deactivateItemTemplate.html',
                      context=context)

    def post(self, request):
        form = models.DeactivateItem(request.POST)
        if form.is_valid():
            id = form.clean().get('project')
            obj = models.Project.objects.get(id=id)
            if not obj.active:
                messages.info(request, 'Project {} has already been deactivated'.format(obj.project_name))
            else:
                obj.active = False
                obj.save()

            context = {
                'delete_project': models.DeactivateItem(),
                'projects': list(models.Project.objects.all())
            }
            return render(request, 'index/deactivateItemTemplate.html',
                          context=context)


class updateCompany(View):
    
    def get(self, request):
        context = {
            'updateform': models.UpdateCompanyForm(),
            'projects': list(models.Project.objects.all()),
        }
        return render(request, 'index/updateCompanyTemplate.html',
                      context=context)

    def post(self, request):
        form = models.UpdateCompanyForm(request.POST)

        if form.is_valid():
            id = form.clean().get('id')
            project = models.Project.objects.get(
                id=form.clean().get('project'))
            project.company_name = form.clean().get('new_company_name')
            project.save()

        context = {
            'updateform': models.UpdateCompanyForm(),
            'projects': list(models.Project.objects.all()),
        }

        return render(request, 'index/updateCompanyTemplate.html',
                     context=context)

class setActive(View):
    def get(self, request):
        context = {
            'delete_project': models.ActiveForm(),
            'projects': list(models.Project.objects.all())
        }
        return render(request, 'index/setActivetemplate.html',
                      context=context)

    def post(self, request):
        form = models.ActiveForm(request.POST)
        if form.is_valid():
            id = form.clean().get('project')
            project = models.Project.objects.get(id=id)
            print form.clean().get('active')
            if form.clean().get('active'):
                project.active = True
            else:
                project.active = False
            project.save()

        context = {
            'delete_project': models.ActiveForm(),
            'projects': list(models.Project.objects.all())
        }
        return render(request, 'index/setActivetemplate.html',
                      context=context)


class UpdateProjectName(View):

    def get(self, request):
        context = {
            'updateform': models.UpdateProjectForm(),
            'projects': list(models.Project.objects.all()),
        }
        return render(request, 'index/updateProjectTemplate.html',
                      context=context)

    def post(self, request):
        form = models.UpdateProjectForm(request.POST)
        if form.is_valid():
            print form.clean().get('project')
            project = models.Project.objects.get(id=form.clean().get('project'))
            project.project_name = form.clean().get('new_project_name')
            project.save()

        context = {
            'updateform': models.UpdateProjectForm(),
            'projects': list(models.Project.objects.all()),
        }

        return render(request, 'index/updateProjectTemplate.html',
                      context=context)
