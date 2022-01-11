from django.urls import include, re_path
from images import views

urlpatterns = [
    re_path(r"^api/images$", views.image_list),
]
