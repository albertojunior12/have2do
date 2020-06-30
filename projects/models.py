from django.db import models

from categories.models import Category


class Project(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(null=True)
    color = models.CharField(max_length=7)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def abstract(self):
        return self.description[:40]
