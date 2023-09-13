from django.urls import path

from apps.core import views

# App Name
app_name = "core"

# URL Patterns
urlpatterns = [
    path("", views.index_view, name="index_view")
]
