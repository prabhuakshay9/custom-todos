from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods

from apps.projects.models import Project
from apps.todos.models import Todo


@never_cache
@require_http_methods(["POST"])
def create_todo(request):
    """ Create a To-do object. """
    if request.method == "POST":
        # Get form fields
        title = request.POST.get("title")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        project_id = request.POST.get("project")
        referrer = request.POST.get("referrer", "core:index_view")

        # Create a todo object
        todo = Todo.objects.create(
            title=title,
            description=description,
            deadline=deadline
        )

        # Assign a project if project is selected in form
        if project_id:
            project = get_object_or_404(Project, pk=project_id)
            todo.project = project
            todo.save()

        return redirect(referrer)


@never_cache
@require_http_methods(["GET"])
def view_all_todos(request):
    """ View all todo objects """
    if request.method == "GET":
        # Get form fields
        search = request.GET.get("search", None)

        # Get all todo objects
        todos = Todo.objects.all()

        # If search query is passed, filter todos
        if search:
            todos = todos.filter(Q(title__icontains=search) | Q(description__icontains=search))

        return render(request, "todos/all_todos.html", {"todos": todos, "search": search})


@never_cache
@require_http_methods(["POST"])
def mark_as_closed(request, pk):
    """ Mark a specific todo object as closed """
    if request.method == "POST":
        # Get todo object
        todo = get_object_or_404(Todo, pk=pk)

        # Update closed_on as today
        todo.closed_on = datetime.today()
        todo.save()

        # Get form fields
        referrer = request.POST.get('referrer', "core:index_view")

        return redirect(referrer)


@never_cache
@require_http_methods(["POST"])
def mark_as_open(request, pk):
    """ Mark a specific todo object as open """
    if request.method == "POST":
        # Get todo object
        todo = get_object_or_404(Todo, pk=pk)

        # Remove closed_on
        todo.closed_on = None
        todo.save()

        # Get form fields
        referrer = request.POST.get('referrer', "core:index_view")

        return redirect(referrer)


@never_cache
@require_http_methods(["GET"])
def day_report(request):
    """ View closed_on daily report """
    if request.method == "GET":
        # Get date. If not provided, default to today
        date = request.GET.get("date", datetime.today().strftime("%Y-%m-%d"))
        date = datetime.strptime(date, '%Y-%m-%d').date()

        # Get todo objects closed on given date
        todos = Todo.objects.filter(closed_on=date)

        return render(request, "todos/day_report.html", {"todos": todos, "date": date})
