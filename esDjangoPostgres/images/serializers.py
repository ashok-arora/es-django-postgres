from rest_framework import serializers
from images.models import Image
from .documents import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        document = ImageDocument
        fields = ("id", "name", "image_url", "description")

        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}
