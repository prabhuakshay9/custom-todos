from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.projects.views import Project

# Integrate Project model with django-admin
admin.site.register(Project, SimpleHistoryAdmin)
