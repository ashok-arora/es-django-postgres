from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from images.models import Image
from images.serializers import ImageSerializer
from images.documents import ImageDocument

from rest_framework.decorators import api_view


from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)


@api_view(["GET", "POST", "DELETE"])
def image_list(request):
    # GET list of images, POST a new image, DELETE all images
    if request.method == "GET":
        images = Image.objects.all()

        # title = request.GET.get('title', None)
        # if title is not None:
        #     images = images.filter(title__icontains=title)

        images_serializer = TutorialSerializer(images, many=True)
        return JsonResponse(images_serializer.data, safe=False)

    elif request.method == "POST":
        image_data = JSONParser().parse(request)
        image_serializer = ImageSerializer(data=image_data)
        if image_serializer.is_valid():
            image_serializer.save()
            return JsonResponse(image_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        count = Image.objects.all().delete()
        return JsonResponse(
            {"message": "{} Tutorials were deleted successfully!".format(count[0])},
            status=status.HTTP_204_NO_CONTENT,
        )


class ImageDocumentView(DocumentViewSet):
    document = ImageDocument
    serializer_class = ImageSerializer

    fielddata = True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]

    search_fields = (
        "name",
        "description",
    )
    multi_match_search_fields = (
        "name",
        "description",
    )
    filter_fields = {
        "name": "name",
        "description": "description",
    }
    ordering_fields = {
        "id": None,
    }
    ordering = ("id",)
