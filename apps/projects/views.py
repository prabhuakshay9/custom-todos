from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods

from apps.projects.models import Project


@never_cache
@require_http_methods(["POST"])
def create_project(request):
    """ Create a Project. """
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Project.objects.create(title=title, description=description)
        return redirect("core:index_view")


@never_cache
@require_http_methods(["GET"])
def view_all_projects(request):
    """ View all projects. """
    if request.method == "GET":
        projects = Project.objects.all()
        return render(request, template_name="projects/all_projects.html", context={"projects": projects})


@never_cache
@require_http_methods(["GET"])
def view_project(request, pk):
    """ View a specific project. pk is project ID """
    if request.method == "GET":
        project = get_object_or_404(Project, pk=pk)
        todos = project.todos.filter(project=project)
        return render(request, "projects/project.html", {"project": project, "todos": todos})
