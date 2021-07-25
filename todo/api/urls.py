from django.urls import path

from rest_framework import routers

from .views import TodoViewset, CompletedTodoView

router = routers.DefaultRouter()
router.register(prefix="todos", viewset=TodoViewset)

urlpatterns = [
    path("todos/completed/", CompletedTodoView.as_view(), name='todo-completed'),
]

urlpatterns += router.urls
