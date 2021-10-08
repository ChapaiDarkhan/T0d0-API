from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()


class Task(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    dedline = models.DateTimeField()
    author = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

