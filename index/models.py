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


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

class Group(models.Model):
    id = models.ManyToManyField(Project)
    group_id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(User)


    
