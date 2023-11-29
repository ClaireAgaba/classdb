import django_filters
from .models import Video


class Video_filter(django_filters.FilterSet):
    class Meta: #used to manipulate content of another class
        model = Video
        fields = ['title']