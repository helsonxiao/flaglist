from django.db import models
from django.utils import timezone

PRIORITY_CHOICES = (
    (1, 'Important'),
    (2, 'Normal'),
)


class Event(models.Model):
    owner = models.ForeignKey('auth.User', related_name='events')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    expire_date = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='Normal', max_length=50)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __unicode__(self):  # __str__ on python3
        return self.title
