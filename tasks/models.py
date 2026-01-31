from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=50)
    description = models.TextField(default="", null=False, blank=True)
    status = models.CharField(choices=[("todo", "To Do"), ("doing", "In Progress"), ("done", "Done")], default="todo", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"