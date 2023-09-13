from datetime import datetime

from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods

from apps.projects.models import Project
from apps.todos.models import Todo


@never_cache
@require_http_methods(["GET"])
def index_view(request):
    """ Dashboard view. Show all Todo objects which are not closed. """
    todos = Todo.objects.filter(closed_on=None)  # Todo objects which are not closed
    projects = Project.objects.all().filter(active=True)  # Projects that are assignable to new Todo objects
    return render(request, template_name="core/index.html",
                  context={"todos": todos, "today": datetime.today(), "projects": projects})
