# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from django.forms import ModelForm


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=64)
    active = models.BooleanField(default=True)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'company_name', 'active']


class ActiveForm(forms.Form):
    project = forms.ChoiceField(choices=[])
    active = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(ActiveForm, self).__init__(*args, **kwargs)
        self.fields['project'].choices = [(p.id, p.project_name)for p in Project.objects.all()]

class UpdateProjectForm(forms.Form):
    project = forms.ChoiceField(choices=[])  # Choices are set in the initialisation to force an update every refresh
    new_project_name = forms.CharField(max_length=64)

    def __init__(self, *args, **kwargs):
        super(UpdateProjectForm, self).__init__(*args, **kwargs)
        self.fields['project'].choices = [(p.id, p.project_name)for p in Project.objects.all()]  # (p, p) first p is the value it will post, second is the displayed value
