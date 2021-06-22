from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Creator
from .serializers import CreatorSerializer


class CreatorViewSet(ReadOnlyModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
