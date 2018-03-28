# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from django.forms import ModelForm


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=64)


class Us3r(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    company = models.ForeignKey(Company)


class Gr0up(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company)
    users = models.ManyToManyField(Us3r)


class Pr0ject(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=64)
    company = models.ForeignKey(Company)
    groups = models.ManyToManyField(Gr0up)
