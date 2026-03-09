from django.urls import include, path

urlpatterns = [
    path("auth/", include("apps.users.urls", namespace="users")),
    path("todos/", include("apps.todos.urls", namespace="todos")),
]