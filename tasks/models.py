from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

    @property
    def abstract(self):
        return self.description[:40] + '...'
