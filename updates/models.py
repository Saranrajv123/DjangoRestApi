from django.db import models
import json
from django.core.serializers import serialize
from django.conf import settings
from datetime import datetime

# Create your models here.

def upload_update_image(self, filename):
    return "updates/{user}/{filaname}".format(user=self.user, filename=filename)

class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
    #     query_set = self
    #     return serialize('json', query_set, fields=['user', 'content', 'image'])

    # def serialize(self):
    #     query_set = self
    #     final_array = []
    #     for i in query_set:
    #         load_data = json.loads(i.serialize())
    #         final_array.append(load_data)
    #     return json.dumps(final_array)

    def serialize(self):
        load_list = list(self.values('user', 'content', 'image'))
        print(load_list)
        return json.dumps(load_list)



class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        # json_data = serialize('json', [self], fields=['user', 'content', 'image'])
        # load_data = json.loads(json_data)
        # data = json.dumps(load_data[0]['fields'])
        # print(load_data)
        # print(data)
        # return data
        try:
            image = self.image.url
        except:
            image = ""

        data = {
            'user': self.user,
            'content': self.content,
            'image': image,
        }
        return json.dumps(data)
