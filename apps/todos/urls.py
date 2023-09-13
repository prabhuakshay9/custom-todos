from django.urls import path

from apps.todos import views

# App Name
app_name = "todos"

# App URL Patterns
urlpatterns = [
    path("", views.view_all_todos, name="all_todos"),
    path("create/", views.create_todo, name="create_todo"),
    path("<int:pk>/mark_as_open/", views.mark_as_open, name="mark_as_open"),
    path("<int:pk>/mark_as_closed/", views.mark_as_closed, name="mark_as_closed"),
    path("day_report/", views.day_report, name="day_report"),
]
