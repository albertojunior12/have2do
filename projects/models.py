from django.db import models

from categories.models import Category


class Project(models.Model):
    name = models.CharField('Nome', max_length=80)
    description = models.TextField('Descrição', null=True)
    color = models.CharField('Cor de destaque', max_length=7)
    category = models.ForeignKey(Category, verbose_name='Categoria', null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    @property
    def abstract(self):
        return self.description[:40]
