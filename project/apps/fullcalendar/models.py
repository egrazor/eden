from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='title')
    start = models.DateTimeField()
    end = models.DateTimeField()
    allDay = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-start', '-end', 'title')