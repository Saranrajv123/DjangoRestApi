from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.

def upload_to_update_image(instance, filename):
    return "upload/{user}/{filename}".format(user = instance.user, filename = instance.filename)

class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_to_update_image)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        verbose_name = 'status post'
        verbose_name_plural = 'status posts'