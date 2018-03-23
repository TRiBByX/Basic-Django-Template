# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import Form
from django.db import models


class Delete_Project(Form):
    index = models.IntegerField(max_length=64)