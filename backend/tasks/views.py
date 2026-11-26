from django.http import JsonResponse
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.order_by("-created_at")
    serializer_class = TaskSerializer

def health(request):
    return JsonResponse({"status": "ok"})