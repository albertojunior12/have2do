from django.db import models
from projects.models import Project


class Task(models.Model):

    PENDING = 0
    DONE = 1
    CANCELED = 2
    STATUS = (
        (PENDING, 'Pendente'),
        (DONE, 'Feito'),
        (CANCELED, 'Cancelado'),
    )

    title = models.CharField('Título', max_length=50)
    description = models.TextField('Descrição')
    status = models.IntegerField('Status', choices=STATUS, default=PENDING)
    project = models.ForeignKey(Project, verbose_name='Projeto', related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tarefa'
        ordering = ['status']

    @property
    def abstract(self):
        return self.description[:40] + '...'
