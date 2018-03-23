from django.db import models

from . import models


def does_project_exist(project):
    print '---------------------------------------------------------------------------------', project
    name = project.get('project_name')
    if models.Project.objects.filter(project_name=name):
        print 'True'
        return False
    else:
        return True
