from datetime import datetime

from django.db import models
from simple_history.models import HistoricalRecords

from apps.projects.models import Project


class Todo(models.Model):
    """ To-do objects model. Main model of the website. """

    created_on = models.DateField(editable=False)  # Todo object created date
    closed_on = models.DateField(null=True, blank=True)  # Todo object closed date

    title = models.CharField(max_length=255)  # Todo object title
    description = models.TextField(null=True, blank=True)  # Todo object description
    deadline = models.DateField()  # Todo deadline date
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="todos")  # Tag against a project

    history = HistoricalRecords()  # Audit Log

    class Meta:
        """ Model Meta """
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        ordering = ["id"]

    def save(self, *args, **kwargs):
        """ On create, save created_on  """
        if not self.id:
            self.created_on = datetime.now()
        self.modified = datetime.today()
        return super(Todo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
