from django.db import models
from django.conf import settings

from utils import models as utils_models


class Faculty(models.Model):
    name = models.CharField(max_length=200)
    dean = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="faculty_dean",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'faculties'


class Department(models.Model):
    name = models.CharField(max_length=200)
    head = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="department_head",
        on_delete=models.CASCADE
    )
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.DO_NOTHING,
        blank=True, null=True
    )

    def __str__(self):
        return self.name


class Direction(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name='direction_department'
                                   )
    years = models.PositiveSmallIntegerField()
    degree = models.CharField(max_length=50, blank=True, null=True,
                              choices=[(choice.name, choice.value)
                                       for choice in utils_models.StudyDegree],
    )

    def __str__(self):
        return self.short_name

    class Meta:
        ordering = ('short_name',)