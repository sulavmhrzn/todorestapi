from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo

from .serializers import TodoSerializer


class TodoViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects
    serializer_class = TodoSerializer

    def get_queryset(self):
        """
        override get_queryset to return todos created by logged in user.
        """
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        override perform_create to assign current logged in user.
        """
        return serializer.save(user=self.request.user)
