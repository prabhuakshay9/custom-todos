from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from apps.todos.models import Todo

# Integrate Todo model with django-admin
admin.site.register(Todo, SimpleHistoryAdmin)
