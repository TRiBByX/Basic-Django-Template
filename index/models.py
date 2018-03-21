# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms


class Project(forms.Form):
    project_name = forms.CharField(max_length=64)
    company_name = forms.CharField(max_length=64)
