# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from django.forms import ModelForm


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=64)
    active = models.BooleanField(default = True)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'company_name', 'active']

class DeactivateItem(forms.Form):
    id = forms.IntegerField()

class UpdateProjectForm(forms.Form):
    id = forms.IntegerField()
    new_project_name = forms.CharField(max_length=64)


    
