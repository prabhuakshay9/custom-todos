from django.db import models
from simple_history.models import HistoricalRecords


class Project(models.Model):
    """ Project Model. To be tagged against a To-do object. """

    title = models.CharField(max_length=255)  # Project title
    description = models.TextField(blank=True, null=True)  # Project description
    active = models.BooleanField(default=True)  # Project status

    history = HistoricalRecords()  # Audit Log

    class Meta:
        """ Model Meta Info """
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["id"]

    def __str__(self):
        return self.title
