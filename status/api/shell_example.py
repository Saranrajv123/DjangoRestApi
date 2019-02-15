from django.utils.six import BytesIO
from rest_framwork.renderer import JSONRenderer
from rest_framwork.parsers import JSONParser

from Status.api.serializers import StatusSerializer
from Status.models import Status

obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser(stream)
print(data)


qs = Status.objects.all()
serializer2 = StatusSerializer(qs)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data)


stream2 = BytesIO(json_data2)
data2 = JSONParser(stream2)
print(data2)

