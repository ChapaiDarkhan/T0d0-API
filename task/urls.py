
from task.views import NewTaskView
from django.urls import path

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'new-tasks', NewTaskView, basename='new-tasks')

app_name = "task"
# app_name will help us do a reverse look-up latter.
urlpatterns = router.urls
