from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='title')
    start = models.DateTimeField()
    end = models.DateTimeField()
    allDay = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    resourceId = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-start', '-end', 'title')


class Resource(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='title')
    eventBackgroundColor = models.CharField(max_length=50, default='#3788d8')
    eventTextColor = models.CharField(max_length=50, default='#fff')
    eventClassNames = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id',)
