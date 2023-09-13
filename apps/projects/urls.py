from django.urls import path

from apps.projects import views

# App name
app_name = "projects"

# App URL Patterns
urlpatterns = [
    path("", views.view_all_projects, name="view_all_projects"),
    path("<int:pk>/", views.view_project, name="view_project"),
    path("create/", views.create_project, name="create_project"),
]
