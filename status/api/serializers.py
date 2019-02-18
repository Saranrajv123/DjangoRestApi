from rest_framework import serializers
from Status.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

    def validation_content(self, value):
        if len(value) >= 1000:
            raise serializers.validationError('this is too long. ')
        return value
    
    def validate(self, data):
        content = data.get("content", None)
        if content == '':
            content = None
        image = data.get('image', None)

        if content is None and image is None:
            raise serializers.validationError('Content or Image is required')
        return data 

    
      