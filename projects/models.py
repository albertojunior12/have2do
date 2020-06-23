from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null=True)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

    @property
    def abstract(self):
        return self.description[:40]
