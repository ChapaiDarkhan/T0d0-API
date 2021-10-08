from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer
from .models import Task


class NewTaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = PostSerializer
