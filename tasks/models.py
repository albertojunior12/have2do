from django.db import models
from projects.models import Project


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def abstract(self):
        return self.description[:40] + '...'
