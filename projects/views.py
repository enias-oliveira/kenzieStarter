from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Project
from .serializers import ProjectSerializer
from .filters import ProjectFilter


class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.prefetch_related(
        "subcategory", "subcategory__category", "location", "creator"
    )

    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter
