from django.db import models

from . import models


def does_project_exist(project):
    print '---------------------------------------------------------------------------------', project
    id = project.get('id')
    if models.Project.objects.filter(id=id):
        print 'True'
        return False
    else:
        return True
