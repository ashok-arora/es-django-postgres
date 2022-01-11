from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)
from .models import Image

PUBLISHER_INDEX = Index("image")

PUBLISHER_INDEX.settings(number_of_shards=1, number_of_replicas=1)


@PUBLISHER_INDEX.doc_type
class ImageDocument(Document):

    id = fields.IntegerField(attr="id")
    image_url = fields.TextField(attr="image_url")
    fielddata = True
    name = fields.TextField(
        fields={
            "raw": {
                "type": "keyword",
            }
        }
    )
    description = fields.TextField(
        fields={
            "raw": {
                "type": "keyword",
            }
        },
    )

    class Django(object):
        model = Image
