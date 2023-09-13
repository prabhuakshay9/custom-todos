from django.contrib import admin
from django.urls import include, path

# URL Patterns
urlpatterns = [
    path("", include("apps.core.urls")),
    path("todos/", include("apps.todos.urls")),
    path("projects/", include("apps.projects.urls")),
    path("admin/", admin.site.urls),
]
